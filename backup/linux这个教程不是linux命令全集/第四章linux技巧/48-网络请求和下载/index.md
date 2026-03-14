---
{
  "id": "3155a2dd-8276-81d3-9cfc-f095a4abbc98",
  "url": "https://www.notion.so/4-8-3155a2dd827681d39cfcf095a4abbc98",
  "created_time": "2026-02-28T12:47:00.000Z",
  "last_edited_time": "2026-02-28T12:47:00.000Z"
}
---

#  4.8 网络请求和下载

# ping命令（检查服务器是否联通）
```shell
ping [-c num] ip或主机名
```
- -c ：ping的次数，不使用-c将持续ping
# wget命令（下载）
```shell
wget [-b] url
```
- -b：后台下载
- url：网址
PS：Ctrl+c可以中断下载，但不会删除已下载的部分
# curl命令（发送HTTP请求）
**当发送curl命令时，会返回HTML源码**
```shell
curl [-O] url
```
- -O：下载文件，当url是下载链接时，可保存文件。
- 不带大O，仅返回HTML源码，不保存文件。
