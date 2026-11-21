---
{
  "id": "4075a2dd-8276-80ca-a307-e311fe5a0667",
  "url": "https://app.notion.com/p/4075a2dd827680caa307e311fe5a0667",
  "created_time": "2026-10-28T09:12:00.000Z",
  "last_edited_time": "2026-10-29T02:06:00.000Z"
}
---

#  反射调用方法

可以通过反射调用实例的方法
# invoke()方法
反射依靠使用invoke()方法来调用实例中的方法
### 作用
**在运行时以动态方式调用该方法对象所代表的底层方法**，等价于编译期写死的 `对象.方法名(参数)` 调用，但方法名和参数都是运行时才确定的。
```java
// 直接调用
user.sayHello("hi");

// 反射调用 —— 效果完全一致
method.invoke(user, "hi");
```
### 传入参数
先看方法签名：
```java
public Object invoke(Object obj, Object... args)
        throws IllegalAccessException, IllegalArgumentException, InvocationTargetException
```
参数列表第一个参数：
- 要调用方法为实例方法时，传入该类的实例对象
- 要调用方法为静态方法时，传 `null`
- 要调用方法为私有方法时，传入该类的实例对象（需要事先调用setAccessible(true)以解除访问限制）
参数列表后面的参数：为要传给底层方法的实参列表
### 返回值
原方法类型不同返回值不同：
| **底层方法返回类型** | **invoke 返回** | **处理方式** |
| --- | --- | --- |
| `void` | `null` | 无需处理 |
| `int/long/double...` | `Integer/Long/Double...` | 强转对应包装类 |
| `String/Object...` | 原对象 | 直接强转 |
| `boolean` | `Boolean` | `(Boolean) result` |
| `null` 引用 | `null` | 判空 |
### 注意
- 参数一 ：必须是**声明该方法的类（或其子类）的实例**，否则抛出异常：*`IllegalArgumentException`*
- 后面的参数：如果是无参调用那就**不传或传空数组**
- 后面的参数：如果需要传nul需要强制类型转换成Object类，否则抛异常*`IllegalArgumentException`*
- 后面的参数：理论上只支持Object类型，不支持基本数据类型，但实际上基本数据类型会自动装箱成对应包装类，所以可以传
- invoke方法默认不能访问私有方法，强行访问需要使用`getDeclaredMethod`**+**`setAccessible(true)`详见：[3. getDeclaredMethod(String name, Class<?>... paramTypes)](https://app.notion.com/p/4075a2dd827680f08728cb60e4e017a7#4075a2dd827680b79bfdcb287108e988) 
### 可能抛的异常
```java
try {
    method.invoke(user, arg);
} catch (IllegalAccessException e) {
    // ① 访问权限不足：私有/受保护方法未 setAccessible(true)
} catch (IllegalArgumentException e) {
    // ② 参数问题：实参数量不对、类型不兼容、obj 类型不匹配
} catch (InvocationTargetException e) {
    // ③ 方法内部抛出的异常被“包装”后抛出
    Throwable 真实异常 = e.getCause(); // 必须用 getCause() 取出
    真实异常.printStackTrace();
}

```

# 示例：调用public方法
1. 先通过class获取类的对象
1. 再获取方法
1. 最后调用方法
获取对象和获取方法还是前面讲的那几板斧↓
[通过Class对象创建类的对象](https://app.notion.com/p/4075a2dd827680d7af7ae239a8e92d2f)
 [获取成员方法的方法](https://app.notion.com/p/4075a2dd827680f08728cb60e4e017a7#4075a2dd82768085bc70f0c20d3add54) 
```java
import java.lang.reflect.Method;

public class ReflectionDemo {
    public static void main(String[] args) throws Exception {
        // 步骤1：获取 Class 对象
        Class<?> clazz = Class.forName("User"); // 或 User.class / new User().getClass()

        // 步骤2：通过class对象创建实例
        Object user = clazz.getDeclaredConstructor().newInstance();

        // 步骤3：获取 Method 对象
        // getMethod()用于获取实例的成员方法
        Method method = clazz.getMethod("sayHello", String.class);

        // 步骤4：调用invoke方法以调用方法
        // invoke(对象实例, 实际参数...)
        method.invoke(user, "你好，反射！");
    }
}

```
