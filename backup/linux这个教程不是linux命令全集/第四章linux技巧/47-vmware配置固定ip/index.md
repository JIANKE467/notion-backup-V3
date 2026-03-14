---
{
  "id": "3155a2dd-8276-81ba-9960-d19547d74e2b",
  "url": "https://www.notion.so/4-7-VMware-IP-3155a2dd827681ba9960d19547d74e2b",
  "created_time": "2026-02-28T12:47:00.000Z",
  "last_edited_time": "2026-02-28T12:47:00.000Z"
}
---

#  4.7 VMware配置固定IP

### 为什么需要配置固定IP？
虚拟机内的IP地址，是虚拟机的DHCP服务分配的
DHCP：动态IP分配，重启会重新分配
连接到虚拟机IP地址老变会很麻烦
### 步骤
1. VMware→编辑→虚拟网络编辑器→VMnet8→记住下面的子网IP和子网掩码→nat设置→记住网关IP
1. 在Linux中编辑文件 `/etc/sysconfig/network-scripts/ifcfg-ens33 `
1. 修改以下条目
BOOTPROTO=”dhcp”
将dhcp改为static

1. 新增以下条目
IPADDR="[192.168.xxx.xxx](http://192.168.xxx.xxx/)"（本机IP）（根据子网IP范围设置）
NETMASK="255.255.255.0"（子网掩码）
GATEWAY="[192.168.xxx](http://192.168.xxx/).2"（网关IP）
DNS1="[192.168.xxx](http://192.168.xxx/).2"（DNS服务器，可设置为网关IP）

1. 重启网卡服务
命令：
`systemctl restart network`
或：`ifdown ens33 && ifup ens33`（针对具体网卡）
