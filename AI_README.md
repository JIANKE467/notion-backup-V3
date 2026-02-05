# AI Maintenance Notes (No Prior Context)

This repository is a GitHub Actions automation that backs up an entire Notion workspace to Markdown.

## High-Level Requirements
- Full backup only (no incremental).
- Rate limit and retries to avoid Notion API failures.
- Use the latest Notion API version header.
- Convert all Notion content to Markdown (do not save raw API JSON).
- Preserve the Notion hierarchy using folders.
- Download images/files locally and reference them in Markdown.
- Token is provided by GitHub secret `NOTION_TOKEN`.

## Entry Points
- Workflow: `.github/workflows/notion-backup.yml`
- Script: `scripts/backup_notion.py`
- Dependencies: `requirements.txt`

## How The Script Works
- Calls Notion Search API to list all pages and data sources.
- Queries each data source to capture all rows (2025-09-03 API).
- Recursively fetches blocks for each page, converting to Markdown.
- Detects `child_page` blocks and backs them up too.
- Stores pages in `backup/<page-slug>/index.md`.
- Stores assets in `backup/<page-slug>/assets/`.
- Writes `backup/manifest.json` with counts and API version.

## Operational Notes
- Runs on a schedule and can be triggered manually.
- Commits changes to the repo if backup output changed.
- `main` branch stores code/config; `data` branch stores only `backup/` output.
- Local run: set `NOTION_TOKEN`, then `python scripts/backup_notion.py --output backup`.
- Logging flags: `--log-every`, `--requests-per-second`, `--max-retries`.
- Slugify keeps Chinese characters; empty titles fall back to `untitled`.
