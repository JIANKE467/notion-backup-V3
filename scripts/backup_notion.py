#!/usr/bin/env python3
import argparse
import datetime as dt
import json
import os
import re
import time
from typing import Any, Dict, List, Optional, Tuple

import requests


NOTION_API_BASE = "https://api.notion.com/v1"
NOTION_VERSION = "2025-09-03"


class NotionClient:
    def __init__(self, token: str, requests_per_second: float, max_retries: int) -> None:
        self._token = token
        self._min_interval = 1.0 / max(0.1, requests_per_second)
        self._max_retries = max_retries
        self._last_request_ts = 0.0

    def _sleep_for_rate_limit(self) -> None:
        now = time.time()
        wait = self._min_interval - (now - self._last_request_ts)
        if wait > 0:
            time.sleep(wait)
        self._last_request_ts = time.time()

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json_body: Optional[Dict[str, Any]] = None,
        stream: bool = False,
    ) -> requests.Response:
        url = f"{NOTION_API_BASE}{path}"
        headers = {
            "Authorization": f"Bearer {self._token}",
            "Notion-Version": NOTION_VERSION,
        }
        for attempt in range(self._max_retries + 1):
            self._sleep_for_rate_limit()
            resp = requests.request(
                method,
                url,
                headers=headers,
                params=params,
                json=json_body,
                stream=stream,
                timeout=60,
            )
            if resp.status_code == 429:
                retry_after = resp.headers.get("Retry-After")
                delay = float(retry_after) if retry_after else min(2 ** attempt, 30)
                time.sleep(delay)
                continue
            if resp.status_code >= 500 and attempt < self._max_retries:
                time.sleep(min(2 ** attempt, 30))
                continue
            resp.raise_for_status()
            return resp
        resp.raise_for_status()
        return resp


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^\w\s-\u4e00-\u9fff]", "", value)
    value = re.sub(r"[\s_-]+", "-", value)
    return value or "untitled"


def unique_slug(base: str, used: Dict[str, int]) -> str:
    if base not in used:
        used[base] = 1
        return base
    used[base] += 1
    return f"{base}-{used[base]}"


def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def write_text(path: str, text: str) -> None:
    ensure_dir(os.path.dirname(path))
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def read_json(resp: requests.Response) -> Dict[str, Any]:
    return resp.json()


def rich_text_to_md(rich_text: List[Dict[str, Any]]) -> str:
    parts: List[str] = []
    for rt in rich_text or []:
        text = rt.get("plain_text", "")
        if rt.get("href"):
            text = f"[{text}]({rt['href']})"
        annotations = rt.get("annotations", {})
        if annotations.get("code"):
            text = f"`{text}`"
        if annotations.get("bold"):
            text = f"**{text}**"
        if annotations.get("italic"):
            text = f"*{text}*"
        if annotations.get("strikethrough"):
            text = f"~~{text}~~"
        if annotations.get("underline"):
            text = f"<u>{text}</u>"
        parts.append(text)
    return "".join(parts)


def rich_text_plain(rich_text: List[Dict[str, Any]]) -> str:
    return "".join(rt.get("plain_text", "") for rt in (rich_text or [])) or ""


def get_page_title(page: Dict[str, Any]) -> str:
    props = page.get("properties", {})
    for prop in props.values():
        if prop.get("type") == "title":
            return rich_text_to_md(prop.get("title", [])) or "Untitled"
    return "Untitled"


def get_page_title_plain(page: Dict[str, Any]) -> str:
    props = page.get("properties", {})
    for prop in props.values():
        if prop.get("type") == "title":
            return rich_text_plain(prop.get("title", [])) or "Untitled"
    return "Untitled"


def get_database_title(db: Dict[str, Any]) -> str:
    return rich_text_to_md(db.get("title", [])) or "Untitled Database"


def get_database_title_plain(db: Dict[str, Any]) -> str:
    return rich_text_plain(db.get("title", [])) or "Untitled Database"


def extract_icon(block_or_page: Dict[str, Any]) -> str:
    icon = block_or_page.get("icon")
    if not icon:
        return ""
    if icon.get("type") == "emoji":
        return icon.get("emoji", "")
    return ""


def list_all(client: NotionClient, path: str, body: Dict[str, Any]) -> List[Dict[str, Any]]:
    results: List[Dict[str, Any]] = []
    start_cursor = None
    while True:
        payload = dict(body)
        if start_cursor:
            payload["start_cursor"] = start_cursor
        resp = client.request("POST", path, json_body=payload)
        data = read_json(resp)
        results.extend(data.get("results", []))
        if not data.get("has_more"):
            break
        start_cursor = data.get("next_cursor")
    return results


