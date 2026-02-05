# Notion 备份（GitHub Actions）

本项目使用 GitHub Actions 定期将整个 Notion 工作区完整备份为 Markdown。

## 功能
- 全量备份（非增量）。
- 将 Notion block 转换为 Markdown。
- 用文件夹结构尽量还原 Notion 的页面/数据库层级（data source 按所属数据库归档）。
- 下载图片/文件到本地并重写为本地引用。

## 配置
1. 创建 Notion Integration，并把工作区共享给它。
2. 在 GitHub 仓库 Secrets 中添加 `NOTION_TOKEN`。
3. 推送仓库。

## 运行方式
- 自动：每天 02:00 UTC 运行。
- 手动：在 Actions 里运行 `Notion Backup` 工作流。

## 分支说明
- `main`：存放脚本与配置。
- `data`：只存放备份输出（`backup/` 目录）。

## 数据清理
- 仓库包含每周一次的 `data` 分支历史清理（仅保留当前内容的单次提交）。
- 触发方式：Actions 中的 `Data Branch Cleanup` 或定时任务。
- 清理流程只在最后 `git push --force` 成功时才会替换 `data` 分支。

## 输出结构
- 备份输出在 `backup/`。
- 每个页面写到 `backup/<page-slug>/index.md`。
- 资源文件写到 `backup/<page-slug>/assets/`。
- 数据库会有独立目录，并生成 `index.md` 列出行。

## 本地运行
1. 安装依赖：`pip install -r requirements.txt`
2. 设置环境变量：`NOTION_TOKEN=你的token`
3. 运行：`python scripts/backup_notion.py --output backup`

## 调试与日志
- `--log-every N`：每导出 N 个页面打印一次进度（默认 20）。
- `--requests-per-second X`：限制请求速率（默认 2.5）。
- `--max-retries N`：请求失败重试次数（默认 5）。

## 说明
- 请求头固定使用最新 Notion API 版本。
- 内置限速与重试，降低被限流的概率。
- 每次运行都是全量备份。
- 页面标题转 slug 时会保留中文字符；如果标题为空或清洗后为空，会回退为 `untitled`。

## 拉取/下载 注意
- 如果要拉取/维护脚本文件，只拉取main分支即可，用如下命令：
git clone -b main --single-branch --depth 1 git@github.com:JIANKE467/notion-backup-V3.git
- 如果要查看备份的数据，不要拉取！直接下载data分支文件（图片太多拉取不下来）