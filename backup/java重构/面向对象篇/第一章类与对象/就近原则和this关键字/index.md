---
{
  "id": "3ad5a2dd-8276-805b-bb99-c4bfe2e8fea4",
  "url": "https://app.notion.com/p/this-3ad5a2dd8276805bbb99c4bfe2e8fea4",
  "created_time": "2026-07-30T09:06:00.000Z",
  "last_edited_time": "2026-07-30T09:12:00.000Z"
}
---

#  就近原则和this关键字

# 就近原则
与c语言相同，当有同名变量时，优先使用最近的那个
Q：为什么能定义同名变量？
A：不能在同一作用域定义同名变量，但作用域不同是可以的
举个例子：
```java
int a；
void ssbn（）{
	int a；
	a=1；
	System.out.println(a);
}
```
↑打印a变量时读取离得最近的，如果局部变量没有定义，则使用稍远的那个
# this关键字
对于局部变量和全局变量同名的情况，this关键字可以指定使用当前对象下的变量，而不是就近原则
语法
```java
this.变量名
```
例
```java
int a；
void ssbn（）{
int a；
a=1；
System.out.println(this.a);
}
```
