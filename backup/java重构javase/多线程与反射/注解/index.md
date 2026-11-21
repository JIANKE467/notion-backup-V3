---
{
  "id": "40a5a2dd-8276-8040-8a27-d0137631a68c",
  "url": "https://app.notion.com/p/40a5a2dd827680408a27d0137631a68c",
  "created_time": "2026-10-31T07:38:00.000Z",
  "last_edited_time": "2026-10-31T09:30:00.000Z"
}
---

#  注解

开始前明确几个点：
- 注解是Java 5 引入的一种元数据机制，用于给代码添加补充信息。注解本身不直接影响代码逻辑，但可以被编译器、开发工具或运行时框架读取并处理。
- 注解是否会在运行时去掉取决于**`@Retention`**** **的设置
- **注解本身不执行任何代码**它是给编译器/框架看的用于检查或相应处理
[预设注解](预设注解/index.md)
  JDK预设了以下注解，作用于代码：
  - [@Override](https://www.itbaima.cn/zh-CN/document/qrd0xfttsz32gpqg?segment=4)检查（仅仅是检查，不保留到运行时）该方法是否是重写方法。如果发现其父类，或者是引用的接口中并没有该方法时，会报编译错误。
  - [@Deprecated](https://www.itbaima.cn/zh-CN/document/qrd0xfttsz32gpqg?segment=4)标记过时方法。如果使用该方法，会报编译警告。
  - [@SuppressWarnings](https://www.itbaima.cn/zh-CN/document/qrd0xfttsz32gpqg?segment=4)指示编译器去忽略注解中声明的警告（仅仅编译器阶段，不保留到运行时）
  - [@FunctionalInterface](https://www.itbaima.cn/zh-CN/document/qrd0xfttsz32gpqg?segment=4)Java 8 开始支持，标识一个匿名函数或函数式接口。
  - [@SafeVarargs](https://www.itbaima.cn/zh-CN/document/qrd0xfttsz32gpqg?segment=4)Java 7 开始支持，忽略任何使用参数为泛型变量的方法或构造函数调用产生的警告。
[自定义注解](自定义注解/index.md)
  Java支持自定义注解
  注解本质上是特殊的类
  # 注解定义
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
    String name();                // 无默认值 → 使用时必须赋值
    
    int age() default 18;     
    // 有默认值 → 使用时可省略
    
    String[] tags() default {}; // 数组默认空
}
  ```
  # 注解调用
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
[元注解](元注解/index.md)
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
[反射获取注解](反射获取注解/index.md)
  # 注意
  注解需要指定**保留策略（保留到运行时）**才能在运行时被反射获取，否则注解早就被编译器删除了，运行时根本看不到
  `@Retention(RetentionPolicy.值)`
  > 注解定义时@Retention元注解的RetentionPolicy的值需要设置为RUNTIME
  # 获取步骤
  分不同情况
  ### 如果注解贴在类上（类前面）
  1. 获取类的class对象
  1. 调用class对象的getAnnotation方法获取注解对象（传入参数为：注解的类型.class）
  1. getAnnotation方法返回该注解的一个**实例对象，**调用该对象的方法来查看注解成员的值
  ```java
Class<?> clazz = User.class;

// 获取指定注解
Table table = clazz.getAnnotation(Table.class);
if (table != null) {
    System.out.println(table.name());  // 输出: user
}


//其他方法见下面👇（正文部分就不详细介绍了）
// 判断是否存在某注解
boolean hasTable = clazz.isAnnotationPresent(Table.class);

// 获取所有注解（仅本类声明的）
Annotation[] declared = clazz.getDeclaredAnnotations();

// 获取所有注解（含继承的，仅对类有效）
Annotation[] all = clazz.getAnnotations();

  ```
  ### 如果注解贴在字段上
  1. 获取类的class对象
  1. 获取指定class对象中的指定成员（反射获取类的成员字段）[获取成员字段的方法](https://app.notion.com/p/4075a2dd827680f08728cb60e4e017a7#4075a2dd827680c2b491dfa4f9d08e08) 
  1. 调用getAnnotation方法获取注解对象（传入参数为：注解的类型.class）
  1. getAnnotation方法返回该注解的一个**实例对象，**调用该对象的方法来查看注解成员的值
  ### **获取构造器、参数上的注解**
  这个省略，用到了再现查
