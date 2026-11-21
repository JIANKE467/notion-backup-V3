---
{
  "id": "3b95a2dd-8276-8011-b21d-fd9091762f3c",
  "url": "https://app.notion.com/p/3b95a2dd82768011b21dfd9091762f3c",
  "created_time": "2026-08-11T12:48:00.000Z",
  "last_edited_time": "2026-08-11T14:34:00.000Z"
}
---

#  枚举类

枚举类是一种特殊的类，他提供了多个选项，调用时只能调用选项范围内的
# 应用场景
假如我们要存储一个状态，那可以这样写
```java
public class Student extends Person implements Study {

    private String status;   //状态，要求是跑步、学习、睡觉这三个之中的其中一种

}
```
但这带来一个问题，外部可以传入任意值↓
```java
	Student test = new Student;
	test.status = "666";
```
如果我们想将输入限制到我们规定的几个选项内，就需要用到枚举类
# 语法
枚举类不用class，而是用enum表示
```java
访问修饰符 enum 枚举类名 {   
    枚举对象一, 枚举对象二, 枚举对象三;    //直接写每个枚举项的名字即可，最后面分号可以不打，但是推荐打上
}
```
- 由于枚举类的底层是普通类，所以枚举类中可以定义成员方法/成员变量/构造方法（这里构造方法只能用private修饰）
# 使用
### 定义变量时
定义变量时需要将变量引用给枚举类（创建枚举类型的变量）
```java
public class Student extends Person implements Study {

    private 枚举类名 status;   //这里要将变量引用给枚举类名

}
```
### 调用变量时
使用`枚举类型.枚举对象`调用
```java
Student test= new Student;
test.statius= 枚举类型.枚举对象一;
```
# Q&A
Q：在getter中写if语句也可以限制传入的数据，为什么要这么做？
A：这种方法也可以实现同样的效果，但无法在编译阶段发现错误，使用枚举类则可以
Q：枚举类的实质是什么？
A：通过反编译，我们可以发现，枚举类其实是一个继承了`java.lang.Enumd`的`public final`修饰的类，其中每个枚举对象都是该类的一个`public static final`的成员变量
```java
//这里使用javap命令对class文件进行反编译得到 Compiled from "Status.java"
public final class com.test.Status extends java.lang.Enum<com.test.Status> {
  public static final com.test.Status RUNNING;
  public static final com.test.Status STUDY;
  public static final com.test.Status SLEEP;
  public static com.test.Status[] values();
  public static com.test.Status valueOf(java.lang.String);
  static {};
}
```
