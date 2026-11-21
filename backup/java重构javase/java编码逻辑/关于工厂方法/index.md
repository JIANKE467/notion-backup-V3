---
{
  "id": "4195a2dd-8276-80d4-aa7e-eba34a44b72b",
  "url": "https://app.notion.com/p/4195a2dd827680d4aa7eeba34a44b72b",
  "created_time": "2026-11-15T07:43:00.000Z",
  "last_edited_time": "2026-11-15T07:59:00.000Z"
}
---

#  关于工厂方法

工厂方法：工厂方法就是**把对象的创建过程封装起来，让调用者不需要直接 ****`new`**** 具体的类，而是通过一个“工厂”来获取对象（****简单说：将构造方法设为私有，不使用new来获取对象，而是使用类内定义的方法，也就是工厂方法来获取对象****）**
# 步骤：
1. 构造方法设为私有
1. 定义一个方法，将该方法返回值类型设为当前类
1. 在该方法的返回值处new当前类
# Q&A
Q：那这不是有点脱裤子放屁，最后还是调用构造方法，为什么不直接把构造设置成public直接new？
A：从代码的调用路径上看确实是脱裤子放屁，但工厂方法真正解决的是防止破坏性改动的问题，就像下面这个例子：
```java
// 第一版：确实脱裤子放屁
public static Foo of(String name) {
    return new Foo(name);
}
```
```java
// 半年后想加校验？方法体改了，调用方无感
public static Foo of(String name) {
    if (name.isBlank()) throw new IllegalArgumentException();
    return new Foo(name);
}
```
Q：那我直接改构造方法不就完了？照样无感
A：确实，但构造器有诸多限制（如不能根据不同分支返回不同对象等），不过多数情况下使用工厂方法纯属过度设计，直接正常构造也没问题
