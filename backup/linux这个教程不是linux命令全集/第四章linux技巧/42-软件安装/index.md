---
{
  "id": "3155a2dd-8276-811a-bd89-c05d3805b5de",
  "url": "https://www.notion.so/4-2-3155a2dd8276811abd89c05d3805b5de",
  "created_time": "2026-02-28T12:47:00.000Z",
  "last_edited_time": "2026-03-14T09:58:00.000Z"
}
---

#  4.2 软件安装

Linux系统支持下载安装包安装，和“软件商店”yum命令安装 两种方式
### yum命令（cent OS）
yum是一个RPM包管理器，可以自动化安装配置Linux软件，可自动寻找依赖
语法：
```shell
yum [-y] [install | remove | update | search | localinstall] 软件包名或路径 
```
- -y：自动确认
- install：安装
- remove：卸载
- update：升级
- search：搜索
- localinstall：从本地安装

**注意：**
**yum命令需要root权限**
**软件可以只写软件包名（最新版），也可以写：**`软件名-版本号-发行号`**（指定版本安装）**
### apt命令（Ubuntu）
apt是Ubuntu的包管理器
语法：
命令格式一样，只是命令不同
```shell
apt [-y] [install | remove | search] 软件名
```
# 注意⚠️
### 原理
yum相当于一个安装器，它默认从系统自带的应用商店下载安装，但也可以给它添加第三方应用商店，这样它就能从第三方下载安装了
### 配置第三方仓库
Q：为什么要用第三方仓库？
A：因为官方软件仓库更新太慢，而且某些地区连接不上
Q：推荐什么方法？
A：能联网最好联网，不然手动安装很麻烦，实在不能联网在内网找一个可以联网的机器建一个软件仓库，不要尝试手动安装（依赖太多，版本还得对上）

**方法1:**
有些第三方软件仓库会repo文件或rpm包，直接下载并安装这个包就会自动配置好（自动配置yun源）

**方法2:**
1. 找到yum仓库配置文件，路径如下
```plain text
/etc/yum.repos.d/
```
每个仓库对应一个.repo文件

1. 新建一个.repo文件，推荐文件名小写，见文知义
1. 编辑这个.repo文件，按以下格式
```shell
[repoid]          # 仓库唯一ID
name=仓库名称      #仓库显示名称
baseurl=仓库URL   # 仓库地址
enabled=1         # 是否启用仓库
gpgcheck=1    # 是否验证RPM包签名，保证安全
gpgkey=仓库公钥URL  # 仓库公钥URL
priority=10       # 仓库优先级，值越小越优先
protect=1         # 启用保护，防止被覆盖
metadata_expire=6h # 元数据过期时间，控制缓存更新频率
failovermethod=roundrobin # 多镜像时切换策略
```
Q：为什么腾讯云/阿里云镜像都建议直接替换or修改源repo文件
A：腾讯/阿里害怕你新建配置优先级低于系统自带配置优先级（在repo文件里控制），导致配置不生效，新建配置完全可以，只是要多看一眼优先级
