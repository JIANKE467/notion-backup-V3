---
{
  "id": "4045a2dd-8276-80c8-880f-dcf24242ce85",
  "url": "https://app.notion.com/p/4045a2dd827680c8880fdcf24242ce85",
  "created_time": "2026-10-25T09:25:00.000Z",
  "last_edited_time": "2026-10-28T09:12:00.000Z"
}
---

#  反射

这章不是很重要，主要讲的是JVM的部分工作原理（重点是Class类）
我认为柏码这章顺序有点问题，所以大幅调整了顺序和标题以及内容（几乎全部重编）
[class类/对象](class类对象/index.md)
  说一个新鲜的：为了贯彻一切皆对象的理念，Java的class其实也是一个类，也能创建对象
  # Class类
  Java中Class类定义的是类的模板，其对象存储的是每个类的元数据
  在机器上运行时，开发者每定义一个类，JVM就会创建一个Class类的对象（不一定真的创建，Java采取的是懒加载策略，不使用就不会创建），每个类都对应一个Class类的对象
  以下是Class类的定义↓
  ```java
Class<?> clazz = Dog.class;

clazz.getName();                  // 类名："com.example.Dog"
clazz.getFields();                // 所有 public 字段
clazz.getDeclaredFields();        // 所有字段（含 private）
clazz.getMethods();               // 所有 public 方法
clazz.getConstructors();          // 所有构造器
clazz.getSuperclass();            // 父类是谁
clazz.getInterfaces();            // 实现了哪些接口
clazz.getAnnotations();           // 头上标了哪些注解
clazz.isInterface();              // 是不是接口

  ```
  可以发现Class类中的各种方法都用于存储类的元数据（类的基础信息）
  这就相当于为各个类提供了统一格式的目录，而Class类本身便是这个目录的模板，Class类的对象就是目录本体
  # Class类的对象
  上面基本上已经解释清楚了，Class类的对象隶属于Class类，在运行期间首次使用某个类时由JVM自动创建，每个类只有一个对应的class对象，且后续该类的创建只会参考该class对象，而不会参考原本的类定义
  从硬件角度讲：
  类定义位于硬盘中，首次使用后在内存中创建该类的class对象，后续该类对象的创建只参考内存中的class对象，不会参考硬盘中的类定义（在运行期间将所有类加载进内存后删除源代码，程序仍可运行就能证明这点）
  # 注意
  - 我们常写的类定义中的class和这个没有关系，它仅仅是个关键字（Java的设计没那么妙）
  ```java
//就这东西里面的class
public class Test {
}
  ```
  - Class类的对象不能被开发者手动创建（不能new），只能由JVM自动创建（不过开发者可以通过触发JVM创建class对象来间接创建）
  # 为什么这么设计？
  Java在运行时需要一个知道各类的基础信息，用以分配内存，明确继承关系，进行各种管理… Java选择了和照片exif元数据类似的思路来管理（定义Class类，运行时自动为各类创建Class对象）
