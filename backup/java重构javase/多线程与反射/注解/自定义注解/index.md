---
{
  "id": "40a5a2dd-8276-8048-b981-c0905cbc3db6",
  "url": "https://app.notion.com/p/40a5a2dd82768048b981c0905cbc3db6",
  "created_time": "2026-10-31T08:22:00.000Z",
  "last_edited_time": "2026-10-31T09:29:00.000Z"
}
---

#  自定义注解

Java支持自定义注解
注解本质上是特殊的类
## **1. 基本语法**
```java
public @interface MyAnnotation {
    // 注解体
}
```
- 关键字：**`@interface`**（不是 `interface`）
- 定义时，注解体里**什么都没有的**无元素注解叫**标记注解**，如 `@Override`
- 定义后即可使用：`@MyAnnotation`
## **2. 注解元素（属性）**
注解也是个类，但注解的设计意图是“便签”而不是”逻辑”，因此其元素只能用来存储信息，不能执行操作
**注解的属性也叫做成员变量，注解只有成员变量，没有方法。注解的成员变量在注解的定义中以“无形参的方法”形式来声明，其方法名定义了该成员变量的名字，其返回值定义了该成员变量的类型（这段话是标准解释，下面使用“方法”口径是当前文档的遗留问题，以本句为准）**
### **2.1 基本写法**
和类定义类似，使用@interface关键字，内部定义方法及其类型（方法用于存放注解内容）
```java
public @interface MyAnnotation {
    String name();              
    // 无默认值 → 使用时必须赋值
    int age() default 18;       
    // 有默认值 → 使用时可省略
    String[] tags() default {}; // 数组默认空
}
```
```java
@MyAnnotation(name = "张三")
@MyAnnotation(name = "李四", age = 30)
```
> ⚠️ 元素**长得像方法但不是方法**，只是“贴注解时要提供什么信息”的声明。
> 定义时没设置默认值，调用时必须赋值（在注解后面的括号里面使用`方法名=值`的方式赋值即可）（调用时不能省略方法名）
> 注解定义中不允许定义变量，只能定义方法
### **2.2 特殊元素名 ****`value`**
方法名value在注解中有特权，当注解定义中只有名为value的方法时，注解调用时可以不写方法名（其他名称的方法没这特权，必须写方法名）
```java
public @interface Note {
    String value();
}
```
```java
@Note("说明文字")   // ✅ 等价于 @Note(value = "说明文字")
```
**但是**，只要注解定义中元素总数 ≥ 2，就不能省略value的方法名：
```java
public @interface Note2 {
    String value();
    int count() default 0;
}
@Note2("说明")     
// ❌ 编译错误，必须 @Note2(value = "说明")
```
**设计习惯**：最常用的信息放 `value`。
## **3. 注解定义中元素类型的限制**
### **✅ 只允许使用以下类型：**
| **类型** |
| --- |
| 8 种基本类型 |
| `String` |
| `Class` |
| 枚举 |
| 注解 |
| 以上**数组** |
### **❌ 不允许使用以下类型：**
```java
Integer age();        // ❌ 包装类不行
List<String> names(); // ❌ 集合不行
Object obj();         // ❌
```
> 注解值必须在**编译期确定**并写入 class 文件，无法存放需运行时构造的对象。
### **衍生规则**
```java
@MyAnno(x = someVariable)   // ❌ 变量不行
@MyAnno(x = 1 + 2)          // ✅ 常量表达式
@MyAnno(x = Constant.SIZE)  // ✅ static final 常量
```
## **4. 嵌套注解与哨兵值**
### **嵌套注解**
```java
public @interface Retry {
    int times() default 3;
}

public @interface Task {
    String name();
    Retry retry() default @Retry(times = 5);   // 默认值用 @注解(...) 形式
}
```
### **null 的替代方案**
**注解元素的值不能是 ****`null`****，****`default`**** 也不能是 ****`null`**，应该用哨兵值替代“null”
1. **数值型：用 ****`-1`****、****`Integer.MAX_VALUE`**** **替代null
1. **字符串型：用 ****`""`****（空字符串）**替代null
1. **Class 型：用 ****`void.class`**替代null
1. **数组型：用空数组 ****`{}`**替代null
```java
String name() default "";   // 空串 = 未指定
int length() default -1;    // -1 = 未指定
```
## **5. 编译器背后做的事**
```java
@interface  →  编译成隐式继承 Annotation 的接口
使用时的值  →  存进 class 文件
反射 anno.name()  →  JVM 动态代理从 class 文件数据取值返回
```
> 解释了为什么读注解像调方法——**本来就是方法调用**。

# 更多信息见下一节
