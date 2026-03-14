---
{
  "id": "3155a2dd-8276-81a1-8832-eb03b332ba60",
  "url": "https://www.notion.so/4-6-IP-3155a2dd827681a18832eb03b332ba60",
  "created_time": "2026-02-28T12:47:00.000Z",
  "last_edited_time": "2026-02-28T12:47:00.000Z"
}
---

#  4.6 IP地址/主机名/域名解析

# IP
IP有ipv4和ipv6两个版本，下面以IPV4为例
ipv4的格式：xxx.xxx.xxx.xxx
有4段，每段都是从0~255的数字
### 特殊IP
127.0.0.1：表示本机
0.0.0.0：
- 可以指代本机
- 可以在端口绑定中用来确定绑定关系
- 在一些IP地址限制中表示所有IP的意思。如放行规则设置为0.0.0.0表示允许任意IP访问
# ifconfig命令（查看本机ip）
**⚠️注意⚠️**
**Linux没有ipconfig命令，那是Windows命令！！！**
```shell
ifconfig
```
PS：
1. 如果没有ifconfig命令，需要安装net-tools
1. centOS的ens33是主网卡，lo是本地环回网卡
# 主机名（域名）（hostname命令）
### 查询主机名（hostname）
```shell
hostname
```
### 修改主机名（hostnamectl）（root权限）
```shell
hostnamectl set-hostname 名称
```
# 域名解析
将域名解析到对应的IP地址
### 流程
1. 输入域名
1. 查询本地host
1. 如果本地host中找不到，在DNS服务器中查询
1. 连接到网站
### 本地host路径
win：`C:\Windows\System32\drivers\etc\hosts`
Linux：`/etc/hosts`
