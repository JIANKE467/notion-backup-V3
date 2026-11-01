---
{
  "id": "3d45a2dd-8276-80e3-af95-e17afef29548",
  "url": "https://app.notion.com/p/3d45a2dd827680e3af95e17afef29548",
  "created_time": "2026-09-07T08:16:00.000Z",
  "last_edited_time": "2026-09-07T08:58:00.000Z"
}
---

#  可变长参数

可变长参数是：一个方法可以接数量不固定个参数
# 语法
在参数类型后面加 `...`
```java
void test(数据类型... 变量名) {
    }
//这里void，test仅做演示，不是一定是void，test
```
这样，调用时可以这样↓
```java
test(1, 2, 3, 4, 5);
```
# 注意
可变长参数本质上是一个数组
另外,
主方法中 String[] args代表：这里接收数量不固定的字符串参数（命令行参数）
```java
public static void main(String[] args) { }
```
当然，也能写成这样
```java
public static void main(String... args) { }
```