def get_blocks(client: NotionClient, block_id: str) -> List[Dict[str, Any]]:
    results: List[Dict[str, Any]] = []
    start_cursor = None
    while True:
        params = {"page_size": 100}
        if start_cursor:
            params["start_cursor"] = start_cursor
        resp = client.request("GET", f"/blocks/{block_id}/children", params=params)
        data = read_json(resp)
        results.extend(data.get("results", []))
        if not data.get("has_more"):
            break
        start_cursor = data.get("next_cursor")
    return results


def download_asset(client: NotionClient, url: str, dest_path: str) -> None:
    ensure_dir(os.path.dirname(dest_path))
    for attempt in range(3):
        try:
            if url.startswith(NOTION_API_BASE):
                resp = client.request("GET", url.replace(NOTION_API_BASE, ""), stream=True)
            else:
                resp = requests.get(url, stream=True, timeout=60)
            resp.raise_for_status()
            with open(dest_path, "wb") as f:
                for chunk in resp.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            return
        except requests.RequestException:
            if attempt == 2:
                raise
            time.sleep(min(2 ** attempt, 10))


def sanitize_filename(name: str) -> str:
    name = re.sub(r"[^\w\s.-]", "", name).strip()
    return name or "file"


def resolve_file_ext(url: str, default: str = "bin") -> str:
    match = re.search(r"\.([a-zA-Z0-9]{1,6})(?:\?|$)", url)
    if match:
        return match.group(1)
    return default


