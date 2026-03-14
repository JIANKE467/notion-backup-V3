---
{
  "id": "3155a2dd-8276-8150-a397-e32229e14157",
  "url": "https://www.notion.so/3-2-3155a2dd82768150a397e32229e14157",
  "created_time": "2026-02-28T12:47:00.000Z",
  "last_edited_time": "2026-02-28T12:47:00.000Z"
}
---

#  3.2 用户，用户组管理

# 用户组（需root权限）
### 创建（groupadd命令）
```shell
groupadd 用户组名
```
### 删除（groupdel命令）
```shell
groupdel 用户组名
```
# 用户（root权限）
### 创建（useradd命令）
```shell
useradd [-g] 用户组名 [-d] 路径 用户名
```
- -g：指定用户组，如不指定，会创建同名用户组并自动加入
- -d：指定用户home路径，不指定默认在 ` /home/用户名`  下
**注意⚠️**
不带-m（创建路径）可能会出现问题，因为-d只是指定了地址，并没有创建。
最好将用户名写到后面，否则在某些特定情况下Shell解析器无法解析。
### 删除（userdel命令）
```shell
userdel [-r] 用户名
```
- -r：删除用户的home目录，不使用默认保留
### 查看用户所属组（id命令）
```shell
id [用户名]
```
- 用户名不填，默认查看当前用户
查看自己不用root权限
### 修改用户所属组（usermod命令）
```shell
uesrmod -aG 用户组 用户名
```
将指定用户加入指定用户组
# getent命令（root权限）
### 查看有哪些用户
```shell
getent passwd
```
为什么是passwd，这是一个历史遗留问题，早期的unix密码跟用户放到一个文件里，所以这样写
输出：用户名，密码（不是明文），用户ID，组ID，描述信息，home目录，执行终端
### 查看哪些组
```shell
getent group
```
输出：组名称，组认证，组ID
