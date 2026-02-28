---
{
  "id": "3005a2dd-8276-810f-b077-c64f0fec9026",
  "url": "https://www.notion.so/3005a2dd8276810fb077c64f0fec9026",
  "created_time": "2026-02-07T09:52:00.000Z",
  "last_edited_time": "2026-02-07T09:52:00.000Z"
}
---

#  数据类型之复数与虚数

复数需要包含<complex.h>头文件
该文件定义了三种复数精度：
double complex（双精度复数）
float complex（单精度复数）
long double complex（长双精度复数）
↑这三个都属于数据类型↑
### 声明
```c
float complex 变量名=值；
```
### 复数值表示
2+3.0*i 就是 2+3i
### 复数运算（需额外声明）
```c
float complex a=b+c；
//其中abc均为复数
```
### 单独取实部/虚部
```c
float
```
