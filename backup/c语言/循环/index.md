---
{
  "id": "3005a2dd-8276-81c1-918c-e85d85f861ec",
  "url": "https://www.notion.so/3005a2dd827681c1918ce85d85f861ec",
  "created_time": "2026-02-07T09:52:00.000Z",
  "last_edited_time": "2026-02-07T09:52:00.000Z"
}
---

#  循环

# 循环
# 说在最前面：
在循环中
**零为假非零为真**
其他表示真假的方法：布尔变量
但需引入 stdbool.h 头文件才能使用
布尔变量使用true和false表示对和错（分别对应非0与0）
```c
#include <stdio.h>
#include <stdbool.h> // 引入布尔类型
int main()
{
  bool isHappy = true; // 定义布尔变量并初始化为true
  bool isSad = false;  // 定义布尔变量并初始化为false
  if (isHappy)
   {
     printf("I am happy!\n");
    }
  if (!isSad)
   {
     printf("I am not sad!\n");
    }
return 0;
}
```
## while循环（前置条件循环）
格式：
```c
while(表达式)   //表达式为真，执行循环，直到表达式不为真，退出循环
     循环语句;
```
先判断，后循环
## do while循环（后置条件循环）
‍
```c
do
{循环语句;}
while(判断条件);
```
## for循环（前置入口循环）
格式
```c
for(表达式1；表达式2；表达式3)
```
**表达式1:**
初始化部分，初始化循环变量
**表达式2**:
条件判断部分，判断循环何时终止
**表达式3**:
调整部分，定义循环变量如何变化
例子：
```c
int a=1;
for(a=2;a<10;a++)
   循环语句；
```
<u>**‍注意⚠️：for括号中是分号！分号！分号！不是逗号！！！**</u>
## break语句（停止）
break语句用于终止switch分支和循环
```c
break;
```
‍
## continue语句（跳过）
continue语句用于跳过本次循环后面的代码，直接去判断部分，进行下一次循环的判断
```c
continue;
```
continue与break一般有如下用法：
```c
if(5==i)
  break;
```
或
```c
if(5==i)
  contiue;
```
‍
