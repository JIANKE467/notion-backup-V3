---
{
  "id": "4085a2dd-8276-80c0-92a7-ff44fbc21f08",
  "url": "https://app.notion.com/p/4085a2dd827680c092a7ff44fbc21f08",
  "created_time": "2026-10-29T02:06:00.000Z",
  "last_edited_time": "2026-10-29T03:02:00.000Z"
}
---

#  修改类属性

可以通过反射访问一个类中定义的成员字段也可以修改一个类的对象中的成员字段值
整体看就几个步骤：
1. 获取class对象[获取class对象](https://app.notion.com/p/4055a2dd82768017a32be1c6b6b0dd72) 
1. 调用相关方法获取字段[获取成员字段的方法](https://app.notion.com/p/4075a2dd827680f08728cb60e4e017a7#4075a2dd827680c2b491dfa4f9d08e08) 
1. 调用set方法对成员字段进行修改
# set()方法
  注意⚠️：set()方法与getter和setter没有任何关系，前者是反射的API，后者是用于封装私有字段的方法
  ### 方法签名
  `set()` 是 `java.lang.reflect.Field` 类中定义的方法，属于 `Field` 继承自 `AccessibleObject` 的字段操作 API：
  ```java
public void set(Object obj, Object value)
        throws IllegalArgumentException, IllegalAccessException
  ```
  `Field` 还提供了一组针对基本类型的重载方法：
  ```java
void setInt(Object obj, int value)      // int
void setLong(Object obj, long value)    // long
void setDouble(Object obj, double value) // double
void setBoolean(Object obj, boolean value) // boolean
void setFloat(Object obj, float value)  // float
void setShort(Object obj, short value)  // short
void setByte(Object obj, byte value)    // byte
void setChar(Object obj, char value)    // char
  ```
  ### 参数说明
  | **参数** | **类型** | **含义** |
  | --- | --- | --- |
  | **obj** | `Object` | 目标**实例对象**。静态字段传 `null`；非静态字段必须传该 Field 声明类的实例 |
  | **value** | `Object` | 要设置的新值。类型必须与字段类型**兼容**，否则抛异常 |
  ### 返回值
  没有返回值
  ### 注意
  - `set()` 会做**宽松类型匹配（Widening + 装箱）**
  - 调用`setAccessible(true)`即可修改private私有字段和final修饰符的常量
  ### 例子
  ```java
public class User {
    public String name = "张三";
    public static int count = 0;
}

//获取指定字段的Field对象
Field nameField = User.class.getField("name");
//获取指定字段的Field对象
Field countField = User.class.getField("count");

// 1. 非静态字段：必须传实例
User user = new User();
nameField.set(user, "李四");     // ✅

// 2. 静态字段：传 null（推荐）
countField.set(null, 100);       // ✅

// 3. 静态字段：传任意实例也可以（会自动忽略 obj）
countField.set(user, 200);       // ✅ 也能成功，obj 被忽略

// 4. 非静态字段传 null —— 报错
nameField.set(null, "王五");     // ❌ NullPointerException

// 5. 传不相关的类型实例 —— 报错
Cat cat = new Cat();
nameField.set(cat, "赵六");      // ❌ IllegalArgumentException

  ```
# 注意
还是那句话，反射可以绕过Java原本的权限限制，甚至修改常量，开发者应该慎重使用越权能力
