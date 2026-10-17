---
{
  "id": "3ba5a2dd-8276-80ba-ab21-f2a627692a81",
  "url": "https://app.notion.com/p/Java16-3ba5a2dd827680baab21f2a627692a81",
  "created_time": "2026-08-12T13:10:00.000Z",
  "last_edited_time": "2026-08-12T14:21:00.000Z"
}
---

#  （Java16）记录类型

Java 14 （预览版），Java16（正式版）中推出了一种新的类：记录类型
它是用来存储不变的数据的类（它是普通类+final写法的简写）
# 语法
使用`record`声明
```java
public record 记录类型名() {   //记录类型的写法与普通类不太一样，类名后面需要带一个括号
}
```
- 记录类型内可以自由编写方法（部分特殊方法除外，会自动生成）
- 记录类型不能被继承，但可以实现接口
- 记录类型内不可以定义成员变量，只能在括号内定义
- 可以在括号中直接定义成员变量（该成员变量初始化后将无法被修改）
```java
public record TestDat(int a, String b) {  
}
```
- 记录类型会自动生成与成员变量同名的getter方法（自动生成的getter方法，命名方式略有不同，参见[getter有两种命名方式：手写➡️get + 首字母大写的成员变量名自动生成➡️首字母大写的成员变量名（但其实从语法上讲 命什么名都行）](https://app.notion.com/p/3b15a2dd82768045b4e0d71b634b95d7#3ba5a2dd827680f7b345d644a168d96a) ）
```java
TestData test = new TestData(1,"测试");
test.a(); //这个方法是自动生成的
test.b(); //这个方法是自动生成的
```
- 记录类型会自动生成 toString() 方法（并且自动重写成了：打印对象的所有成员变量及其值）[toString()方法](https://app.notion.com/p/3b45a2dd827680fea73cda9dfdc888a1#3b85a2dd82768066b9aad0b03197c98a) 
- 记录类型会自动生成equals方法（并自动重写成了：比较两个对象的值 而非引用）[equals()方法](https://app.notion.com/p/3b45a2dd827680fea73cda9dfdc888a1#3b85a2dd82768036b7fbf1e72cb33944) 
- 如果自动生成的方法不能满足需求，也可以直接在记录类型中重写对应的方法进行覆盖
- 由于记录类型是不可修改的，所以记录类型内不能编写setter方法

# Q&A
Q：记录类型本质是什么？
A：本质上在编译之后也是一个普通的类，不过是final且继承自`java.lang.Record`抽象类的，它会在编译时，会自动编译出 `public get` `hashcode` 、`equals`、`toString` 等方法。
