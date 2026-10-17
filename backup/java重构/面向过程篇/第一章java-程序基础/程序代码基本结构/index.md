---
{
  "id": "3a25a2dd-8276-80f7-9a13-ecf4ab626a97",
  "url": "https://app.notion.com/p/3a25a2dd827680f79a13ecf4ab626a97",
  "created_time": "2026-07-19T07:03:00.000Z",
  "last_edited_time": "2026-07-28T02:18:00.000Z"
}
---

#  程序代码基本结构

 以下是最基本的 Java代码结构
```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
}
```
其中，这是每个 Java 程序必须有的“主方法”（c语言叫主函数）（程序入口）
**PS：与c不同的是，JAVA一个类只能有一个程序入口，但允许多个类有多个程序入口（此时需要指定要运行的类）**
```java
public static void main(String[] args)
```
- 每句代码间用`；`隔开
- 主方法是固定格式`public static void main(String[] args)`
- Java 不像 Python，它的代码不靠空格和换行分隔
- Java 只要有主方法就能运行，不一定需要创建类和包

常用方法
调试中常使用方法`System.out.println("")`来将结果打印到控制台
# Java25
Java25支持这样简写主方法
```java
void main ()
```
