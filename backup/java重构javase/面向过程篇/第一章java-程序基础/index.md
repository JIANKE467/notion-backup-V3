---
{
  "id": "3a25a2dd-8276-8022-b536-ee4ef2372ecf",
  "url": "https://app.notion.com/p/Java-3a25a2dd82768022b536ee4ef2372ecf",
  "created_time": "2026-07-19T07:03:00.000Z",
  "last_edited_time": "2026-07-21T12:56:00.000Z"
}
---

#   第一章：Java 程序基础

[程序代码基本结构](程序代码基本结构/index.md)
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
[ 注释](注释/index.md)
  单行注释
  ```java
// 注释内容
  ```
  多行注释
  ```java
/* 注释内容 */
  ```
  文档注释
  ```java
/** 
 * 文档注释 1
 * 文档注释 2
 * @since 日期
 * @author 作者
 */
  ```
  markdown 格式注释（Java23）
  ```java
/// markdown 格式注释
  ```
  # 吐槽
  Java真是sb光注释就搞4种，格式还不统一，纯纯过度工程化，语法都臃肿成啥了
[变量和常量](变量和常量/index.md)
  # 变量
   Java 定义变量需要手动指定变量的数据类型
  ```java
数据类型 变量名； 
  ```
  变量名有以下要求：
  - 标识符可由大小写字母、数字、下划线(_)和美元符号($)组成，不能以数字开头
  - 变量不能重复定义，大小写敏感
  - 不能有空格、@、#、+、-、/ 等符号
  - 应见名知意
  - 不能与关键字重名
  PS：Java语法允许使用中文变量名，但不推荐（兼容性极差）
  ## 变量赋值/定义
  可以初始化赋值
  ```java
int a=1；
  ```
  可以先定义后赋值
  ```java
int a；
a=1；
  ```
  也可以一次定义多个变量（逗号隔开）
  ```java
int a，b；
  ```
  # 常量
  Java 的常量是基于变量定义的
  在变量前加上 final 修饰符，使变量不可修改
  ```java
final int a；
  ```
  常量赋值后不可修改（未初始化的变量可以赋值一次）
