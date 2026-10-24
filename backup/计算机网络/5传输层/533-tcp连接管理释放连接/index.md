---
{
  "id": "3855a2dd-8276-80f5-bca2-c287e3dcebcb",
  "url": "https://app.notion.com/p/5-3-3-TCP-3855a2dd827680f5bca2c287e3dcebcb",
  "created_time": "2026-06-20T07:53:00.000Z",
  "last_edited_time": "2026-06-20T08:20:00.000Z"
}
---

#  5.3.3 TCP连接管理（释放连接）

前提：仍把主动发起关闭的一方叫客户端，被动响应的一方叫服务器（双方都可能发起关闭）
# 四次挥手（标记值）
挥手1：客户端→服务器（客户端申请关闭）
FIN=1；ACK=1；SYN=0；seq=xx(客户端当前序号)；ack=服务器当前seq+1（若之前已收数据则为期望的下一个序号）

挥手2：服务器→客户端（服务器确认）
FIN=0；ACK=1；SYN=0；seq=xx(服务器当前序号)；ack=客户端seq+1

挥手3：服务器→客户端（服务器准备好关闭并发起关闭）
FIN=1；ACK=1；SYN=0；seq=xx(服务器当前序号)；ack=客户端seq+1（客户端后续若有数据则相应变化）

挥手4：客户端→服务器（客户端确认关闭）
FIN=0；ACK=1；SYN=0；seq=客户端seq+1（若挥手1只发FIN则+1；若中间还发了数据则累计增加）；ack=服务器seq+1
注意⚠️
- 只有挥手1，3的FIN=1
- 挥手1，3的FIN 即使不携带数据也会消耗一个序号（seq+1）
- 挥手2可以携带数据，挥手4不能携带数据

# 四次挥手（状态转换）
### 客户端
```plain text
已建立连接ESTABLISHED
↓（发送挥手1 FIN）
终止等待1FIN-WAIT-1
↓（收到挥手2 ACK）
终止等待2FIN-WAIT-2
↓（收到挥手3 FIN）
时间等待TIME-WAIT
↓（等待2MSL后）
连接关闭CLOSED
```
### 服务器
```plain text
已建立连接ESTABLISHED
↓（收到挥手1 FIN，发送挥手2 ACK）
关闭等待CLOSE-WAIT
↓（发送挥手3 FIN）
最后确认LAST-ACK
↓（收到挥手4 ACK）
连接关闭CLOSED
```
![](assets/3855a2dd-8276-80be-bb6c-d23dbc6ce41c.jpg)

# TIME-WAIT（为什么要等2MSL）
- **保证挥手4的ACK可靠到达**：若ACK丢失，服务器会重传挥手3（FIN），客户端仍在TIME-WAIT才能再次发送ACK
- **防止旧连接报文干扰新连接**：等待足够时间让网络中属于旧连接的报文都消失（2MSL）
- 经验记忆：TIME-WAIT 在 **主动关闭方** 出现，时间为 **2MSL**
# 释放连接耗时分析
用（RTT：往返时延）计算
通常至少需要：挥手1→挥手2（1RTT） + 挥手3→挥手4（1RTT） + 2MSL（TIME-WAIT）
不用死记
- 客户端收到挥手3后，至少要到计时2SML才能关闭
- 服务器可以连续发出挥手2，3（这算1RTT）
- MSL（最大报文段寿命）是TCP协议规定的固定时间
