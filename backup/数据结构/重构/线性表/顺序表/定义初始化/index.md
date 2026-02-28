---
{
  "id": "2d05a2dd-8276-806b-80f2-fb1914d813be",
  "url": "https://www.notion.so/2d05a2dd8276806b80f2fb1914d813be",
  "created_time": "2025-12-21T09:51:00.000Z",
  "last_edited_time": "2025-12-21T10:09:00.000Z"
}
---

#  定义+初始化

## 顺序表的实现——静态分配
  使用静态数组（固定大小的数组）叫静态分配
  ### 定义顺序表结构（结构体）
  ```c
#include <stdio.h>
#include <stdlib.h>
#define MAX_SIZE 100 // 定义顺序表大小
typedef struct {
   int data[MAX_SIZE]; // 用数组存数据
   int length; // 顺序表当前长度
} SeqList;
  ```
  **速记：**
  **用结构体打包一个数组（存数据），一个变量（存顺序表当前长度）**

  ### 初始化顺序表（函数）
  - 需要将length变量（顺序表长度）赋为0
  - 需要将数组中的每个元素赋值为0（内存中有脏数据）（用一个for循环实现）
  ```c
void InitList (SeqList){
  for (int i=0; i<MaxSize; i++)
    L.data=0;
  L.length=0;
}
  ```
  速记：
  这是一个函数，执行：遍历数组并赋0，记录顺序表长度的变量赋0。
  ### 主函数
  ```c
int main(){
  SeqList L; //声明一个顺序表
  InitList(L); //初始化顺序表
  //...后续操作
  return 0;
}
  ```
