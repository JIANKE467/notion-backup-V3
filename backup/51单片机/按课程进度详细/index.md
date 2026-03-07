---
{
  "id": "26d5a2dd-8276-800a-97e6-f09d0b7a2163",
  "url": "https://www.notion.so/26d5a2dd8276800a97e6f09d0b7a2163",
  "created_time": "2025-09-13T04:59:00.000Z",
  "last_edited_time": "2025-09-13T06:50:00.000Z"
}
---

#  按课程进度详细

LED教程部分异常详见[灯闪烁](https://www.notion.so/2355a2dd82768045a1aef8aaee7a9dfb) 
[2-1点亮一个LED（正式第一节）](2-1点亮一个led正式第一节/index.md)
  # 实验1（点亮LED）
  1. 打开keil→project→new uvision project（新建项目文件）→选择MCU型号→project中选择target1→右键source group1→add new….
  1. 代码
  ```c
#include <REGX52.H>
void main ()
{
  p2=0xFE//11111110;
}
  ```
  ### 原理
  查看原理图，看要点亮的LED与那个寄存器相连，修改寄存器内的值以改变LED亮灭状态
  解释：
  <REGX52.H>是定义stc89c52单片机寄存器的头文件
  注意⚠️：
  1. 如果LED是共阳接法，寄存器的值与实际亮灭状态是相反的
  1. 给寄存器赋值要用16进制，不能直接用二进制，否则会被当成10进制处理

  PS：手头的开发板不仅是共阳接法，寄存器标号也标反了😅😅😅
  keil默认不生成hex文件，需要点这个
  ![](assets/26d5a2dd-8276-80fc-91a4-e01c7e929c46.jpg)
  在output中勾选create hex file后点击OK
  # 实验二（让程序持续运行）
  在最外层写一个死循环阻止程序退出
  ```c
#include <REGX52.H>
void main ()
{ 
 while(1)
  {
    p2=0xFE//11111110;
  }
}
  ```
[2-2，2-3LED闪烁，led流水灯（软件延时）](2-22-3led闪烁led流水灯软件延时/index.md)
  # 实验1（软件延时使用）
  代码：
  ```c
#include <REGX52.H>
#include <INTRINS.H>
void Delay1000ms()		//@11.0592MHz
{	unsigned char i, j, k;
	_nop_();
	i = 8;
	j = 1;	
	k = 243;	
	do	
	{		
	do		
	{			
	while (--k);		
	} 
	while (--j);	
	} 
	while (--i);
	}
/*Delay1000ms是软件延时计算器生成的延时1000ms的函数*/

void main()
{	
while(1)	
{
		P2=0x00;
		Delay1000ms();
		P2=0xFF;		
		Delay1000ms();	
		}
}
  ```
  ### 原理
  利用stc烧录程序提供的软件延时计算器实现：亮—等待—灭—等待，的循环
  ### 注意⚠️
  这个程序需要包含INTRINS.H头文件，这个定义了keil编译器的内置函数
  # 实验2（改造软件延时函数）
  代码：
  ```c
#include <REGX52.H>
#include <INTRINS.H>
void Delay1ms(unsigned int x_ms)		//@11.0592MHz
{
	for( ;x_ms>0;x_ms--)
	{
		unsigned char i, j;

		_nop_();
		_nop_();
		_nop_();
		i = 11;
		j = 190;
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
		P2=0x00;
		Delay1ms(50);
		P2=0xFF;
		Delay1ms(100);
	}
}
  ```
  ### 原理
  1. 生成一个 1ms的延时函数
  1. 给延时函数内套一个执行n次的循环（建议用for循环）
  1. 给延时函数定义一个参数n
  1. 调用函数时传入参数n
  ps：这个n就是延时多少ms
  注意⚠️：定义函数参数时使用了unsigned int“无符号整形”，单片机寄存器只有8位，所以只能使用8位的无符号整形

  ### **for循环：**
  ```c
for(表达式1；表达式2；表达式3)
  ```
  **表达式1:**
  初始化部分，初始化循环变量
  **表达式2**:
  条件判断部分，判断循环何时终止
  **表达式3**:
  调整部分，定义循环变量如何变化

  ### led流水灯
  逻辑：
  修改寄存器为第一个灯亮的值—调用延时函数—…..第二个灯亮的值—调用延时函数……..一直循环
[3-1独立按键控制led亮灭（按键消抖，按键按下判断，单独修改寄存器的一位）](3-1独立按键控制led亮灭按键消抖按键按下判断单独修改寄存器的一位/index.md)
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
