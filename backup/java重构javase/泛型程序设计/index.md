---
{
  "id": "3df5a2dd-8276-800a-8273-f728f009e972",
  "url": "https://app.notion.com/p/3df5a2dd8276800a8273f728f009e972",
  "created_time": "2026-09-18T06:44:00.000Z",
  "last_edited_time": "2026-09-25T09:43:00.000Z"
}
---

# 4️⃣ 泛型程序设计


[第一章：泛型](第一章泛型/index.md)
  泛型这东西初学不用看那么多，越看越燃，搞清楚泛型出现的几个位置就行
  泛型类
    试想一下这种情况：统计期末成绩，但成绩有「优/良/中」 和 「分数」两种表示方法，还要求把它们用同一个变量表示。显然「优/良/中」是String类，「分数」是Float类，这怎么办？
    当然，我们可以将该变量定义为Object类（所有类都继承自Object类），但这样会带来安全问题（传入什么类型的值都行）
    这时，你就需要泛型类解决
    # 语法
    > 泛型思想：定义变量时类型先留空（用“类型参数”替代空缺），调用时再声明类型
    > 人话：先找一个变量作为类型，运行时再根据实际传入数据的类型写入具体的类型（编译时一律以Object类型编译）
    注意，泛型的语法非常割裂且语法逻辑不统一，请按泛型出现的4处位置记忆
    ### 出现位置1：类名后（泛型声明）
    在类中泛型声明跟在类名后
    ```java
class Box<T> {              // ← 类名后紧跟 <T>
//        ↑
//   "这个类接受一个类型参数，名字叫T"

    ```
    ### 出现位置2：**类内部 —— 使用（当普通类型用）**
    在类内部把类型参数当正常的类型使用
    ```java
class Box<T> {
    T field;                // 当字段类型用
    T get() { return field; }   // 当返回值类型用
    void set(T t) { field = t; } // 当参数类型用
}

    ```
    ### 出现位置3：**方法返回值前面 —— 声明（仅泛型方法需要）**
    注意⚠️：在类中泛型声明跟在类名后，但在方法中泛型声明却是在返回值前（这里语法逻辑很sb）
    ```java
       public static <T> void print(T item) { }
                     ↑
// 位置在返回值类型之前！这是泛型方法的"注册"语法

    ```
    ### 出现位置4：类调用（创建对象时）**—— 传入实际类型**
    也是跟在类名后
    注意⚠️：创建对象时等号右侧的类名后也要跟实际的传入类型（可只简写为一对尖括号）
    ```java
Box<String> box;                    // 声明变量时
box = new Box<String>();            // 创建对象时
Box<String> box = new Box<>();      // 右边可以省略写成 <>

    ```
    # 注意
    - 使用泛型后不用对传入的参数进行强制类型转换（泛型能接收所有类型，用不着转换）
    - 泛型只能在类/方法中使用，不能通过这个不确定的类型创建对象或数组
    - 静态方法不能使用泛型，因为泛型与对象挂钩
    - 使用了泛型的变量实际上是Object类型的
    - 泛型只能代表引用类型，不能代表基本数据类型，需要使用对应的包装类（依旧屎山语法）
    - 泛型支持嵌套（应该不会有人这么写吧）
    - 当然，泛型实现的是代码复用，而不能做到同一个对象中的同一个变量能传入两种类型的数据，它可以实现不同的对象的同一个变量传入不同类型的数据
    # `<?>`通配符
    `<?>`通配符的泛型可以接收所有类型，但只能读不能写
    # 同时定义/使用多个泛型
    定义
    ```java
public class Test<A, B, C> {   //多个类型变量使用逗号隔开
    public A a;
    public B b;
    public C c;
}
    ```
    使用
    ```java
public static void main(String[] args) {
    Test<String, Integer, Character> test = new Test<>();  //使用钻石运算符可以省略其中的类型
    test.a = "lbwnb";
    test.b = 10;
    test.c = '淦';
}
    ```
    # 记住
    **Java是假泛型，原理是将所有泛型（类型参数）改写成Object，再通过编译器检查泛型声明实现的**
    **代码阅读方法：如果合起来看不懂，那就先忽视尖括号（反正这东西不会被编译进去），看明白这是什么东西，再看此处是泛型参数的声明还是传入实际类型**
    # Java这点最臭
    Java5添加泛型又不愿意牺牲旧版兼容性，搞了个假泛型，语法逻辑臭不可闻，既反直觉，又不统一
  泛型与多态
    这节没有啥，主要就是讲接口，抽象类，记录类型（Java16）也可以用泛型，因为他们都是特殊的类，所以用法和类差不多（都是加到类名后面）
    # 接口
    定义
    ```java
public interface Study<T> {
    T test();
}
    ```
    传入实际类型
    ```java
static class Test implements Study<Integer> {
	@Override
	...
}
    ```
    或者继续使用泛型
    ```java
static class Test implements Study<T> {
	@Override
	...
}
    ```
    # 继承
    继承也一样
    ```java
static class Father<T> {
    
}

static class Son extends Father<String> {

}
    ```
  泛型方法
    再次重申：泛型解决的是某类/方法的传入参数不确定时的代码复用问题
    # 语法
    泛型在方法中的语法和在类中的语法是不一样的，这主要是Java的历史包袱导致的
    泛型在方法中的声明是在返回值类型前定义的
    ```java
private static <T> void test(T t){   //在返回值类型前添加<>并填写泛型变量表示这个是一个泛型方法
        ...
    }
    ```
    还有说法说“泛型方法会在使用时自动确定泛型类型”，这个叫类型推断，但无论推断还是不推断，最终类型都会被擦除成Object，这只是个语法糖
  泛型的界限
    我们知道，泛型可以接收多种数据类型的数据，但什么都接收未免也太不安全了，因此泛型的界限就是对泛型可接收的类型的限制
    # 语法
    ### 泛型上界
    表示泛型必须是该类或该类的子类
    ```java
<泛型名 super 类>
    ```
    例
    ```java
// 类或方法声明中使用 extends 定义上界
class Box<T extends Number> { }          // 泛型参数的上界
void print(List<? extends Number> list) { }  // 通配符上界

    ```
    ### 泛型下界
    表示泛型必须是该类或该类的父类
    泛型下界只能用于通配符“？”
    ```java
<？ super 类>
    ```
    例
    ```java
void addNumbers(List<? super Integer> list) { }
    ```
    泛型下界很少使用，且有一堆特性，可暂时忽略
  类型擦除
    前面已经介绍过，Java的泛型是假泛型，它底层并不支持把类型空着不写，因此在语法上它采用了类似注释的形式来表示泛型，这些”注释“不会被编译进二进制文件，而空缺的类型全部由Object类型代替（没有泛型上界的情况，有泛型上界则全部由泛型上界的类型替代）
    没了，太高级的没听懂
  协变/逆变
    不好意思，这节选学，我直接跳过
  函数式接口
    # 前置内容说明
    本节需要熟悉“泛型”，“匿名内部类”，“Lambda表达式”等内容
    链接在这里↓
    [泛型与多态](https://app.notion.com/p/3df5a2dd827680ca9354f5718b41b5a3) [匿名内部类](https://app.notion.com/p/3db5a2dd8276806190c1d8e1efcba247) [Lambda表达式](https://app.notion.com/p/3db5a2dd827680bf9e55d713895473c1) 
    # 是什么
    我们知道，接口是对类的抽象，准确来说，接口只定义了行为，具体实现由对应的实现类实现
    Java自带了一些类/方法去便于我们进行一些操作（详见[第六章：常用工具类](https://app.notion.com/p/3de5a2dd8276805f8339d7e4eff90df7) ），和他们类似，Java也自带了一些接口（函数式接口），它们不是便于开发者编程的，而是用于规定一些标准行为
    因为Java希望你的程序是由“标准行为”拼接成的，这可以有效提高代码复用能力
    （如：吃饭是由“张嘴”“闭嘴”“咀嚼”这些标准行为组成的，喝水是由“张嘴”闭嘴”组成，其中张嘴/闭嘴复用了吃饭的实现）
    # 举个例子
    需求：将一个经过一系列计算得出的字符串（假设为“小明”）赋值给Student类中的name变量
    ```java
//Student类
public class Student{
	String name;
	
	//给name变量赋值的方法
	public void takeName (Supplier<String> name){
			this.name=name.get()
	}
	
}
    ```
    ```java
public class Main{
	//主方法
	public static void main(String[] args){
	Student student = new Student();
	student.takeName(new Supplier(){
	  public String get(){
	  
		  一系列操作...
		  return "小明";
		  }
	  }); 
	}
}
    ```
    或者也可以写成Lambda表达式
    ```java
public class Main{
	//主方法
	public static void main(String[] args){
	Student student = new Student();
	student.takeName(()->{
		  一系列操作...
		  return "小明";
	  }); 
	}
}
    ```
    # 四大核心函数式接口
    ## **1. Supplier<T> —— 供给型（只出不进）**
    **不接收任何参数，返回一个结果。** 像一个“工厂/生产者”。
    ## **2. Consumer<T> —— 消费型（只进不出）**
    **接收一个参数，没有返回值。** 像“消费者”，处理完就结束。
    ## **3. Function<T, R> —— 函数型（进一个，出一个）**
    **接收一个参数 T，返回结果 R。** 像数学中的函数 y = f(x)
    ## **4. Predicate<T> —— 断言型（进一个，出布尔）**
    **接收一个参数，返回 boolean。** 用于条件判断
    | **接口** | **抽象方法** | **输入** | **输出** | **语义** | **常见应用** |
    | --- | --- | --- | --- | --- | --- |
    | `Supplier<T>` | `get()` | 无 | T | 生产数据 | 工厂、惰性求值 |
    | `Consumer<T>` | `accept(T)` | T | 无 | 消费数据 | forEach |
    | `Function<T,R>` | `apply(T)` | T | R | 转换数据 | map |
    | `Predicate<T>` | `test(T)` | T | boolean | 判断条件 | filter |
  Optional判空包装（Java8）
    # 判空目的
    Java虽说不让操作指针，但是有空指针异常的，如果你调用一个不存在的对象的方法，那么就会报错，所以某些时候我们无法确定传入的值是否为空，就需要判空（避免程序报错终止）
    # 传统判空
    传统判空使用if语句来判断
    ```java
public class Student{
	String name; 
	
	public void main(String[] args){
		if(name!=null){System.out.println(name);}
		else{System.out.println("name变量未赋值！");}
	}
}
    ```
    这看起来是不是挺常规的
    但如果是链式调用的判空就会出现if嵌套的情况，这对可读性及维护性很不利↓
    ```java
if (user != null) {
    Address address = user.getAddress();
    if (address != null) {
        String city = address.getCity();
        if (city != null) {
            System.out.println(city);
        }
    }
}

    ```
    > PS：Java原生支持链式调用，像这样 `对象名.方法1().方法2().方法3()`
    # 判空包装
    原理很简单：Java自带了一个Optional类专门用来判空，将判空逻辑写到了该类的方法里
    使用方法：创建该类的对象，将待判空的引用作为参数传入，调用该类的方法来获取判空结果
    注意⚠️：
    - Optional类不能直接new，而是使用其内部的三个方法`of` / `ofNullable` / `empty`来创建对象
    - Optional类是泛型类，使用时需要声明类型
    ### 创建对象方法
    Optional类不能直接new，而是使用其内部的三个方法`of` / `ofNullable` / `empty`来创建对象
    | **方法** | **说明** | **示例** |
    | --- | --- | --- |
    | `empty()` | 创建空的 Optional对象 | `Optional.empty()` |
    | `of(value)` | 包装值，**值不能为 null**，否则抛 NPE | `Optional.of("abc")` |
    | `ofNullable(value)` | 包装值，**允许为 null**（推荐常用） | `Optional.ofNullable(maybeNull)` |
    ```java
Optional<String> opt1 = Optional.of(a);      // 不能传 null，传了直接报错
Optional<String> opt2 = Optional.ofNullable(a); // 可以传 null，返回空 Optional
Optional<String> opt3 = Optional.empty();          // 直接创建空的
    ```
    ### 获取判空结果（判空后操作）
    **判断是否有值**
    | **方法** | **说明** | **示例** |
    | --- | --- | --- |
    | `isPresent()` | 有值返回 true | `opt.isPresent()` |
    | `isEmpty()` | 无值返回 true（Java 11+） | `opt.isEmpty()` |
    **获取值**
    | **方法** | **说明** | **示例** |
    | --- | --- | --- |
    | `get()` | 取值，**空则抛异常**（⚠️ 不推荐） | `opt.get()` |
    | `orElse(默认值)` | 空则返回默认值 | `opt.orElse("默认")` |
    | `orElseGet(供应者)` | 空则执行 lambda 生成默认值（**惰性**） | `opt.orElseGet(() -> "默认")` |
    | `orElseThrow(异常)` | 空则抛指定异常 | `opt.orElseThrow(() -> new RuntimeException("空了"))` |
    **消费值（有值时做事）**
    | **方法** | **说明** | **示例** |
    | --- | --- | --- |
    | `ifPresent(消费者)` | 有值就执行，没值跳过 | `opt.ifPresent(v -> print(v))` |
    | `ifPresentOrElse(消费者, Runnable)` | 有值执行前者，无值执行后者（Java 9+） | `opt.ifPresentOrElse(v -> print(v), () -> print("空"))` |
    **转换值（链式调用的核心 ⭐）**
    | **方法** | **说明** | **示例** |
    | --- | --- | --- |
    | `map(函数)` | 转换值，普通转换 | `opt.map(User::getName)` |
    | `flatMap(函数)` | 转换值，**函数返回的本身是 Optional 时用** | `opt.flatMap(u -> Optional.ofNullable(u.getName()))` |
    | `filter(谓词)` | 条件过滤，不满足变空 | `opt.filter(u -> u.getAge() >= 18)` |
    **多选一（Java 9+）**
    | **方法** | **说明** | **示例** |
    | --- | --- | --- |
    | `or(供应者)` | 空则换另一个 Optional | `opt.or(() -> Optional.of("备用"))` |
    | `stream()` | 转成 Stream（有 0 或 1 个元素） | `opt.stream()` |
    **其他**
    | **方法** | **说明** | **示例** |
    | --- | --- | --- |
    | `equals(obj)` | 比较两个 Optional | `opt1.equals(opt2)` |
    | `hashCode()` | 哈希值 | `opt.hashCode()` |
    | `toString()` | 打印，形如 `Optional[abc]` 或 `Optional.empty` | `opt.toString()` |
    # 链式调用示例
    ```java
private static void test(String str){
    Integer i = Optional.ofNullable(str).map(String::length).orElse(-1);
    System.out.println(i);
}
    ```
    当然，一般会缩进成这种形式（好看）
    ```java
private static void test(String str){
    Integer i = Optional
            .ofNullable(str)   //创建对象
            .map(String::length)   //使用map来进行映射，将当前类型转换为其他类型，或者是进行处理
            .orElse(-1);
    System.out.println(i);
}
    ```
  (Java 9/10) 判空包装增强
    这节内容已被上节涵盖（未采用柏码教程）
[第二章：Java数据结构](第二章java数据结构/index.md)
  这章基于菜鸟教程编撰，和柏码对应部分完全不同
  链接在这↓
  [https://www.runoob.com/java/java-data-structures.html](https://www.runoob.com/java/java-data-structures.html)
  菜鸟教程该部分仅介绍了各种数据结构在Java中的实现类/接口，及特性，没有做原理说明
  # Java 数据结构
  Java 提供了丰富的数据结构来处理和组织数据。
  Java 的 java.util 包中提供了许多这些数据结构的实现，可以根据需要选择合适的类。
  以下是一些常见的 Java 数据结构：
  ### **数组（Arrays）**
  数组（Arrays）是一种基本的数据结构，可以存储固定大小的相同类型的元素。
  ```java
int[] array=newint[5];
  ```
  - **特点：** 固定大小，存储相同类型的元素。
  - **优点：** 随机访问元素效率高。
  - **缺点：** 大小固定，插入和删除元素相对较慢。
  ### **列表（Lists）**
  Java 提供了多种列表实现，如 ArrayList 和 LinkedList。
  ```java
List<String> arrayList=newArrayList<>();List<Integer> linkedList=newLinkedList<>();
  ```
  **ArrayList:**
  - **特点：** 动态数组，可变大小。
  - **优点：** 高效的随机访问和快速尾部插入。
  - **缺点：** 中间插入和删除相对较慢（需要遍历）
  **LinkedList:**
  - **特点：** 双向链表，元素之间通过指针连接。
  - **优点：** 插入和删除元素高效，迭代器性能好。
  - **缺点：** 随机访问相对较慢。
  ### **集合（Sets）**
  集合（Sets）用于存储不重复的元素，常见的实现有 HashSet 和 TreeSet。
  ```java
Set<String> hashSet=newHashSet<>();Set<Integer> treeSet=newTreeSet<>();
  ```
  **HashSet:**
  - **特点：** 无序集合，基于HashMap实现。
  - **优点：** 高效的查找和插入操作。
  - **缺点：** 不保证顺序。
  **TreeSet:**
  - **特点：**TreeSet 是有序集合，底层基于红黑树实现，不允许重复元素。
  - **优点：** 提供自动排序功能，适用于需要按顺序存储元素的场景。
  - **缺点：** 性能相对较差，不允许插入 null 元素。
  ### **映射（Maps）**
  映射（Maps）用于存储键值对，常见的实现有 HashMap 和 TreeMap。
  ```plain text
Map<String,Integer> hashMap=newHashMap<>();Map<String,Integer> treeMap=newTreeMap<>();
  ```
  **HashMap:**
  - **特点：** 基于哈希表实现的键值对存储结构。
  - **优点：** 高效的查找、插入和删除操作。
  - **缺点：** 无序，不保证顺序。
  **TreeMap:**
  - **特点：** 基于红黑树实现的有序键值对存储结构。
  - **优点：** 有序，支持按照键的顺序遍历。
  - **缺点：** 插入和删除相对较慢。
  ### **栈（Stack）**
  栈（Stack）是一种线性数据结构，它按照后进先出（Last In, First Out，LIFO）的原则管理元素。在栈中，新元素被添加到栈的顶部，而只能从栈的顶部移除元素。这就意味着最后添加的元素是第一个被移除的。
  ```plain text
Stack<Integer> stack=newStack<>();
  ```
  **Stack 类:**
  - **特点：** 代表一个栈，通常按照后进先出（LIFO）的顺序操作元素。
  ### **队列（Queue）**
  队列（Queue）遵循先进先出（FIFO）原则，常见的实现有 LinkedList 和 PriorityQueue。
  ```plain text
Queue<String> queue=newLinkedList<>();
  ```
  **Queue 接口:**
  - **特点：** 代表一个队列，通常按照先进先出（FIFO）的顺序操作元素。
  - **实现类：** LinkedList, PriorityQueue, ArrayDeque。
  ### **堆（Heap）**
  堆（Heap）优先队列的基础，可以实现最大堆和最小堆。
  ```java
PriorityQueue<Integer> minHeap=newPriorityQueue<>();PriorityQueue<Integer> maxHeap=newPriorityQueue<>(Collections.reverseOrder());
  ```
  ### **树（Trees）**
  Java 提供了 TreeNode 类型，可以用于构建二叉树等数据结构。
  ```java
classTreeNode{int val;TreeNode left;TreeNode right;TreeNode(int x){ val= x;}}
  ```
  ### **图（Graphs）**
  图的表示通常需要自定义数据结构或使用图库，Java 没有内建的图类。
  以上介绍的只是 Java 中一些常见的数据结构，实际上还有很多其他的数据结构和算法可以根据具体问题选择使用。
  ---
  ## 其他一些说明
  以下这些类是传统遗留的，在 Java2 中引入了一种新的框架-集合框架(Collection)，我们后面再讨论。
  ### **枚举（Enumeration）**
  枚举（Enumeration）接口虽然它本身不属于数据结构,但它在其他数据结构的范畴里应用很广。 枚举（The Enumeration）接口定义了一种从数据结构中取回连续元素的方式。
  例如，枚举定义了一个叫nextElement 的方法，该方法用来得到一个包含多元素的数据结构的下一个元素。
  关于枚举接口的更多信息，[请参见枚举（Enumeration）](https://www.runoob.com/java/java-enumeration-interface.html)。
  ### **位集合（BitSet）**
  位集合类实现了一组可以单独设置和清除的位或标志。
  该类在处理一组布尔值的时候非常有用，你只需要给每个值赋值一"位"，然后对位进行适当的设置或清除，就可以对布尔值进行操作了。
  关于该类的更多信息，[请参见位集合（BitSet）](https://www.runoob.com/java/java-bitset-class.html)。
  ### **向量（Vector）**
  向量（Vector）类和传统数组非常相似，但是Vector的大小能根据需要动态的变化。
  和数组一样，Vector对象的元素也能通过索引访问。
  使用Vector类最主要的好处就是在创建对象的时候不必给对象指定大小，它的大小会根据需要动态的变化。
  关于该类的更多信息，[请参见向量(Vector)](https://www.runoob.com/java/java-vector-class.html)
  ### **栈（Stack）**
  栈（Stack）实现了一个后进先出（LIFO）的数据结构。
  你可以把栈理解为对象的垂直分布的栈，当你添加一个新元素时，就将新元素放在其他元素的顶部。
  当你从栈中取元素的时候，就从栈顶取一个元素。换句话说，最后进栈的元素最先被取出。
  关于该类的更多信息，[请参见栈（Stack）](https://www.runoob.com/java/java-stack-class.html)。
  ### **字典（Dictionary）**
  字典（Dictionary） 类是一个抽象类，它定义了键映射到值的数据结构。
  当你想要通过特定的键而不是整数索引来访问数据的时候，这时候应该使用 Dictionary。
  由于 Dictionary 类是抽象类，所以它只提供了键映射到值的数据结构，而没有提供特定的实现。
  关于该类的更多信息，[请参见字典（ Dictionary）](https://www.runoob.com/java/java-dictionary-class.html)。
  **Dictionary 类在较新的 Java 版本中已经被弃用（deprecated），推荐使用 Map 接口及其实现类，如 HashMap、TreeMap 等，来代替 Dictionary。**
  Map 接口及其实现类 可以参考：[Java 集合框架](https://www.runoob.com/java/java-collections.html)。
  ### **哈希表（Hashtable）**
  Hashtable类提供了一种在用户定义键结构的基础上来组织数据的手段。
  例如，在地址列表的哈希表中，你可以根据邮政编码作为键来存储和排序数据，而不是通过人名。
  哈希表键的具体含义完全取决于哈希表的使用情景和它包含的数据。
  关于该类的更多信息，[请参见哈希表（HashTable）](https://www.runoob.com/java/java-hashTable-class.html)。
  ### **属性（Properties）**
  Properties 继承于 Hashtable.Properties 类表示了一个持久的属性集.属性列表中每个键及其对应值都是一个字符串。
  Properties 类被许多Java类使用。例如，在获取环境变量时它就作为System.getProperties()方法的返回值。
  关于该类的更多信息，[请参见属性（Properties）](https://www.runoob.com/java/java-properties-class.html)。