def block_children_to_md(
    client: NotionClient,
    blocks: List[Dict[str, Any]],
    page_ctx: Dict[str, Any],
    indent: int = 0,
) -> Tuple[str, List[str]]:
    md_lines: List[str] = []
    discovered_child_pages: List[str] = []

    i = 0
    while i < len(blocks):
        block = blocks[i]
        block_type = block.get("type")
        prefix = "  " * indent

        if block_type in ("bulleted_list_item", "numbered_list_item", "to_do"):
            list_type = block_type
            list_lines: List[str] = []
            while i < len(blocks) and blocks[i].get("type") == list_type:
                item = blocks[i]
                text = rich_text_to_md(item[list_type].get("rich_text", []))
                if list_type == "bulleted_list_item":
                    line = f"{prefix}- {text}"
                elif list_type == "numbered_list_item":
                    line = f"{prefix}1. {text}"
                else:
                    checked = item[list_type].get("checked", False)
                    mark = "x" if checked else " "
                    line = f"{prefix}- [{mark}] {text}"
                list_lines.append(line)
                if item.get("has_children"):
                    children = get_blocks(client, item["id"])
                    child_md, child_pages = block_children_to_md(client, children, page_ctx, indent + 1)
                    if child_md:
                        list_lines.append(child_md.rstrip())
                    discovered_child_pages.extend(child_pages)
                i += 1
            md_lines.extend(list_lines)
            continue

        if block_type == "paragraph":
            text = rich_text_to_md(block["paragraph"].get("rich_text", []))
            md_lines.append(f"{prefix}{text}" if text else "")
        elif block_type == "heading_1":
            text = rich_text_to_md(block["heading_1"].get("rich_text", []))
            md_lines.append(f"{prefix}# {text}")
        elif block_type == "heading_2":
            text = rich_text_to_md(block["heading_2"].get("rich_text", []))
            md_lines.append(f"{prefix}## {text}")
        elif block_type == "heading_3":
            text = rich_text_to_md(block["heading_3"].get("rich_text", []))
            md_lines.append(f"{prefix}### {text}")
        elif block_type == "quote":
            text = rich_text_to_md(block["quote"].get("rich_text", []))
            md_lines.append(f"{prefix}> {text}")
        elif block_type == "code":
            text = rich_text_to_md(block["code"].get("rich_text", []))
            lang = block["code"].get("language") or ""
            md_lines.append(f"{prefix}```{lang}")
            md_lines.append(text)
            md_lines.append(f"{prefix}```")
        elif block_type == "divider":
            md_lines.append(f"{prefix}---")
        elif block_type == "callout":
            text = rich_text_to_md(block["callout"].get("rich_text", []))
            icon = extract_icon(block)
            header = f"{icon} " if icon else ""
            md_lines.append(f"{prefix}> {header}{text}")
        elif block_type == "toggle":
            text = rich_text_to_md(block["toggle"].get("rich_text", []))
            md_lines.append(f"{prefix}<details>")
            md_lines.append(f"{prefix}<summary>{text}</summary>")
            if block.get("has_children"):
                children = get_blocks(client, block["id"])
                child_md, child_pages = block_children_to_md(client, children, page_ctx, indent + 1)
                if child_md:
                    md_lines.append(child_md.rstrip())
                discovered_child_pages.extend(child_pages)
            md_lines.append(f"{prefix}</details>")
        elif block_type == "image":
            image = block["image"]
            if image.get("type") == "external":
                url = image["external"].get("url")
            else:
                url = image["file"].get("url")
            if url:
                ext = resolve_file_ext(url, "png")
                fname = sanitize_filename(f"{block['id']}.{ext}")
                asset_path = os.path.join(page_ctx["assets_dir"], fname)
                download_asset(client, url, asset_path)
                rel_path = os.path.relpath(asset_path, page_ctx["page_dir"])
                md_lines.append(f"{prefix}![]({rel_path.replace(os.sep, '/')})")
        elif block_type == "file":
            file_obj = block["file"]
            if file_obj.get("type") == "external":
                url = file_obj["external"].get("url")
            else:
                url = file_obj["file"].get("url")
            if url:
                ext = resolve_file_ext(url, "bin")
                fname = sanitize_filename(f"{block['id']}.{ext}")
                asset_path = os.path.join(page_ctx["assets_dir"], fname)
                download_asset(client, url, asset_path)
                rel_path = os.path.relpath(asset_path, page_ctx["page_dir"])
                md_lines.append(f"{prefix}[Download file]({rel_path.replace(os.sep, '/')})")
        elif block_type == "bookmark":
            url = block["bookmark"].get("url")
            if url:
                md_lines.append(f"{prefix}[{url}]({url})")
        elif block_type == "equation":
            expr = block["equation"].get("expression", "")
            md_lines.append(f"{prefix}$$\n{expr}\n$$")
        elif block_type == "table":
            table_rows = []
            if block.get("has_children"):
                children = get_blocks(client, block["id"])
                for child in children:
                    if child.get("type") == "table_row":
                        cells = []
                        for cell in child["table_row"].get("cells", []):
                            cells.append(rich_text_to_md(cell))
                        table_rows.append(cells)
            if table_rows:
                header = table_rows[0]
                md_lines.append(prefix + "| " + " | ".join(header) + " |")
                md_lines.append(prefix + "| " + " | ".join(["---"] * len(header)) + " |")
                for row in table_rows[1:]:
                    md_lines.append(prefix + "| " + " | ".join(row) + " |")
        elif block_type == "child_page":
            title = block["child_page"].get("title", "Untitled")
            child_id = block["id"]
            discovered_child_pages.append(child_id)
            link = page_ctx.get("page_links", {}).get(child_id, "")
            if link:
                md_lines.append(f"{prefix}[{title}]({link})")
            else:
                md_lines.append(f"{prefix}{title}")
        elif block_type == "unsupported":
            md_lines.append(f"{prefix}<!-- unsupported block type -->")
        else:
            text = block.get(block_type, {}).get("rich_text")
            if text:
                md_lines.append(f"{prefix}{rich_text_to_md(text)}")

        if block.get("has_children") and block_type not in (
            "toggle",
            "table",
            "bulleted_list_item",
            "numbered_list_item",
            "to_do",
        ):
            children = get_blocks(client, block["id"])
            child_md, child_pages = block_children_to_md(client, children, page_ctx, indent + 1)
            if child_md:
                md_lines.append(child_md.rstrip())
            discovered_child_pages.extend(child_pages)

        i += 1

    return "\n".join(md_lines).rstrip() + "\n", discovered_child_pages


def build_front_matter(page: Dict[str, Any]) -> str:
    data = {
        "id": page.get("id"),
        "url": page.get("url"),
        "created_time": page.get("created_time"),
        "last_edited_time": page.get("last_edited_time"),
    }
    return "---\n" + json.dumps(data, ensure_ascii=False, indent=2) + "\n---\n\n"


