# Notion 备份（GitHub Actions）

本项目使用 GitHub Actions 定期将整个 Notion 工作区完整备份为 Markdown。

## 功能
- 全量备份（非增量）。
- 将 Notion block 转换为 Markdown。
- 用文件夹结构尽量还原 Notion 的页面/数据库层级。
- 下载图片/文件到本地并重写为本地引用。

## 配置
1. 创建 Notion Integration，并把工作区共享给它。
2. 在 GitHub 仓库 Secrets 中添加 `NOTION_TOKEN`。
3. 推送仓库。

## 运行方式
- 自动：每天 02:00 UTC 运行。
- 手动：在 Actions 里运行 `Notion Backup` 工作流。

## 输出结构
- 备份输出在 `backup/`。
- 每个页面写到 `backup/<page-slug>/index.md`。
- 资源文件写到 `backup/<page-slug>/assets/`。
- 数据库会有独立目录，并生成 `index.md` 列出行。

## 说明
- 请求头固定使用最新 Notion API 版本。
- 内置限速与重试，降低被限流的概率。
- 每次运行都是全量备份。
