---
{
  "id": "4055a2dd-8276-8017-a32b-e1c6b6b0dd72",
  "url": "https://app.notion.com/p/class-4055a2dd82768017a32be1c6b6b0dd72",
  "created_time": "2026-10-26T10:17:00.000Z",
  "last_edited_time": "2026-10-28T07:04:00.000Z"
}
---

#  获取class对象

上节我们了解到，Class类的对象不能由开发者手动创建（不能new，只能由JVM自动创建），但我们可以获取JVM已经创建的class对象
# 获取class对象的三种方法
### `类名.class` 来获取
```java
Class<String> clazz = String.class;
Class<Integer> intClass = int.class;  // 基本类型也可以
```
有没有发现这种写法很怪，怪就对了，因为这根本就不是对象调用（调用对象没有这种`类名.对象`的写法），这就是个语法糖（而且class对象也不隶属于用户写的类，它隶属于Class类）
注意：
- 不会触发类加载，编译期确定

### `对象.getClass()` 方法获取
getClass()方法用于获取该对象对应类的class对象
```java
String str = "hello";
Class<?> clazz = str.getClass();
```
传入参数：空参调用
注意：由于运行时才会创建对象，因此该方法需要在对象创建后使用
### `Class.forName()` 方法获取
使用Class类的forName方法来获取对应路径类的class对象
传入参数：相应类路径的字符串
```java
Class<?> clazz = Class.forName("java.lang.String");
```
注意：会触发类的静态初始化
### 通过**ClassLoader 加载**
通过ClassLoader类的getSystemClassLoader()方法先获取系统类加载器，然后再调用`loadClass()` 方法获取class对象
```java
Class<?> clazz = ClassLoader.getSystemClassLoader()
        .loadClass("java.lang.String");
```
getSystemClassLoader()方法空参调用
`loadClass()` 方法传入相应类路径的字符串
注意：不会触发类静态初始化
# 注意⚠️
- 基本数据类型虽然不是类，但也有相应的class对象
- Class类是泛型类，需要在使用的时候明确泛型类型