def compute_page_path(
    page_id: str,
    pages: Dict[str, Dict[str, Any]],
    databases: Dict[str, Dict[str, Any]],
    data_sources: Dict[str, Dict[str, Any]],
    page_paths: Dict[str, str],
    db_paths: Dict[str, str],
    slug_registry: Dict[str, Dict[str, int]],
    root: str,
) -> str:
    if page_id in page_paths:
        return page_paths[page_id]

    page = pages[page_id]
    parent = page.get("parent", {})
    parent_type = parent.get("type")

    if parent_type == "workspace" or not parent_type:
        parent_dir = root
    elif parent_type == "page_id":
        parent_id = parent.get("page_id")
        parent_path = compute_page_path(
            parent_id, pages, databases, data_sources, page_paths, db_paths, slug_registry, root
        )
        parent_dir = os.path.dirname(parent_path)
    elif parent_type in ("database_id", "data_source_id"):
        if parent_type == "database_id":
            db_id = parent.get("database_id")
        else:
            db_id = data_sources.get(parent.get("data_source_id"), {}).get("database_id")
        if db_id and db_id in databases:
            parent_dir = compute_db_path(
                db_id, pages, databases, data_sources, page_paths, db_paths, slug_registry, root
            )
        else:
            parent_dir = root
    else:
        parent_dir = root

    title = get_page_title_plain(page)
    slug_base = slugify(title)
    registry = slug_registry.setdefault(parent_dir, {})
    slug = unique_slug(slug_base, registry)
    page_dir = os.path.join(parent_dir, slug)
    page_path = os.path.join(page_dir, "index.md")
    page_paths[page_id] = page_path
    return page_path


def compute_db_path(
    db_id: str,
    pages: Dict[str, Dict[str, Any]],
    databases: Dict[str, Dict[str, Any]],
    data_sources: Dict[str, Dict[str, Any]],
    page_paths: Dict[str, str],
    db_paths: Dict[str, str],
    slug_registry: Dict[str, Dict[str, int]],
    root: str,
) -> str:
    if not db_id:
        return root
    if db_id in db_paths:
        return db_paths[db_id]

    db = databases[db_id]
    parent = db.get("parent", {})
    parent_type = parent.get("type")

    if parent_type == "workspace" or not parent_type:
        parent_dir = root
    elif parent_type == "page_id":
        parent_id = parent.get("page_id")
        parent_path = compute_page_path(
            parent_id, pages, databases, data_sources, page_paths, db_paths, slug_registry, root
        )
        parent_dir = os.path.dirname(parent_path)
    else:
        parent_dir = root

    title = get_database_title_plain(db)
    slug_base = slugify(title)
    registry = slug_registry.setdefault(parent_dir, {})
    slug = unique_slug(slug_base, registry)
    db_dir = os.path.join(parent_dir, f"{slug}-db")
    db_paths[db_id] = db_dir
    return db_dir


