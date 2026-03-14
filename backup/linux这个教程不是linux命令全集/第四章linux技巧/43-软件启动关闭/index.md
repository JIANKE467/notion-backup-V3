---
{
  "id": "3155a2dd-8276-814f-940b-f08654a4d08b",
  "url": "https://www.notion.so/4-3-3155a2dd8276814f940bf08654a4d08b",
  "created_time": "2026-02-28T12:47:00.000Z",
  "last_edited_time": "2026-02-28T12:47:00.000Z"
}
---

#  4.3 软件启动关闭

### systemctl命令（控制软件启/停/自启）
能被systemctl管理的软件一般称为服务
```shell
systemctl start | stop | status | enable | disable 服务名
```
- start  启动
- stop 停止
- status 查看当前状态
- enable 开机自启
- disable 关闭开机自启
PS：有些软件在安装时没有自动注册到systemctl中，所以无法管理，想管理可以手动注册进去
