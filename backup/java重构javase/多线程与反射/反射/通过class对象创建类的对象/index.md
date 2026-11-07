---
{
  "id": "4075a2dd-8276-80d7-af7a-e239a8e92d2f",
  "url": "https://app.notion.com/p/Class-4075a2dd827680d7af7ae239a8e92d2f",
  "created_time": "2026-10-28T07:52:00.000Z",
  "last_edited_time": "2026-10-28T09:36:00.000Z"
}
---

#  通过Class对象创建类的对象

# Q&A
Q：什么意思？
A：Class对象既然是类的元数据，那能不能不使用传统的`new 类型`创建对象，而是直接使用class对象创建类的对象（答案当然是可以）
Q：蛋疼吧？不用new创建对象，用class对象创建对象有什么意义？
A：这引入了一个重要特性：动态加载（代码写完不代表写死了，更改一行配置就改变了）（这是引入SpringBoot的一环）
# 方法1**（JDK 8 及以前）**
调用class的**`newInstance()`**** **方法获取对象
```java
//先获取class对象
Class<?> clazz = Class.forName("com.example.User");
//调用class对象的newInstance()方法获取类对象
User user = (User) clazz.newInstance();  
```
- 类必须有无参构造方法
- 构造方法必须是 public 的
- 无参构造器必须存在，否则抛出 `InstantiationException`
这种方式已经过时，不推荐使用
# 方法2**（推荐，JDK 9+）**
省流：先获取构造方法，再创建对象
先调用class的**`getConstructor()`**** **方法获取该class对应类的构造方法，返回一个 `Constructor` 对象
然后再调用`Constructor` 对象的`newInstance()`方法来创建类的对象
```java
//引入这个包
import java.lang.reflect.Constructor;
//获取class对象
Class<?> clazz = Class.forName("com.example.User");

// 获取无参构造方法
Constructor<?> constructor = clazz.getConstructor();
//创建类的对象
User user = (User) constructor.newInstance();

```
注意⚠️：
- Java8以前的获取方法之所以被淘汰是因为只支持无参构造，而`getConstructor()`方法既支持无参构造也支持有参构造
- 如果类没有无参构造，那`getConstructor()`方法必须带参数，`getConstructor()`方法的传入参数为构造方法参数的class对象
```java
Class<?> clazz = Class.forName("com.example.User");

// 获取指定参数类型的构造器
Constructor<?> constructor = clazz.getConstructor(String.class, int.class);

// 传入实际参数创建对象
User user = (User) constructor.newInstance("张三", 25);
```
- 如果构造方法为私有的，getDeclaredConstructor()可以强行访问，但需要调用`setAccessible(true)`这个方法打开强行访问权限
```java
// 获取class对象
Class<?> clazz = Class.forName("com.example.Singleton");
//获取构造方法
Constructor<?> constructor = clazz.getDeclaredConstructor();  
//突破私有访问限制
constructor.setAccessible(true);  
//创建类的对象
Singleton instance = (Singleton) constructor.newInstance();

```
