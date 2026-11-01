---
{
  "id": "4075a2dd-8276-80f0-8728-cb60e4e017a7",
  "url": "https://app.notion.com/p/Class-4075a2dd827680f08728cb60e4e017a7",
  "created_time": "2026-10-28T07:04:00.000Z",
  "last_edited_time": "2026-10-28T10:12:00.000Z"
}
---

#  Class对象的使用

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
