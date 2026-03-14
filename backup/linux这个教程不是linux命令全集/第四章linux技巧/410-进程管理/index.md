---
{
  "id": "3155a2dd-8276-812b-a7b2-f2a8a3eb03cd",
  "url": "https://www.notion.so/4-10-3155a2dd8276812ba7b2f2a8a3eb03cd",
  "created_time": "2026-02-28T12:47:00.000Z",
  "last_edited_time": "2026-02-28T12:47:00.000Z"
}
---

#  4.10 进程管理

# 查看进程
```shell
ps [-e -f]
```
- -e：显示全部进程
- -f：格式化显示
### 输出项目：
- UID：进程所属用户ID
- pid：进程id
- ppid：父进程id
- c：CPU占用率
- stime：进程启动时间
- tty：启动此进程的终端编号（？为非终端启动，如系统启动）
- time：进程占用CPU时间
- cmd：启动命令/启动路径
PS：
可通过管道符+grep进行过滤
# 关闭进程kill
```shell
kill [-9] 进程ID
```
- -9：强制关闭
PS：
不强制关闭，被关闭的进程会显示terminaled（被终止）
强制关闭，被关闭的进程会显示killed（被杀死）