[获取class对象](获取class对象/index.md)
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
[Class对象的使用](class对象的使用/index.md)
  我们已经了解了如何获取class对象引用，那么接下来，我们看看class对象中记录了什么信息，有什么方法（研究一下Class类定义）
  # Class类记录的字段
  详细的字段名称这里就不说了，反正一般人谁没事重写Class类的方法啊
  | **类别** | **内容** |
  | --- | --- |
  | 基本信息 | 完整类名、简单类名、修饰符、包信息 |
  | 继承关系 | 父类、实现的接口列表 |
  | 字段信息 | 字段名、类型、修饰符（对应 `Field` 对象） |
  | 方法信息 | 方法名、参数、返回值、异常（对应 `Method` 对象） |
  | 构造器 | 参数列表、修饰符（对应 `Constructor` 对象） |
  | 注解 | 类上标注的注解 |
  | 泛型信息 | 编译时保留的泛型声明 |
  | 其他 | 类加载器引用、类型判断信息（接口/枚举/数组等） |
  # Class类的方法
  ## 获取基本信息
    ```java
getName();          // 完整类名（含包名）
getSimpleName();    // 简单类名
getPackage();       // 所在包
getModifiers();     // 修饰符（int 编码，配合 Modifier 解析）
getSuperclass();    // 父类的 Class
getInterfaces();    // 实现的接口数组
    ```
  ## 获取成员字段的方法
    ### **1. ****`getField(String name)`**
    - **作用**：获取指定名称的**单个字段**
    - **范围**：只能获取 **public** 字段
    - **包含继承**：✅ 能获取本类 + 所有父类的 public 字段
    - **找不到时**：抛 `NoSuchFieldException`
    - 返回值：返回字段值
    - 传参：字段名字符串
    ### **2. ****`getFields()`**
    - **作用**：获取**所有** public 字段（返回 `Field[]`）
    - **范围**：本类 + 所有父类（直至 Object）的 public 字段
    - 传入：空参调用
    - 返回：返回一个 Field 类的对象，它反映此 Class 对象所表示的类或接口的指定公共成员字段。
    ### **3. ****`getDeclaredField(String name)`**
    - **作用**：获取本类声明的**单个字段**
    - **范围**：**任意修饰符**（public / protected / 默认 / private）
    - **包含继承**：❌ 只看本类，父类字段拿不到
    - 返回值：返回字段值
    - 传参：字段名字符串
    ### **4. ****`getDeclaredFields()`**
    - **作用**：获取本类声明的**所有**字段（返回 `Field[]`）
    - **范围**：任意修饰符，仅本类
    - 传入：空参调用
    - 返回：返回一个 Field 类的对象，它反映此 Class 对象所表示的类或接口的指定公共成员字段。
  ## 获取成员方法的方法
    ### **1. ****`getMethod(String name, Class<?>... paramTypes)`**
    - **作用**：获取指定的**单个方法**（需传方法名 + 参数类型列表来精确定位）
    - **范围**：只能获取 **public** 方法
    - **包含继承**：✅ 本类 + 父类的 public 方法，**还包括 Object 类的 public 方法**（如 `toString`、`hashCode`）
    - **找不到时**：抛 `NoSuchMethodException`
    - 传入：方法名，参数类型列表
    - 返回：Method 对象，它是一个“方法描述对象”，封装了目标方法的全部元数据。
    ### **2. ****`getMethods()`**
    - **作用**：获取**所有** public 方法
    - **范围**：本类 + 父类 + Object 类的全部 public 方法
    - 传入：空参调用
    - 返回：Method数组
    ### **3. ****`getDeclaredMethod(String name, Class<?>... paramTypes)`**
    - **作用**：获取本类声明的**单个方法**
    - **范围**：**任意修饰符**（含 private、static、final 等修饰的方法）
    - **包含继承**：❌ 只看本类
    - 传入：方法名，参数类型列表
    - 返回：Method数组
    - 访问私有属性的方法需要调用`setAccessible(true)`这个方法打开强行访问私有权限
    ### **4. ****`getDeclaredMethods()`**
    - **作用**：获取本类声明的**所有**方法
    - **范围**：任意修饰符，仅本类
    - 传入：空参调用
    - 返回：Method 对象，它是一个“方法描述对象”，封装了目标方法的全部元数据。
    - 需要调用`setAccessible(true)`这个方法打开强行访问私有权限
  ## 类型判断
  ```java
isInterface();               // 是否接口
isArray();                   // 是否数组
isEnum();                    // 是否枚举
isAnnotation();              // 是否注解类型
isPrimitive();               // 是否基本类型
isInstance(obj);             // obj 是否为该类实例（相当于 instanceof）
  ```
  ## 注解相关
  ```java
isAnnotationPresent(MyAnno.class);  
// 是否有某注解
getAnnotation(MyAnno.class);        
// 获取注解对象
  ```
  ## 其他
  ```java
getClassLoader();              
// 获取类加载器
getResource("/xx");            
// 获取资源文件
cast(obj);                     
// 安全类型转换（替代强转）
asSubclass(clazz);             
// Class 泛型收窄（判断父类是否一致）
isAssignableFrom(clazz2);      
// clazz2 是否可赋值给当前类
  ```
[通过Class对象创建类的对象](通过class对象创建类的对象/index.md)
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
[反射调用方法](反射调用方法/index.md)
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

  # 实例：调用public方法
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