def main() -> None:
    parser = argparse.ArgumentParser(description="Backup Notion workspace to Markdown.")
    parser.add_argument("--output", default="backup", help="Output directory")
    parser.add_argument("--requests-per-second", type=float, default=2.5)
    parser.add_argument("--max-retries", type=int, default=5)
    parser.add_argument("--log-every", type=int, default=20, help="Log progress every N pages")
    args = parser.parse_args()

    token = os.environ.get("NOTION_TOKEN")
    if not token:
        raise SystemExit("NOTION_TOKEN environment variable is required.")

    client = NotionClient(token, args.requests_per_second, args.max_retries)
    output_root = args.output
    ensure_dir(output_root)

    pages: Dict[str, Dict[str, Any]] = {}
    databases: Dict[str, Dict[str, Any]] = {}
    data_sources: Dict[str, Dict[str, Any]] = {}
    parent_children: Dict[str, List[str]] = {}

    def index_parent_child(page_obj: Dict[str, Any]) -> None:
        parent = page_obj.get("parent", {})
        if parent.get("type") == "page_id":
            parent_id = parent.get("page_id")
            parent_children.setdefault(parent_id, []).append(page_obj["id"])

    print("Scanning Notion workspace...")
    pages_list = list_all(
        client,
        "/search",
        {"page_size": 100, "filter": {"property": "object", "value": "page"}},
    )
    for page in pages_list:
        pages[page["id"]] = page
        index_parent_child(page)

    data_source_list = list_all(
        client,
        "/search",
        {"page_size": 100, "filter": {"property": "object", "value": "data_source"}},
    )
    for ds in data_source_list:
        parent = ds.get("parent", {})
        db_id = parent.get("database_id")
        data_sources[ds["id"]] = {"database_id": db_id, "name": ds.get("name")}
        if db_id and db_id not in databases:
            db_resp = client.request("GET", f"/databases/{db_id}")
            databases[db_id] = read_json(db_resp)

    for ds_id in list(data_sources.keys()):
        ds_pages = list_all(client, f"/data_sources/{ds_id}/query", {"page_size": 100})
        for page in ds_pages:
            pages.setdefault(page["id"], page)
            index_parent_child(page)

    print(f"Found {len(pages)} pages, {len(databases)} databases, {len(data_sources)} data sources.")

    page_paths: Dict[str, str] = {}
    db_paths: Dict[str, str] = {}
    slug_registry: Dict[str, Dict[str, int]] = {}

    export_queue = list(pages.keys())
    exported: set = set()

    processed = 0
    while export_queue:
        page_id = export_queue.pop(0)
        if page_id in exported:
            continue

        if page_id not in pages:
            page_resp = client.request("GET", f"/pages/{page_id}")
            pages[page_id] = read_json(page_resp)

        page = pages[page_id]
        processed += 1
        total_pages = len(exported) + len(export_queue) + 1
        if args.log_every > 0 and (
            processed == 1 or processed == total_pages or processed % args.log_every == 0
        ):
            title = get_page_title_plain(page)
            print(f"[{processed}/{total_pages}] Exporting: {title}")
        page_path = compute_page_path(
            page_id, pages, databases, data_sources, page_paths, db_paths, slug_registry, output_root
        )
        page_dir = os.path.dirname(page_path)
        assets_dir = os.path.join(page_dir, "assets")
        ensure_dir(page_dir)

        page_links: Dict[str, str] = {}
        for child_id in parent_children.get(page_id, []):
            child_path = compute_page_path(
                child_id, pages, databases, data_sources, page_paths, db_paths, slug_registry, output_root
            )
            page_links[child_id] = os.path.relpath(child_path, page_dir).replace(os.sep, "/")

        blocks = get_blocks(client, page_id)
        page_ctx = {"page_dir": page_dir, "assets_dir": assets_dir, "page_links": page_links}
        body_md, child_pages = block_children_to_md(client, blocks, page_ctx)

        for child_id in child_pages:
            if child_id not in pages:
                child_resp = client.request("GET", f"/pages/{child_id}")
                pages[child_id] = read_json(child_resp)
                index_parent_child(pages[child_id])
            if child_id not in export_queue and child_id not in exported:
                export_queue.append(child_id)

        front_matter = build_front_matter(page)
        title = get_page_title(page)
        icon = extract_icon(page)
        heading = f"# {icon} {title}".strip()
        content = front_matter + f"{heading}\n\n" + body_md
        write_text(page_path, content)
        exported.add(page_id)

    for db_id, db in databases.items():
        db_dir = compute_db_path(
            db_id, pages, databases, data_sources, page_paths, db_paths, slug_registry, output_root
        )
        ensure_dir(db_dir)
        title = get_database_title(db)
        heading = f"# {title}\n\n"
        lines = [heading, "## Rows\n"]
        for page_id, page in pages.items():
            parent = page.get("parent", {})
            if parent.get("type") == "database_id" and parent.get("database_id") == db_id:
                page_path = compute_page_path(
                    page_id, pages, databases, data_sources, page_paths, db_paths, slug_registry, output_root
                )
                rel = os.path.relpath(page_path, db_dir).replace(os.sep, "/")
                lines.append(f"- [{get_page_title(page)}]({rel})")
            if parent.get("type") == "data_source_id":
                ds = data_sources.get(parent.get("data_source_id"))
                if ds and ds.get("database_id") == db_id:
                    page_path = compute_page_path(
                        page_id, pages, databases, data_sources, page_paths, db_paths, slug_registry, output_root
                    )
                    rel = os.path.relpath(page_path, db_dir).replace(os.sep, "/")
                    lines.append(f"- [{get_page_title(page)}]({rel})")
        write_text(os.path.join(db_dir, "index.md"), "\n".join(lines) + "\n")

    manifest = {
        "generated_at": dt.datetime.utcnow().isoformat() + "Z",
        "notion_version": NOTION_VERSION,
        "page_count": len(exported),
        "database_count": len(databases),
    }
    write_text(os.path.join(output_root, "manifest.json"), json.dumps(manifest, ensure_ascii=False, indent=2))
    print("Backup complete.")


if __name__ == "__main__":
    main()
