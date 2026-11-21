---
{
  "id": "3865a2dd-8276-803c-865e-d86c4ad4ef19",
  "url": "https://app.notion.com/p/6-2-DNS-3865a2dd8276803c865ed86c4ad4ef19",
  "created_time": "2026-06-21T07:06:00.000Z",
  "last_edited_time": "2026-06-21T07:22:00.000Z"
}
---

#  6.2 DNS概述

网址=域名
### 域名结构
```plain text
www.w3.com
www：三级域
w3：二级域
com：顶级域
```
### DNS作用
保存各域名IP信息，将域名转换为IP
### DNS基本特点
- DNS采用C/S（客户端/服务器）工作方式
- DNS是应用层协议，通常基于UDP（53端口）
- DNS是分布式系统，即使单个计算机出来故障，也不会妨碍整个DNS运行
