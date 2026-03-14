---
{
  "id": "3155a2dd-8276-813a-99ae-f165f8e596f8",
  "url": "https://www.notion.so/3-1-root-3155a2dd8276813a99aef165f8e596f8",
  "created_time": "2026-02-28T12:47:00.000Z",
  "last_edited_time": "2026-02-28T12:47:00.000Z"
}
---

#  3.1 认识root用户

root用户是超级管理员，有最大权限
普通用户，一般在home目录下不受限，其他目录都受限
# su命令（切换用户）
switch user 的简写，切换用户
### 语法
```shell
su [-] [用户名]
```
- -符号：表示是否在切换后加载环境变量
- 用户名：省略默认切换到root用户
- 使用`exit命令`退出到上一个用户
- root切换到另一个用户不用输密码
# sudo命令（临时使用root权限）
### 语法
```shell
sudo 其他命令
```
- **只有配置过sudo认证的用户才能用sudo命令**
### 配置sudo认证
1. 切换到root用户
1. 执行visudo命令，会用编辑器自动打开/etc/sudoers
1. 在文件最后添加
```plain text
用户名 ALL=(ALL)    NOPASWARD: ALL
```
NOPASSWARD：ALL 表示使用sudo命令无需输密码
1. 保存，退出root用户

**部分系统的初始用户没配置sudo也能用sudo是因为，系统在安装时自动将初始用户加入了sudo组**
