---
{
  "id": "3155a2dd-8276-816c-9498-d1f52d4336a6",
  "url": "https://www.notion.so/2-8-3155a2dd8276816c9498d1f52d4336a6",
  "created_time": "2026-02-28T12:47:00.000Z",
  "last_edited_time": "2026-02-28T12:47:00.000Z"
}
---

#  2.8 查找命令

# which命令（查找命令）
**在Linux中各种命令都是程序文件**
**which命令用来查找某命令的程序文件的位置**
### 语法
```shell
which 要查找的命令
```
# find命令（查找文件）
find命令用来查找文件
### 语法（按文件名查找）
```shell
find 起始路径 -name "被查找文件名"
```
PS：
起始路径指定了从哪搜索
find支持通配符模糊匹配
### 语法（按大小查找）
```shell
find 起始路径 -size +|-n[kMG]
```
PS：
- +|-：代表大于或小于
- n：代表大小
- kMG：代表单位：k（小写）表示kb，M表示MB，G表示GB
例子：
在根目录查找小于10kb的文件
```shell
find / -size -10k
```
如果是区间限制（如10k到10M），这么写
```shell
find / -size +10k -size -10M
```
