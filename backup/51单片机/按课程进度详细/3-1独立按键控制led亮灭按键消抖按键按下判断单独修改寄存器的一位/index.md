---
{
  "id": "26d5a2dd-8276-8075-90e8-e38bedd7a8b4",
  "url": "https://www.notion.so/3-1-led-26d5a2dd8276807590e8e38bedd7a8b4",
  "created_time": "2025-09-13T06:50:00.000Z",
  "last_edited_time": "2025-09-13T07:58:00.000Z"
}
---

#  3-1独立按键控制led亮灭（按键消抖，按键按下判断，单独修改寄存器的一位）

# 实验1：按下按键灯状态切换
代码
```c
#include <REGX52.H>
#include <INTRINS.H>
void Delay1ms(int xms)		//@11.0592MHz 改造的延时函数
{
	unsigned char i, j;
	for( ;xms>0;xms--)
		{
			

			_nop_();
			i = 2;
			j = 199;
			do
			{
				while (--j);
			} while (--i);
		}
}
void main()
{
while(1)
{		
			if(P3_1==0)
			{
		
			Delay1ms(20);
			while(P3_1==0);
			Delay1ms(20);
			P2=~P2;
			}
}				
}

```
### 主函数逻辑
初始化寄存器，先用if分支判断是否按下，没有按下则会阻塞运行，按下则进入循环（循环条件是按键按下寄存器的值），不松开则会阻塞运行，松开后给寄存器的值取反
### 按键消抖
用软件延时计算器生成20ms的延时函数，放在按下和抬起的逻辑后面
### 寄存器一位修改
用P1_1修改，由<REGX52.H>定义
