---
{
  "id": "3ee5a2dd-8276-83d3-a23f-81766efead82",
  "url": "https://app.notion.com/p/5-3ee5a2dd827683d3a23f81766efead82",
  "created_time": "2026-03-03T14:42:00.000Z",
  "last_edited_time": "2026-03-03T14:42:00.000Z"
}
---

#  5.安装，配置

# win
去官网下，安装
安装好了任意界面右键可以看到git gui （图形化）和git bash（命令行）
# 配置git（让其能够使用）
### 1. 打开git bash
### 2. 设置用户信息（用户名和邮件）
```shell
git config --global user.name "用户名"
#设置用户名
```
```shell
git config --global user.email "邮箱"
#设置邮箱
```
PS：用户名，邮箱不用一定是真的

查看配置信息
```shell
git config --global user.name
#查看用户名
```
```shell
git config --global user.email
```
### 3. 为指令配置别名（可选）
Git bath 是一个Linux环境（即便他在Windows上运行），所以也就是配置Linux命令别名

方法：
在`/home/用户名`目录下创建一个`.bashrc`文件，并在该文件中输入
```shell
alias 命令别名='原命令'
#原命令可以带选项和参数
```
然后打开git bash输入命令：`source ~/.bashrc`
# 解决gitbash乱码问题（如果）
打开Git Bash，右键点击窗口标题栏，选择"Options"
在"Text"选项卡中，将"Locale"设置为"zh_CN"，"Character set"设置为"UTF-8"
重启Git Bash即可解决中文乱码问题

如果还不行，上网查一下
