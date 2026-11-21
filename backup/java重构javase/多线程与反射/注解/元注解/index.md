---
{
  "id": "40a5a2dd-8276-8030-96f4-ccadf6fb2c29",
  "url": "https://app.notion.com/p/40a5a2dd8276803096f4ccadf6fb2c29",
  "created_time": "2026-10-31T08:09:00.000Z",
  "last_edited_time": "2026-10-31T09:26:00.000Z"
}
---

#  元注解

元注解是注解的注解：注解贴在方法/字段/类上，元注解贴在注解定义上，给**注解本身**贴标签
**元注解是写在注解定义前面的**
元注解用于设置自定义注解的属性：
- [@Retention](https://www.itbaima.cn/zh-CN/document/qrd0xfttsz32gpqg?segment=4)标识定义的注解怎么保存，是只在代码中，还是编入class文件中，或者是在运行时可以通过反射访问。
- [@Documented](https://www.itbaima.cn/zh-CN/document/qrd0xfttsz32gpqg?segment=4)标记定义的注解是否包含在用户文档中。
- [@Target](https://www.itbaima.cn/zh-CN/document/qrd0xfttsz32gpqg?segment=4)标记定义的注解应该是哪种 Java 成员。
- [@Inherited](https://www.itbaima.cn/zh-CN/document/qrd0xfttsz32gpqg?segment=4)标记这个注解是继承于哪个注解类(默认 注解并没有继承于任何子类)
- [@Repeatable](https://www.itbaima.cn/zh-CN/document/qrd0xfttsz32gpqg?segment=4)Java 8 开始支持，标识某注解可以在同一个声明上使用多次。
# 下面逐个介绍
### **1. ****`@Retention`**** —— 注解的“寿命”**
```java
//下面代码位为注解定义
@Retention(RetentionPolicy.RUNTIME)   
// 活到运行时，反射能读到
public @interface MyAnno { }
```
三种寿命：
```java
//下面代码位于注解定义中
@Retention(RetentionPolicy.SOURCE)   
// 死于编译：编译完就丢弃（如 @Override）
@Retention(RetentionPolicy.CLASS)    
// 死于加载：进了class文件，运行时丢弃（默认值！）
@Retention(RetentionPolicy.RUNTIME)  
// 活到最后：运行时反射可读（如 @Autowired）
```
> ⚠️ 不写 `@Retention` 默认就是 `CLASS`，反射读不到。**自定义注解 90% 的情况都要显式写 RUNTIME。**
### **2. ****`@Target`**** —— 注解的“岗位”**
规定这个注解只能贴在哪些位置：
```java
//下面代码为注解定义
@Target(ElementType.METHOD)                    // 只能贴方法
public @interface OnlyMethod { }



@Target(ElementType.TYPE)                      // 只能贴类/接口/枚举
public @interface OnlyClass { }



@Target(ElementType.FIELD)                     // 只能贴字段
public @interface OnlyField { }



@Target({ElementType.METHOD, ElementType.FIELD})  // 可以贴多个位置
public @interface MethodOrField { }
```
贴错了位置直接编译报错：
```java
//下面代码位于注解使用处
@OnlyMethod          
// ❌ 编译错误：Not applicable to type
public class Demo { }
```
常用取值一览：
| **取值** | **可贴位置** |
| --- | --- |
| `TYPE` | 类、接口、枚举、注解 |
| `METHOD` | 方法 |
| `FIELD` | 字段（包括枚举常量） |
| `PARAMETER` | 方法参数 |
| `CONSTRUCTOR` | 构造器 |
| `LOCAL_VARIABLE` | 局部变量 |
| `ANNOTATION_TYPE` | 注解类型（**元注解自己就用这个**） |
| `PACKAGE` | 包（较少用） |
### **3. ****`@Documented`**** —— 跟随文档**
在注解定义时使用该元注解，如果该注解被使用，在 Javadoc 工具生成文档时，该注解会出现在文档里。
```java
//下面代码位于注解定义中
@Documented
public @interface MyAnno { }
```

### **4. ****`@Inherited`**** —— 子类继承（只对类有效）**
在定义注解时使用`@Inherited` 元注解，表示如果该注解贴在**父类上可以被子类“继承”**——用反射查子类时，能查到贴在父类上的注解。
```java
@Inherited
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.TYPE)
public @interface ClassMark { }

@ClassMark
public class Parent { }

public class Child extends Parent { }
```
```java
//这里省略了父类
//子类使用
Child.class.isAnnotationPresent(ClassMark.class);   // 加了@Inherited → true
                                                    // 不加 → false
```
**两个坑要记住**：
- 只对**类上的注解**有效，方法、字段上的注解不能被继承
- 接口上的注解，实现类永远读不到（`@Inherited` 也救不了）
### **5. ****`@Repeatable`**** —— 重复贴（Java 8 新增）**
Java 8 之前，同一注解一个位置只能贴一次。想贴多次必须配一个“容器注解”，而Java8+则推出了**`@Repeatable`**将这套流程标准化
```java
// 第 1 步：定义真正的注解，标记可重复
@Repeatable(Roles.class)
@Retention(RetentionPolicy.RUNTIME)
public @interface Role {
    String value();
}

// 第 2 步：定义容器注解（属性必须是注解数组）
@Retention(RetentionPolicy.RUNTIME)
public @interface Roles {
    Role[] value();
}

// 第 3 步：现在可以贴多次了
@Role("admin")
@Role("user")
public class Account { }
```
读取时注意拿到的可能是容器：
```plain text
Role[] roles = Account.class.getAnnotationsByType(Role.class);  // 推荐：直接拿多个 Role
```
