---
{
  "id": "3e55a2dd-8276-8090-a707-cb1ad7e2212a",
  "url": "https://app.notion.com/p/IO-3e55a2dd82768090a707cb1ad7e2212a",
  "created_time": "2026-09-24T08:30:00.000Z",
  "last_edited_time": "2026-10-14T08:09:00.000Z"
}
---

# 5️⃣ 集合类与IO

啊，这一章节大量采用ai与菜鸟教程的内容，仅使用了柏码的目录作为指导（柏码这节拉了）

[集合类重构（Java集合框架）](集合类重构java集合框架/index.md)
  # 为什么重构
  啊，柏码那里是分接口介绍的，一开始没看出来，所以写出来的文档没有可读性
  现在声明：本章以不同接口分节
  每节大致结构是：接口（继承关系，作用，定义的方法）➡️实现类➡️通用算法（不一定写）
  旧页面扔归档页面里了
  # 声明
  这个文档只讲框架，不是API详情，具体使用需参考官方API
  # 省流：
  这章讲的是Java集合框架
  什么是集合框架：Java针对“集合”做的一系列 创建/操作 的标准 方法/类/接口
  什么是集合：集合是针对Java不同数据结构做的标准的 创建/操作 的 方法/类/接口
  集合框架的设计分为三层：接口（定义行为），实现类（实现接口），通用算法（将实现类组合起来，做成一些常用算法）
  JavaSE非常贴心的将这三层全部自带了，开发者几乎不需要自己实现任何东西
  根集合接口
    Java集合框架其实就是一堆接口实现一堆类，组合成一堆算法
    **集合框架的设计分为三层：接口（定义行为），实现类（实现接口），通用算法（将实现类组合起来，做成一些常用算法）**
    Java集合框架所有集合的祖先都是集合根接口`Collection`

    ![](assets/3e75a2dd-8276-8003-97d4-f2d0fc476734.gif)
    Java 集合框架提供的 接口/类/方法 性能优良，还是很推荐使用的
    > java集合框架位于java.util包中，别忘了import导入
    # Collection 接口作用
    这个接口是所有集合框架接口的祖先，没有特别具体的作用（只是说明这是个集合框架）
    > Java不提供直接继承自Collection的类，只提供继承于的子接口
    # Collection 接口实现类
    注意⚠️：前文说Java不提供直接继承自Collection的类（因为接口只能被接口继承，不能被类继承），不代表Collection 接口不能有实现类
    如果不算子类下挂的实现类（“**直接**实现 `Collection` 接口”的类），Collection 接口只有一个实现类**`AbstractCollection`**
    **`AbstractCollection`**类实现了大部分接口的通用方法
    ### Q&A
    Q：为什么不是在接口下直接实现各种类，而是搞一个**`AbstractCollection`**类实现所有？实现一个Collection 接口有啥用啊？
    A：**`AbstractCollection`**类实现的是多数接口的通用方法，这是为了避免重复实现造成可维护性下降
  List接口
    # List接口
    List接口直接继承自Collection接口（集合根接口）（Java21以前）或SequencedCollection（Java21+）
    List接口在**`AbstractCollection`**类及其子类实现
    它定义了列表（线性表）这种数据类型
    > 列表包含以下数据类型：动态数组，双向链表。常用的实现类有**ArrayList，LinkedList，Vector，Stack，CopyOnWriteArrayList**
    # List接口中定义的方法
    跟数组一样，列表每个元素有自己的下标
    **继承自 Collection 的基本方法**
    | **方法** | **说明** |
    | --- | --- |
    | `int size()` | 返回列表中元素的数量 |
    | `boolean isEmpty()` | 判断列表是否为空 |
    | `boolean contains(Object o)` | 判断是否包含指定元素 |
    | `boolean add(E e)` | 向末尾添加元素 |
    | `boolean remove(Object o)` | 移除第一个匹配的元素 |
    | `boolean containsAll(Collection<?> c)` | 是否包含指定集合的所有元素 |
    | `boolean addAll(Collection<? extends E> c)` | 添加指定集合的所有元素 |
    | `boolean removeAll(Collection<?> c)` | 移除指定集合中包含的元素 |
    | `boolean retainAll(Collection<?> c)` | 只保留指定集合中包含的元素（交集） |
    | `void clear()` | 清空列表 |
    | `Iterator<E> iterator()` | 返回迭代器 |
    | `Object[] toArray()` | 转换为数组 |
    | `<T> T[] toArray(T[] a)` | 转换为指定类型的数组 |
    **List 特有的索引方法**
    | **方法** | **说明** |
    | --- | --- |
    | `E get(int index)` | **获取**指定索引的元素 |
    | `E set(int index, E element)` | **替换**指定索引的元素，返回旧值 |
    | `void add(int index, E element)` | 在指定索引处**插入**元素 |
    | `E remove(int index)` | 移除指定索引的元素，返回被移除的元素 |
    | `int indexOf(Object o)` | 返回元素**第一次**出现的索引，不存在返回 -1 |
    | `int lastIndexOf(Object o)` | 返回元素**最后**出现的索引，不存在返回 -1 |
    | `boolean addAll(int index, Collection<? extends E> c)` | 在指定索引处插入集合的所有元素 |
    **List 特有的迭代方法**
    | **方法** | **说明** |
    | --- | --- |
    | `ListIterator<E> listIterator()` | 返回列表迭代器（可双向遍历） |
    | `ListIterator<E> listIterator(int index)` | 从指定索引开始迭代 |
    **Java 8+ 新增的默认方法**
    | **方法** | **说明** |
    | --- | --- |
    | `default void replaceAll(UnaryOperator<E> operator)` | 对每个元素应用操作并替换 |
    | `default void sort(Comparator<? super E> c)` | 根据比较器排序 |
    | `default Spliterator<E> spliterator()` | 返回可分割迭代器（并行处理） |
    **Java 21+ 新增（SequencedCollection）**
    | **方法** | **说明** |
    | --- | --- |
    | `void addFirst(E e)` | 在头部添加元素 |
    | `void addLast(E e)` | 在尾部添加元素 |
    | `E getFirst()` | 获取第一个元素 |
    | `E getLast()` | 获取最后一个元素 |
    | `E removeFirst()` | 移除并返回第一个元素 |
    | `E removeLast()` | 移除并返回最后一个元素 |
    | `List<E> reversed()` | 返回反转视图 |
    # 特性
    - 集合类在删除元素时，只会调用`equals`方法进行判断内容是否相等，而不是进行等号判断是否为同一对象，此时只会删除第一个元素
    - 列表中允许存在相同元素
    - 集合类支持嵌套使用，一个集合中可以存放其他集合
    ```java
public static void main(String[] args) {
    List<List<String>> list = new LinkedList<>();
    list.add(new LinkedList<>());   //集合中的每一个元素就是一个集合，这个套娃是可以一直套下去的
    System.out.println(list.get(0).isEmpty());
}
    ```
    # 常用实现类
    **ArrayList 动态数组**（线性表的一种）：更适合随机访问，因为可以直接读取某个下标的元素。插入则性能较差，因为需要移动一组元素，让出空间。
    **LinkedList 双向链表：**不适合随机访问，因为无法直接获取某个元素，只能遍历查找。插入性能较好，因为可以直接改变链表中结点的指向。
    # 列表基本操作（以ArrayList为例）
    上面说这么多下面直接演示
    <u>***用法总结：先创建列表→再添加元素→再进行各种操作***</u>
    ### 创建
    创建对象以创建列表
    ```java
List<String> list = new ArrayList<>();
    ```
    注意：需将对象引用给List而非ArrayList，方便后期更改类型
    ### 添加元素
    调用add()方法，内容作为参数传入
    ```java
list.add("张三");
    ```
    ### 查找元素
    调用相应方法
    ```java
//按照索引（下标）查找，使用get()方法
String name = list.get(0);
//按内容查找索引，使用indexOf()方法
int index = list.indexOf("李四");
//判断内容是否存在，使用contains()方法
boolean has = list.contains("王五"); 
    ```
    ### 修改元素
    调用相应方法
    ```java
// 通过索引替换
list.set(1, "新名字");  // 替换索引 1 的元素，返回旧值

// 替换所有元素（Java 8+）
list.replaceAll(s -> s + "!");
    ```
    ### 删除元素
    依旧是调用相应方法
    ```java
// 1. 按索引删除
list.remove(0);          

// 2. 按对象删除（注意 Integer 的坑）
list.remove("李四"); 
    ```
    另外还有遍历，排序等，不一一演示
  Iterator接口（迭代器）
    # Iterator接口
    作用：用于遍历集合（某种数据结构）的接口，它定义了统一的遍历集合的方法，开发者无需关心底层是什么数据结构，只需调用Iterator接口的实现类即可
    注意：
    - Iterator接口定义的不是集合（不是某种数据结构），它是访问集合的工具接口
    - Java不止有一个迭代器，Iterator接口只是Java 迭代器最简单的实现，ListIterator 是 Collection API 中的接口， 它扩展了 Iterator 接口。
    - 虽然Iterator接口接口是独立于集合类的，但其实现位置与集合类中接口实现位置一致（都在**`AbstractCollection`**类及其子类实现），并不独立于集合类
    继承关系：正如上文所述，”Iterator接口定义的不是集合“ Iterator接口不在集合根接口下，它是独立的顶层接口，因此它不算集合类，它是独立的工具类

    # Iterator接口中定义的方法
    - **next()** - 返回迭代器的下一个元素，并将迭代器的指针移到下一个位置。
    - **hasNext()** - 用于判断集合中是否还有下一个元素可以访问。
    - **remove()** - 从集合中删除迭代器最后访问的元素（可选操作）
    # 注意
    - Iterator接口迭代器只能从前往后单向遍历，ListIterator 接口迭代器支持双向遍历
    - 在使用迭代器遍历集合时，不能直接修改集合中的元素（可能会导致 ConcurrentModificationException 异常），需要使用迭代器的 remove() 方法安全删除当前元素
    - 迭代器只能使用一次，如果需要再次使用，需要再次获取迭代器（创建迭代器对象）
    # 使用方法（以ArrayList+Iterator为例）
    使用方法总结：**由于迭代器的实现类就是集合类的实现类（对应数据结构的实现类），所以获取迭代器不是创建一个独立于集合类的某个类的对象，而是直接调用相应数据结构的iterator()方法，该方法会返回一个对象，将其引用给Iterator接口即可**
    Iterator 类位于 java.util 包中，使用前需要引入它
    ```java
import java.util.Iterator; // 引入 Iterator 类
    ```
    ### （前置要求）创建集合
    ```java
// 创建集合
ArrayList<String> sites = new ArrayList<String>();
sites.add("Google");
sites.add("Runoob");
sites.add("Taobao");
sites.add("Zhihu");
    ```
    ### 获取迭代器（创建迭代器）
    我们需要用到集合ArrayList（列表）下的一个方法iterator()，这个方法的作用是：返回一个迭代器对象
    然后引用给接口Iterator
    （这里写法是不是有点奇怪➡️因为迭代器的构造方法是私有的，因此无法通过new创建对象，而是需要使用静态方法iterator()来创建对象）
    ```java
// 获取迭代器
Iterator<String> it = sites.iterator();
    ```
    ### 返回下一个元素【next（）方法】
    ```java

System.out.println(it.next());
    ```
    ### 逐个返回所有元素【next()+hasNext()方法】
    以下是最简单的例子
    ```java
while(it.hasNext()) {
    System.out.println(it.next());
}
    ```
    PS：使用迭代器遍历集合时，如果在遍历过程中集合发生了修改（例如添加或删除元素），可能会导致 ConcurrentModificationException 异常，为了避免这个问题，可以使用迭代器自身的 **remove()** 方法进行安全删除
    ### 删除元素【remove() 方法】
    ```java
it.next();
//删除了最后一次访问的元素
    ```
  foreach（ for 循环）语法糖
    `foreach` 是一种用于遍历集合/数组的循环语法，和for循环没有本质区别
    是一种语法糖（for循环针对集合/数组的简便写法）
    ## **基本语法**
    ```plain text
for (元素类型 变量名 : 待遍历的对象) {
    // 循环体，变量代表当前元素
}
    ```
    冒号 `:` 左边是**临时变量的声明**，右边是**要遍历的目标**。
    # 示例
    ```java
// 遍历数组
int[] arr = {1, 2, 3};
for (int num : arr) {
    System.out.println(num);
}
    ```
  Queue和Deque接口
    光看标题是不是看懵了，这啥东西？
    Queue和Deque都是接口
    下面详细介绍
    # Queue接口
    这个接口定义了队列的抽象，它定义了队列一进一出，先进先出的特性
    不必知道具体细节,只需要知道它有这几个抽象方法
    `java.util.Queue` 继承自 `Collection`，除了继承的方法外，定义了以下 6 个核心方法：
    ```java
public interface Queue<E> extends Collection<E> {
    // 插入
    boolean add(E e);      // 队列已满/受限时抛出 IllegalStateException
    boolean offer(E e);    // 插入失败返回 false，不抛异常

    // 移除
    E remove();            // 队列为空时抛出 NoSuchElementException
    E poll();              // 队列为空时返回 null

    // 检查队首（不移除）
    E element();           // 队列为空时抛出 NoSuchElementException
    E peek();              // 队列为空时返回 null
}

    ```
    # **Deque接口**
    `java.util.Deque` 继承自接口 `Queue`，它定义了针对队列**两端操作**的方法（如头插/尾插）
    一下是API列表：
    ```java
public interface Deque<E> extends Queue<E> {

    // ========== 两端插入 ==========
    void addFirst(E e);       // 头部插入，失败抛异常
    void addLast(E e);        // 尾部插入，失败抛异常
    boolean offerFirst(E e);  // 头部插入，失败返回 false
    boolean offerLast(E e);   // 尾部插入，失败返回 false

    // ========== 两端移除 ==========
    E removeFirst();          // 移除头部，为空抛异常
    E removeLast();           // 移除尾部，为空抛异常
    E pollFirst();            // 移除头部，为空返回 null
    E pollLast();             // 移除尾部，为空返回 null

    // ========== 两端检查（不移除）==========
    E getFirst();             // 查看头部，为空抛异常
    E getLast();              // 查看尾部，为空抛异常
    E peekFirst();            // 查看头部，为空返回 null
    E peekLast();             // 查看尾部，为空返回 null

    // ========== 栈操作（等价于 addFirst/removeFirst/peekFirst）==========
    void push(E e);           // 压栈 → addFirst(e)
    E pop();                  // 弹栈 → removeFirst()
    E peek();                 // 查看栈顶（继承自 Queue，但 Deque 语义指向头部）

    // ========== 元素移除（继承自 Queue 的扩展）==========
    boolean removeFirstOccurrence(Object o);  // 从头到尾删除第一个匹配元素
    boolean removeLastOccurrence(Object o);   // 从尾到头删除第一个匹配元素

    // ========== 逆序视图 ==========
    Iterator<E> descendingIterator();  // 返回反向迭代器（从尾到头）
}

    ```

    乂，我知道这东西有什么用？难道让我自己实现这些接口？
    当然不用↓
    # Queue和Deque的实现类
    ### LinkList（双向链表）
    怎么用？
    **直接创建LinkList类的对象➡️对象名.方法  调用即可**
    ### 专门的队列类
    这个有很多，不一一解释了
    | **专门类** | **底层结构** | **适用场景** |
    | --- | --- | --- |
    | **`ArrayDeque`** | 循环数组 | 通用队列/栈，**性能最好**（数组缓存友好，无节点开销） |
    | `ConcurrentLinkedQueue` | 单向链表 + CAS | 高并发无锁队列 |
    | `LinkedBlockingQueue` | 单向链表 + 锁 | 生产者-消费者模式 |
    | `ArrayBlockingQueue` | 循环数组 + 锁 | 有界队列，生产者-消费者 |
    | `PriorityQueue` | 二叉堆 | 优先级调度 |
    ### 那么有老铁问了：
    Q：乂，linkList不是双向链表么，怎么还兼职做队列？
    A：对，LinkList做双向链表的时候顺手也把队列也给实现了，但是还是建议使用专门的队列类
    # 用法
    这个用法简单：某集合类的对象.方法()
    直接用，不用创建/获取什么东西
  set接口（集合）
    # set接口
    作用：set接口定义了**存储不重复的元素**的数据结构【集合】（这里的集合是数学意义上的集合，而非我们之前提到的集合类也就是Java集合框架）
    继承关系：`set`接口直接继承自集合根接口`Collection`
    实现位置：**`AbstractCollection`**及其子类
    # 注意
    数据结构“集合“
    - 不允许出现重复元素
    - 不支持随机访问（没下标）
    # Set接口定义的方法
    Set接口是从Collection中直接继承的，因此，Set支持的功能其实也就和Collection中定义的差不多
    同样是插入，删除等（需要自己查）
    # 实现类
    ### **HashSet（哈希集合）**
    - **底层结构**：基于 `HashMap` 实现
    - **特点**：无法保证顺序，允许 `null` 元素，不支持随机访问
    使用：
    ```java
public static void main(String[] args) {
		//创建哈希集合
    Set<String> set = new HashSet<>();
    //插入元素
    System.out.println(set.add("AAA"));
    //删除元素
    System.out.println(set.remove("AAA"));
    
    System.out.println(set);
}
    ```
    ### **LinkedHashSet**
    - **底层结构**：基于 `LinkedHashMap` 实现（链表 + 哈希表）
    - **特点**：维护元素的**插入顺序**
    - **性能**：略低于 HashSet，迭代性能更好
    使用：同上
    ### **TreeSet**
    - **底层结构**：基于红黑树（`TreeMap`）实现
    - **特点**：可排序，不允许 `null`
    使用：同上
  Map接口（映射）
    # Map接口
    作用：Map接口定义了“映射”这种逻辑，元素两两对应，也就是“键值对”
    继承关系：和迭代器一样，Map不继承自集合根接口，但Map仍属于Java集合框架，下面引用Oracle官方的说法↓
    > Java Collections Framework 的核心接口由两棵**并列的、相互独立的**接口树构成：**Collection 分支，Map 分支**
    实现类：Map接口的实现类分为 ”一个抽象骨架”（AbstractMap） 和骨架下 “六个具体实现类”（HashMap，LinkedHashMap，Hashtable，WeakHashMap，IdentityHashMap，EnumMap），还有一堆不在抽象骨架下的类
    # Map接口定义的方法
    ```java
//Map并不是Collection体系下的接口，而是单独的一个体系，因为操作特殊
//这里需要填写两个泛型参数，其中K就是键的类型，V就是值的类型，比如上面的学生信息，ID一般是int，那么键就是Integer类型的，而值就是学生信息，所以说值是学生对象类型的
public interface Map<K,V> {
    //-------- 查询相关操作 --------
  
  	//获取当前存储的键值对数量
    int size();

    //是否为空
    boolean isEmpty();

    //查看Map中是否包含指定的键
    boolean containsKey(Object key);

    //查看Map中是否包含指定的值
    boolean containsValue(Object value);

    //通过给定的键，返回其映射的值
    V get(Object key);

    //-------- 修改相关操作 --------

    //向Map中添加新的映射关系，也就是新的键值对
    V put(K key, V value);

    //根据给定的键，移除其映射关系，也就是移除对应的键值对
    V remove(Object key);


    //-------- 批量操作 --------

    //将另一个Map中的所有键值对添加到当前Map中
    void putAll(Map<? extends K, ? extends V> m);

    //清空整个Map
    void clear();


    //-------- 其他视图操作 --------

    //返回Map中存放的所有键，以Set形式返回
    Set<K> keySet();

    //返回Map中存放的所有值
    Collection<V> values();

    //返回所有的键值对，这里用的是内部类Entry在表示
    Set<Map.Entry<K, V>> entrySet();

    //这个是内部接口Entry，表示一个键值对
    interface Entry<K,V> {
        //获取键值对的键
        K getKey();

        //获取键值对的值
        V getValue();

        //修改键值对的值
        V setValue(V value);

        //判断两个键值对是否相等
        boolean equals(Object o);

        //返回当前键值对的哈希值
        int hashCode();

        ...
    }

    ...
}
    ```
    非常多,没全列出来
    # Map接口的实现类（以HashMap为例）
    ### 创建，插入，读取
    ```java
public static void main(String[] args) {
		
		//创建哈希映射
    Map<Integer, String> map = new HashMap<>();
    
    //使用put方法添加键值对
    map.put(1, "小明");   
    map.put(2, "小红");
    
    //使用get方法根据键获取对应的值
    System.out.println(map.get(2)); 
}
    ```
    PS：映射（Map）无法添加相同的键，即使值不同。如果出现键相同的情况，那么会覆盖掉旧的，可以使用Java8新方法putIfAbsent()安全插入
    ### 默认返回值
    ```java
public static void main(String[] args) {
    Map<Integer, String> map = new HashMap<>();
    map.put(1, "小明");
    
    //get方法，找不到键值对默认返回null
    System.out.println(map.get(3));
    
    //getOrDefault方法，找不到键值对可以返回自定义的值
    System.out.println(map.getOrDefault(3, "备胎"));   //Java8新增操作，当不存在对应的键值对时，返回备选方案
}
    ```
  “比较“相关接口
    下面分成两种接口介绍：
    # `Comparable`接口
    ### 作用：
    `java.lang.Comparable` 接口，让类**自身**具备可比较的能力
    ### 工作原理：
    1. 在类定义时实现`Comparable`接口并重写`compareTo()` 方法，来使得类拥有“比较”的能力
    PS：`compareTo()` 方法用来定义比较规则
    1. 在使用时调用排序算法（sort等方法）
    1. 排序方法会在其内部调用compareTo() 方法并直接在原有对象的基础上进行排序
    示例：
    ```java
//类定义

public class Test implements Comparable<Test>{
	int a;
	
	//构造方法，用来为成员变量a赋值
	public Test(int a){
	this.a=a;
	}
	
	//在类内重写compareTo()方法以获得比较的能力
	@Override
	public int compareTo(Test o) {
      return this.a - o.a;
      //这里简化了比较的过程，仅用a-b来实现
    }

	}

    ```
    ```java
//使用，以自然排序算法sort为例
Test test1 =new Test(5);
Test test2 =new Test(4);
test1.sort(test2);
    ```
    ### 关键方法说明
    1. `compareTo()` 方法
    作用：定义比较规则（比较哪个成员变量）
    传入：被比较的元素（该数据结构**里的某个元素的引用）**
    返回：正/负/零  类型的数值
    注意：该方法只需要定义，无需手动调用，比较算法有关方法会自动在其内部调用。
    使用：定义时在参数列表创建一个与被比较对象相同类型的局部变量，用于接收比较的对象，重写时可以使用减法来实现一个最简单的正负输出逻辑，调用时由排序算法自动调用（无需手动调用）

    1. 排序算法（比较算法）
    以`sort`方法为例↓（自然排序）
    作用：直接在原对象基础上重新排序
    传入：待排序的数据结构的对象（如数组）
    返回：不会返回值，而是直接在原对象上做修改
    使用：无需重写定义，在调用时传入待排序的数据结构的对象

    # Comparator接口
    ### 作用：
    Comparator也是一个比较器，但它适用于无法在数据结构实现类中实现`Comparable`接口及重写`compareTo()`方法的情况（代码不开源，无权限等）
    这是一个外挂的比较器，而非`Comparable`接口那种将比较能力嵌入原类中
    ### 工作原理
    1. 由于无法修改原类，因此单独定义一个比较器类，该类实现Comparator接口并重写`compare()`方法
    1. 在使用时调用排序算法（sort等方法）
    1. 排序方法会在其内部调用compare() 方法并直接在原有对象的基础上进行排序
    ```java
//原始类定义
class Person {
    String name; 
    int age;
    // 注意：没实现 Comparable！
}
    ```
    ```java
// 单独写的比较器类定义
class AgeComparator implements Comparator<Person> {
    @Override
    public int compare(Person p1, Person p2) {
        return p1.age-p2.age;   
    }
}
    ```
    ```java
// 调用
Person[] persons = {...};
Arrays.sort(persons, new AgeComparator());
    ```
    ### 关键方法说明
    1. compare()方法
    作用：定义比较规则（比较哪个成员变量）（外挂版）
    传入：被比较的元素和比较的元素o1和o2（由于不能像compareTo方法嵌入原类，因此需要显示声明两个元素，且无法用“this”）
    返回：正/负/零  类型的数值
    注意：该方法只需要定义，无需手动调用，比较算法有关方法会自动在其内部调用。
    使用：定义时在参数列表创建一个与被比较对象相同类型的局部变量，用于接收比较的对象，重写时可以使用减法来实现一个最简单的正负输出逻辑，调用时由排序算法自动调用（无需手动调用）

    1. 排序算法（比较算法）
    以`sort`方法为例↓（自然排序）
    作用：直接在原对象基础上重新排序
    传入：待排序的数据结构的对象（如数组）
    返回：不会返回值，而是直接在原对象上做修改
    使用：无需重写定义，在调用时传入待排序的数据结构的对象
  Collections工具类
    我们知道，集合框架的设计分为三层：接口（定义行为），实现类（实现接口），通用算法（将实现类组合起来，做成一些常用算法）
    **java.util.Collections** 就是第三层，Java集合框架的通用算法

    PS：我们前面提到的自然排序**`sort()`**方法就是由**`Collections`**类定义

    ## 常用的集合算法(方法)：
    | 算法分类 | 方法名 | 功能描述 |
    | --- | --- | --- |
    | 排序 | sort() | 对 List 进行升序排序 |
    | 混排 | shuffle() | 随机打乱 List 中元素的顺序 |
    | 反转 | reverse() | 反转 List 中元素的顺序 |
    | 二分查找 | binarySearch() | 在有序 List 中二分查找指定元素 |
    | 填充 | fill() | 用指定元素替换 List 中的所有元素 |
    | 复制 | copy() | 将一个 List 的元素复制到另一个 List |
    | 最大/最小值 | max() / min() | 返回集合中的最大或最小元素 |
    | 统计频次 | frequency() | 返回指定元素在集合中出现的次数 |
    | 不相交判断 | disjoint() | 判断两个集合是否有公共元素 |
    | 不可变集合 | unmodifiableXxx() | 返回集合的只读视图 |
    | 线程安全 | synchronizedXxx() | 返回线程安全的集合包装 |
    上一节我们已经以sort() 方法为例演示了集合框架通用算法的调用，其他方法的使用都与之类似，**作为开发者只需要关心方法传入什么，返回什么即可**
    用的时候查，不详细说了
  集合工厂方法（jdk9）
    # 作用
    集合工厂方法是用于快速创建内容固定（不可变）且只读的数据结构
    # 特性
    - 集合工厂方法是静态方法，它们定义在`List`、`Set`、`Map` 接口内部
    - 用集合工厂方法创建的数据结构内容不可变，只能读不能写
    # 对比
    使用传统方式创建集合
    ```java
//先创建集合对象
List<String> list = new ArrayList<>();
//再调用add方法添加内容
list.add("a");
list.add("b");
list.add("c");
    ```
    使用集合工厂方法
    ```java
List<String> list = List.of("a", "b", "c");  
// 一行写完
    ```
    # 使用
    有三种工厂方法：
    ### **1️⃣ ****`List.of()`**** / ****`Set.of()`**** / ****`Map.of()`**** —— 直接创建**
    作用：直接创建不可变集合
    使用：直接调用方法即可，别忘了这几个of方法不在List/Set/Map接口的实现类里，而是作为静态方法定义在接口内，所以直接`接口.of()`调用
    传入：直接将集合元素作为参数传入
    调用：方法和普通集合一样
    ```java
List<String> list = List.of("a", "b", "c");
Set<Integer> set = Set.of(1, 2, 3);
Map<String, Integer> map = Map.of("apple", 1, "banana", 2);
    ```
    原理：为了加快创建速度，List/Set/Map 下有10个静态方法of()的重载（不用创建对象，元素直接作为参数传入）
    注意⚠️：
    - Map.of()方法最多传入10个元素，而List.of()和Set.of()则没有这个限制
    - 不能传入空元素nul
    ### **2️⃣ ****`Map.entry()`**** +**`Map.ofEntries()`**—— 构造不可变键值对**
    当Map集合超过了10个键值对就不能使用**`Map.of()`**方法，而需要使用**`Map.entry()`**** **方法
    ```java
Map<String, Integer> map = Map.ofEntries(
    Map.entry("apple", 1),
    Map.entry("banana", 2),
    Map.entry("cherry", 3),
    Map.entry("date", 4),
    Map.entry("elderberry", 5)
    // ...任意多对，没有数量上限
);

    ```
    注意⚠️：
    - 只有Map接口有**`entry()`**方法，List/Set接口没有该方法
    - **`Map.entry()`**** 和**`Map.ofEntries()` 是搭配使用的，两个方法都不能单独使用
    调用：方法和普通集合一样

    ### **3️⃣ ****`List.copyOf()`**** / ****`Set.copyOf()`**** / ****`Map.copyOf()`**** —— 拷贝转换（jdk10）**
    作用：传入一个已有集合，返回一个它的不可变的拷贝
    ```java
//已创建集合
List<String> mutable = new ArrayList<>(List.of("a", "b", "c"));
    ```
    ```java
//拷贝已有集合
List<String> snapshot = List.copyOf(mutable);
    ```
    调用：方法和普通集合一样
  有序集合功能规范（jdk21）
    先来解释一下什么是有序类：
    Java中的有序类指按照元素的值来决定在数据结构中的位置（如二叉树），而不是由放入的顺序决定在数据结构中的位置（如数组，队列）
    # 是什么
    **有序集合功能规范**是一系列有序集合接口及其扩展的统称（`SequencedCollection`、`SequencedSet`和`SequencedMap`这三个接口的统称）
    Java21后jdk的集合框架的接口层的继承被修改了：主要是新增了`SequencedCollection`、`SequencedSet`和`SequencedMap`接口
    在代码上的体现就是Java21后接口继承层级发生的改变
    ```mermaid
graph LR
    subgraph "改造前"
    Collection --> List
    Collection --> Deque
    Set --> SortedSet
    Map --> SortedMap
    end
    subgraph "改造后（JDK 21+）"
    Collection2[Collection] --> SequencedCollection
    SequencedCollection --> List2[List]
    SequencedCollection --> Deque2[Deque]
    Set2[Set] --> SortedSet2[SortedSet]
    SortedSet2 --> SequencedSet2["SequencedSet<br/>(也继承 SequencedCollection)"]
    Map2[Map] --> SortedMap2[SortedMap]
    SortedMap2 --> SequencedMap2[SequencedMap]
    end
    ```
    # 意义
    统一有序集合的方法
    jdk21前：各家的“首尾操作”是割裂的，`LinkedList` 有 `addFirst`（来自 Deque），`List` 却只有 `add(0, e)`；`SortedSet` 有 `first()`，`Deque` 有 `getFirst()`，`LinkedHashMap` 什么都没有（相同操作不同方法）
    jdk21后：三个接口统一了6个方法↓
    | **方法** | **契约** |
    | --- | --- |
    | `addFirst(e)` | 在顺序最前端插入 |
    | `addLast(e)` | 在顺序末尾插入 |
    | `getFirst()` | 返回首元素，**空集合抛 ****`NoSuchElementException`** |
    | `getLast()` | 返回末元素，同上 |
    | `removeFirst()` | 移除并返回首元素，同上 |
    | `removeLast()` | 移除并返回末元素，同上 |

    # 三个接口作用
    ### **SequencedCollection：统一6个方法**
    它直接继承 `Collection`，是整个规范的发起点，定义了“遇见顺序”的判定标准和 7 个核心方法
    ```java
interface SequencedCollection<E> extends Collection<E> {
    SequencedCollection<E> reversed();
    void addFirst(E e);
    void addLast(E e);
    E getFirst();
    E getLast();
    E removeFirst();
    E removeLast();
}

    ```
    ps：遇见顺序就是有序类的概念
    ### **SequencedSet：语义上的东西，不用在意**
    ### **SequencedMap：Map类型独立统一了6个方法**
    因为Map类型无法复用**SequencedCollection接口的，所以重新定义一遍**
    # 有什么影响
    没什么影响，只在集合框架的接口层修改，没有改动实现层一行代码
    但三个接口统一了原本割裂零碎的方法，解决了相同操作在不同集合下有不同方法的混乱局面
    # Q&A
    Q：那既然有序类有功能规范，像Link这样的由插入顺序而非元素决定位置的有没有功能规范
    A：很遗憾，没这东西，这也是逻辑不对称的地方，这东西其实是一个补丁，由于有序类的接口分散在各处，Java使用这个东西将他们组织起来
  (Java 8) Stream流
    # 说在最前面
    **本节围绕“流水线”这一核心思想展开**，`Stream`也是为了引入“流水线”这一概念诞生的
    注意⚠️：Stream流不隶属于`java.io`包，而是在`java.utli`包下
    # 流水线是什么
    在Java集合框架中，想操作集合中的元素，传统的办法是：遍历所有元素后操作。如果有多步操作则需要进行多次遍历（每一步都遍历集合中所有元素）（整个集合为单位跑一遍流程）
    ![](assets/3f75a2dd-8276-8066-a675-ff0bc75ba735.webp)
    ```java
public static void main(String[] args) {
  	//定义一个集合
    List<String> list = new ArrayList<>();
    list.add("A");
    list.add("B");
    list.add("C");
  
  	//移除为B的元素（第一步）
  	Iterator<String> iterator = list.iterator();
    while (iterator.hasNext()){
        if(iterator.next().equals("B")) iterator.remove();
    }
  
  	//移除为A的元素（第二步）
   iterator = list.iterator();
    while (iterator.hasNext()){
        if(iterator.next().equals("A")) iterator.remove();
    }
    
  
	  //打印结果
	  System.out.println(list);
}
    ```
    而流水线思想是：每个元素单独跑一遍流程（中途淘汰的元素，后面的步骤不再遍历）
    ```java
                 ┌──────────────────────────────────────────────┐
   Source        │   1    2    3    4    5    6    7    8       │   List<Integer>
                 └──────────────────────┬───────────────────────┘
                                        │
                                        v
                 ┌──────────────────────────────────────────────┐
  Creation       │                 .stream()                    │   Stream<Integer>
                 └─┬────┬────┬────┬────┬────┬────┬────┬────────┘
                   │1   │2   │3   │4   │5   │6   │7   │8
                   v    v    v    v    v    v    v    v
                 ┌──────────────────────────────────────────────┐
Intermediate     │        .filter(n -> n % 2 == 0)              │   Stream<Integer>
                 └─────┬─────────┬─────────┬─────────┬──────────┘
                       │2        │4        │6        │8
                       v         v         v         v
                 ┌──────────────────────────────────────────────┐
Intermediate     │        .map(n -> n * n)                      │   Stream<Integer>
                 └─────┬─────────┬─────────┬─────────┬──────────┘
                       │4        │16       │36       │64
                       v         v         v         v
                 ┌──────────────────────────────────────────────┐
Intermediate     │        .sorted()                             │   Stream<Integer>
 (stateful)      └──────────────────────┬───────────────────────┘
                                        │4    16    36    64
                                        v
                 ┌──────────────────────────────────────────────┐
Intermediate     │        .skip(1)                              │   Stream<Integer>
 (stateful)      └──────────────────────┬───────────────────────┘
                                        │16   36    64
                                        v
                 ┌──────────────────────────────────────────────┐
  Terminal       │        .forEach(System.out::println)         │   void
                 │        打印: 16  36  64                       │
                 └──────────────────────────────────────────────┘

    ```
    ```java
public static void main(String[] args) {
  	//定义一个集合
    List<String> list = new ArrayList<>();
    list.add("A");
    list.add("B");
    list.add("C");
  
  	//使用流水线处理
    list = list     
            .stream()    //获取流
            .filter(e -> !e.equals("B"))   //只允许所有不是B的元素通过流水线
	            .filter(e -> !e.equals("A")) //只允许所有不是A的元素通过流水线
            .collect(Collectors.toList());   //将流水线中的元素重新收集起来，变回List
    System.out.println(list);
}
    ```
    # **Stream接口**
    `java.util.stream.Stream` 是一个**接口**
    实现类：各集合的实现类均实现了该接口
    作用：为Java引入流水线能力，该接口还定义了多种集合操作方法
    ### 关键方法：
    获取流**「写在链式调用的最前面」**
    - **`stream()`****方法：获取流**
    - parallelStream()方法：获取并行流「写在链式调用的最前面」
    终止流**「写在链式调用的最后」（触发执行）**
    - **`collect()`****方法：终止操作**
    - …
    中间操作
    - **`filter()`**方法：过滤掉指定元素
    - ** ****`map()`**方法：转换元素类型
    - **`sorted()`**方法：对元素排序
    - **`distinct()`**方法：去除重复元素
    - ….
    ### 使用方法
    将链式调用的结果赋值给原对象：先调用**`stream()`**方法获取流，接着调用中间操作方法操作集合，最后调用**`collect()`**方法终止流并触发执行
    例子：
    ```java
public static void main(String[] args) {
  	//定义一个集合
    List<String> list = new ArrayList<>();
    list.add("A");
    list.add("B");
    list.add("C");
  
  	//使用流水线处理
    list = list     
            .stream()    //获取流
            .filter(e -> !e.equals("B"))   //只允许所有不是B的元素通过流水线
	          .filter(e -> !e.equals("A")) //只允许所有不是A的元素通过流水线
            .collect(Collectors.toList());   //将流水线中的元素重新收集起来，变回List
    System.out.println(list);
}
    ```
    # 注意
    - 中间操作的方法允许传入Lambda表达式
    - 流水线是惰性执行，只有读到终止流的方法才会触发执行
    - 使用流水线相比于普通迭代器遍历在大量数据时更加节省内存（省去了重复遍历的内存开销）
    - 对于多线程的意义[https://www.icloud.com.cn/freeform/0b2aRciYqgZ7dF1xdfbels1Dg](https://www.icloud.com.cn/freeform/0b2aRciYqgZ7dF1xdfbels1Dg)
  (Java 9/11/16) Stream增强方法
    由于jdk8推出的Stream流很实用，因此jdk9/11/16再次扩展了Stream流的功能
    # jdk9
    新增方法：
    ### **takeWhile() 取前缀**
    - 功能：对流进行截取
    - 传入参数：“谓词”，也就是判断条件
    - 返回：截取后的流
    - 工作原理：从流的第一个元素开始，根据传入的判断条件判断是否符合，一旦读到不符合的元素，立即截断流，并返回前面的所有元素（不包含截断处的元素）
    名词解释：
    前缀➡️就是截断位置前的所有元素
    谓词➡️就是判断条件，使用Lambda表达式
    例：
    ```java
//创建集合
List<Integer> nums = List.of(1, 2, 3, 7, 8, 4, 5, 9);

		//获取流 
nums.stream()
		//取前缀
		.takeWhile(n -> n < 3)
		//结束流
    .forEach(System.out::print);  // 输出: 12
    ```
    ### **dropWhile()** 去前缀
    - 功能：对流进行截取
    - 传入参数：“谓词”，也就是判断条件
    - 返回：截取后的流
    - 工作原理：从流的第一个元素开始，根据传入的判断条件判断是否符合，一旦读到不符合的元素，立即截断流，并返回后面的所有元素（不包含截断处的元素）
    名词解释：
    前缀➡️就是截断位置前的所有元素
    谓词➡️就是判断条件，使用Lambda表达式
    例：
    ```java
//创建集合
List<Integer> nums = List.of(1, 2, 3, 7, 8, 4, 5, 9);

		//获取流
nums.stream()
		//去前缀
		.dropWhile(n -> n < 3)
		//结束流
    .forEach(System.out::print);  // 输出: 78459

    ```
    ### **iterate() 方法扩展**
    - 功能：用来生成流的方法（不是获取流）
    - 工作原理：根据传入的种子和迭代算法，通过与上一个元素计算生成下一个元素
    - 传入（Java8）：传入两个参数（初始值，迭代函数）
    - 传入（Java9）：传入三个参数（初始值，终止条件，迭代函数）
    - 返回：生成的流
    - 注意⚠️：由于生成流时还没有流，因此链式调用中不是先调用获取流的方法，而是直接调用生成流的方法
    例：
    ```java
//Java8
			 //生成流
Stream.iterate(1, n -> n * 2)
			 //截断流（否则会无限生成）   
      .limit(5)  
       //结束流              
      .forEach(System.out::print);  // 1 2 4 8 16

    ```
    ```java
//Java9
			//生成流
Stream.iterate(1, n -> n < 100, n -> n * 2)
			//结束流
      .forEach(System.out::println);
// 1 2 4 8 16 32 64
    ```
    ### **ofNullable()**
    - 功能：**把“可能为 null 的引用”安全地转换成流（防止空指针异常）**
    - 工作原理：值为 null 时返回空流，值非 null 时返回单元素流
    - 传入：待转换成流的引用
    - 返回：流
    例：
    ```java
Stream.ofNullable("hello")  // 返回流hello
Stream.ofNullable(null)     // 返回空流
    ```
    # jdk11
    新增方法:
    ### Predicate.not()
    非 Stream 接口的方法，而是 `java.util.function.Predicate` 的静态方法
    - 功能：给传入的谓词取反
    - 工作原理：将一个谓词作为参数传入，返回它的取反谓词
    - 传入：待取反谓词
    - 返回：取反谓词
    - 存在意义：Lambda表达式可以不用这种而是直接在执行的操作前挂一个！来取反，但如果是一个写好的取反类的对象则不支持！取反，这时`Predicate.not()`就派上用场了
    例：
    ```java
// Java 11：方法引用保留，语义清晰
//可以给引用使用
list.stream().filter(Predicate.not(String::isBlank));
//也可以给Lambda表达式使用
list.removeIf(Predicate.not(s -> s.startsWith("WARN")));
    ```
    # jdk16
    新增方法:
    ### **toList()**
    - 功能：**把流中的元素直接收集为一个不可变 List**
    - 工作原理：不用传参，在链式调用中调用该方法即将流转换成List
    - 传入：不用传参，该方法是空参调用的
    - 返回：一个List
    例：
    ```java
// 直接调用即可，括号里什么都不填
List<String> result = stream.map(String::toUpperCase)
														.toList();
    ```
    ### **mapMulti()**
    - 功能：**把每个元素替换为零个或多个元素**
    - 工作原理：传入一个Lambda声明替换规则，按该规则替换后返回
    - 传入：一个Lambda表达式，该Lambda表达式有两个形参（当前流元素类型，输出类型），通过在Lambda中控制调用`输出类型.accept（替换内容）`的次数来控制入元素的数量
    例
    ```java
			//调用替换方法
stream.mapMulti((element, downstream) -> {
    downstream.accept(结果1);   // 将结果1替换全部元素
    downstream.accept(结果2);   // 将结果2替换全部元素（不覆盖结果1）
});

    ```
    可以发现这种方法可以实现所有元素多对一替换
  （Java24）流汇聚器Gatherers「暂时跳过」
    暂时跳过，这个是Java24的新特性，截止26-10-14Java24 仍是最新版，没有应用场景，兼容性不行
[Java IO](java-io/index.md)
  本章节讲Java I/O框架，我们知道，读写硬盘等IO操作需要使用系统调用，而不同操作系统的调用方式不同，而Java则通过Java IO框架屏蔽了这种差异，实现了：一套代码到处运行
  **JavaIO框架核心是通过流来操作IO数据的**
  注意⚠️：前面学的Stream流不隶属于`java.io`包，且特性/方法也是不一样的
  这章的类型只分两种：字节流和字符流
  本章所有流都源自**4 个抽象基类**（注意不是前两节的4个类）（后面的流都是在这4个类上进行了包装）
  | **流类型** | **顶级基类** | **核心方法** | **处理单位** |
  | --- | --- | --- | --- |
  | 字节输入流 | `InputStream` | `read()` | byte（8 位） |
  | 字节输出流 | `OutputStream` | `write(int b)` | byte（8 位） |
  | 字符输入流 | `Reader` | `read(char[] cbuf)` | char（16 位） |
  | 字符输出流 | `Writer` | `write(String str)` | char（16 位） |
  文件字节流
    本节的核心是FileInputStream类及**FileOutputStream类**，下面围绕该类进行展开
    # FileInputStream类（文件字节输入流）
    来历：FileInputStream是`InputStream` 的具体实现类，位于 `java.io` 包中
    作用：用于获取文件的字节流（把硬盘上的一个文件，以**字节**为单位读取到程序内存中）（输入文件到流）
    ### 常用方法
    构造方法（创建FileInputStream类的对象时支持的传入参数）：
    ```java
FileInputStream(File file)          
// 通过 File 对象创建
FileInputStream(String name)        
// 通过文件路径名创建
FileInputStream(FileDescriptor fdObj) 
// 通过文件描述符创建
    ```
    读取方法：
    | 方法 | 功能 | 传入 | 返回 |
    | --- | --- | --- | --- |
    | **read()** | 一次读取一个字节，下次调用读取下一个，读到末尾返回-1 | 空参调用 | 读到的那个字节值，读到末尾返回-1 |
    | **read(byte[] b)** | 一次读多个字节，将读到的值放入传入的数组中，每次读都从数组的0下标覆盖写入 | 传入一个数组 | 读到的字节数，读到的值放到了数组中，读到末尾返回-1 |
    | **int read(byte[] b, int off, int len)** | 依旧将数据存到数组中，不过可以控制存放位置、读取量 | 数组（存放读到的数据），起始下标，读取字节 | 读到的字节数，读到的值放到了数组中，读到末尾返回-1 |
    | 方法 | 功能 | 传入 | 返回 |
    | --- | --- | --- | --- |
    | **skip(n)** | 跳过并丢弃 n 个字节的数据 | 跳过字节数 | 字节流 |
    | **available()** | 返回剩余可读取（不受阻塞）的字节估计数 | 空 | 字节数 |
    | **Descriptor getFD()** | 获取文件描述符对象。 | 空 | 对象 |
    | 方法 | 功能 | 传入 | 返回 |
    | --- | --- | --- | --- |
    | **close()** | 关闭流并释放系统资源（**使用完必须调用）** | 空 | 无 |
    ### 使用方法
    需要导入`java.io`包
    1. 创建FileInputStream类的对象以创建流
    ```java
FileInputStream fis = new FileInputStream("路径");
//将文件路径作为参数传入以明确要读取哪个文件
    ```
    1. 调用read() 方法读取流（以**int read(byte[] b, int off, int len)**签名的方法为例）
    ```java
byte[] buffer = new byte[1024];
int len = fis.read(buffer, 0, 512); // 最多读512字节存入buffer
    ```
    1. 关闭流并释放系统资源
    ```java
fis.close();
    ```
    ### 注意
    IO操作可能受很多因素影响导致抛异常（文件被占用，硬盘正忙），因此需要捕获异常（使用try catch捕获异常）
    可以空处理/打印堆栈/稍后重试
    ```java
public static void main(String[] args) {
    try {   
		    //注意，IO相关操作会有很多影响因素，有可能出现异常，所以需要明确进行处理
        FileInputStream inputStream = new FileInputStream("路径");
        //路径支持相对路径和绝对路径
    } catch (FileNotFoundException e) {
		    //打印异常堆栈
        e.printStackTrace();
    }
}
    ```
    # **FileOutputStream类（文件字节输出流）**
    来历：FileOutputStream是`OutputStream`的具体实现类，位于`java.io`包中
    作用：用于将程序中的字节写入文件（把内存中的数据，以**字节**为单位写入硬盘上的文件）（从流中输出）
    ### 常用方法
    构造方法（创建FileOutputStream类的对象时支持的传入参数）：
    ```java
FileOutputStream(File file)
// 通过 File 对象创建，默认覆盖文件原有内容
FileOutputStream(String name)
// 通过文件路径名创建，默认覆盖文件原有内容
FileOutputStream(File file, boolean append)
// 通过 File 对象创建，可指定是否追加写入
FileOutputStream(String name, boolean append)
// 通过文件路径名创建，可指定是否追加写入
FileOutputStream(FileDescriptor fdObj)
// 通过文件描述符创建
    ```
    写入方法：（跟字节输入流差不多）
    | 方法 | 功能 | 传入 | 返回 |
    | --- | --- | --- | --- |
    | **write(int b)** | 写入一个字节（一次只写入参数的前 8 位，超出部分会被忽略） | 字符/数字/十六进制 | 无 |
    | **write(byte[] b)** | 将数组中的所有字节写入文件 | 一个字节数组 | 无 |
    | **write(byte[] b, int off, int len)** | 将数组中从 `off` 开始的 `len` 个字节写入文件 | 字节数组、起始下标、写入字节数 | 无 |
    | **flush()** | 刷新输出流，使待写数据提交到底层输出目标 | 空 | 无 |
    | **close()** | 关闭流并释放系统资源（使用完必须调用） | 空 | 无 |
    ### 使用方法
    需要导入`java.io`包
    1. 创建FileOutputStream类的对象以创建流
    ```java
FileOutputStream fos = new FileOutputStream("路径");
// 将文件路径作为参数传入，以明确要写入哪个文件
    ```
    1. 调用write()方法写入字节（以`write(byte[] b)`为例）
    ```java
byte[] data = {65, 66, 67};
fos.write(data); // 将数组中的字节写入文件
    ```
    1. 关闭流并释放系统资源
    ```java
fos.close();
    ```
    ### 注意
    IO操作可能受很多因素影响导致抛异常（路径不存在、文件无法创建、磁盘正忙等），因此需要捕获异常（使用try catch捕获异常）
    异常可以空处理/打印堆栈/稍后重试；
    默认创建FileOutputStream时，如果目标文件已经存在，会先清空原有内容再写入；如果需要保留原内容并在末尾追加，应使用带`append`参数的构造方法，并将其设为`true`
    FileOutputStream写入的是字节，不是字符；写入文本时需要先按指定字符集将字符串转换为字节
    ```java
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.charset.StandardCharsets;

public static void main(String[] args) {
    try (FileOutputStream outputStream = new FileOutputStream("路径")) {
        // 路径支持相对路径和绝对路径
        byte[] data = "示例文本".getBytes(StandardCharsets.UTF_8);
        outputStream.write(data);
    } catch (IOException e) {
        // 打印异常堆栈
        e.printStackTrace();
    }
}
    ```
  文件字符流
    这个跟上一节差不多
    文件字符流主要由两个类构成：**FileReader（文件字符输入流）**、**FileWriter（文件字符输出流）**。下面围绕这两个类展开。
    # FileReader 类（文件字符输入流）
    继承关系：继承自 `InputStreamReader`，位于 `java.io` 包中；它会把文件中的字节按指定字符集解码为字符。
    作用：获取文件的字符流（把硬盘上的文件，以字符为单位读取到程序内存中）。适合读取文本文件；读取图片、音频等二进制文件应使用字节流（输入文件到流）
    ### 常用方法
    构造方法（创建 `FileReader` 对象时支持的传入参数）：
    ```java
FileReader(File file)
// 通过 File 对象创建，使用平台默认字符集
FileReader(String fileName)
// 通过文件路径名创建，使用平台默认字符集
FileReader(FileDescriptor fd)
// 通过文件描述符创建
FileReader(File file, Charset charset)
// 通过 File 对象创建，并指定字符集（Java 11+）
FileReader(String fileName, Charset charset)
// 通过文件路径名创建，并指定字符集（Java 11+）
    ```
    读取方法：
    | 方法 | 功能 | 传入 | 返回 |
    | --- | --- | --- | --- |
    | **read()** | 一次读取一个字符；读到末尾返回 `-1` | 空参调用 | 读到的字符值（`int`），末尾返回 `-1` |
    | **read(char[] cbuf)** | 将字符读入字符数组，从数组下标 `0` 开始覆盖写入 | 字符数组 | 实际读取的字符数，末尾返回 `-1` |
    | **read(char[] cbuf, int off, int len)** | 将字符读入数组，可指定存放位置和最多读取的字符数 | 字符数组、起始下标、最多读取长度 | 实际读取的字符数，末尾返回 `-1` |
    其他常用方法：
    | 方法 | 功能 | 传入 | 返回 |
    | --- | --- | --- | --- |
    | **skip(long n)** | 跳过并丢弃 `n` 个字符 | 要跳过的字符数 | 实际跳过的字符数 |
    | **ready()** | 判断下一次读取是否可以保证不阻塞 | 空 | `true` 或 `false` |
    | **getEncoding()** | 获取当前使用的字符编码名称 | 空 | 编码名称；若流已关闭则可能为 `null` |
    | **close()** | 关闭流并释放系统资源（使用完必须调用） | 空 | 无 |
    ### 使用方法
    需要导入 `java.io` 包。读取文本时，建议明确指定字符集，避免文件编码与平台默认字符集不一致而出现乱码。
    1. 创建 `FileReader` 对象以创建流
    ```java
FileReader reader = new FileReader("路径", StandardCharsets.UTF_8);
// 将文件路径和字符集作为参数传入
    ```
    1. 调用 `read()` 方法读取字符（以字符数组批量读取为例）
    ```java
char[] buffer = new char[1024];
int len = reader.read(buffer, 0, buffer.length); // 最多读取 1024 个字符
    ```
    1. 关闭流并释放系统资源
    ```java
reader.close();
    ```
    ### 注意
    IO 操作可能受文件不存在、文件被占用、磁盘异常等因素影响而抛出异常，因此需要处理 `IOException`。推荐使用 `try-with-resources`，让流在代码块结束时自动关闭。
    ```java
import java.io.FileReader;
import java.io.IOException;
import java.nio.charset.StandardCharsets;

public static void main(String[] args) {
    try (FileReader reader = new FileReader("路径", StandardCharsets.UTF_8)) {
        char[] buffer = new char[1024];
        int len;
        while ((len = reader.read(buffer)) != -1) {
            System.out.print(new String(buffer, 0, len));
        }
    } catch (IOException e) {
        e.printStackTrace();
    }
}
    ```
    `read()` 的返回类型是 `int`，这样可以用 `-1` 表示文件末尾；读到字符时返回其字符值。Java 的 `char` 表示 UTF-16 代码单元，因此一个补充字符可能由两个 `char` 组成。
    # FileWriter 类（文件字符输出流）
    继承关系：继承自 `OutputStreamWriter`，位于 `java.io` 包中；它会把程序中的字符按指定字符集编码为字节，再写入文件。
    作用：用于将程序中的字符写入文本文件（把内存中的字符数据写入硬盘上的文件）（从流中输出文件）
    ### 常用方法
    构造方法（创建 `FileWriter` 对象时支持的传入参数）：
    ```java
FileWriter(File file)
// 通过 File 对象创建，使用平台默认字符集；默认覆盖原内容
FileWriter(String fileName)
// 通过文件路径名创建，使用平台默认字符集；默认覆盖原内容
FileWriter(File file, boolean append)
// 通过 File 对象创建，可指定是否追加；使用平台默认字符集
FileWriter(String fileName, boolean append)
// 通过文件路径名创建，可指定是否追加；使用平台默认字符集
FileWriter(FileDescriptor fd)
// 通过文件描述符创建
FileWriter(File file, Charset charset)
// 指定字符集（Java 11+）
FileWriter(File file, Charset charset, boolean append)
// 指定字符集和是否追加（Java 11+）
FileWriter(String fileName, Charset charset)
// 指定字符集（Java 11+）
FileWriter(String fileName, Charset charset, boolean append)
// 指定字符集和是否追加（Java 11+）
    ```
    写入方法：
    | 方法 | 功能 | 传入 | 返回 |
    | --- | --- | --- | --- |
    | **write(int c)** | 写入一个字符 | 字符值（`int`） | 无 |
    | **write(char[] cbuf)** | 将字符数组中的全部字符写入文件 | 字符数组 | 无 |
    | **write(char[] cbuf, int off, int len)** | 将数组中从 `off` 开始的 `len` 个字符写入文件 | 字符数组、起始下标、字符数 | 无 |
    | **write(String str)** | 将字符串写入文件 | 字符串 | 无 |
    | **write(String str, int off, int len)** | 将字符串中指定范围的字符写入文件 | 字符串、起始下标、字符数 | 无 |
    | **flush()** | 刷新输出流，使缓冲中的数据提交到底层输出目标 | 空 | 无 |
    | **close()** | 关闭流并释放系统资源（使用完必须调用） | 空 | 无 |
    ### 使用方法
    需要导入 `java.io` 包。指定字符集时，需使用 Java 11+ 提供的 `Charset` 构造方法。
    1. 创建 `FileWriter` 对象以创建流
    ```java
FileWriter writer = new FileWriter("路径", StandardCharsets.UTF_8);
// 默认覆盖目标文件原有内容
    ```
    1. 调用 `write()` 方法写入字符
    ```java
writer.write("示例文本");
writer.write("追加到程序缓冲区的字符");
    ```
    1. 刷新并关闭流
    ```java
writer.flush();
writer.close();
    ```
    ### 注意
    IO 操作可能因为路径不存在、文件无法创建、磁盘异常等原因抛出 `IOException`，需要进行异常处理。推荐使用 `try-with-resources`：
    ```java
import java.io.FileWriter;
import java.io.IOException;
import java.nio.charset.StandardCharsets;

public static void main(String[] args) {
    try (FileWriter writer = new FileWriter("路径", StandardCharsets.UTF_8)) {
        writer.write("示例文本");
    } catch (IOException e) {
        e.printStackTrace();
    }
}
    ```
    `FileWriter` 默认使用平台默认字符集；为保证不同环境下文本编码一致，建议显式指定字符集，例如 `StandardCharsets.UTF_8`。Java 18 及之后版本的默认字符集通常为 UTF-8，但显式指定仍更清晰、可靠。
    默认创建 `FileWriter` 时，如果目标文件已存在，会先清空原有内容再写入；若要保留原内容并在末尾追加，应使用带 `append` 参数的构造方法，并将其设为 `true`：
    ```java
try (FileWriter writer = new FileWriter("路径", StandardCharsets.UTF_8, true)) {
    writer.write("追加内容");
}
    ```
    `FileWriter` 写入的是字符，字符会根据所选字符集编码后保存为文件字节；读取时应使用相同字符集，避免乱码。
  (Java 7/8/11) 文件工具类
    Java原生的文件工具类有File，Files，RandomAccessFile
    这里我们只介绍Files类
    # Files类
    归属：依旧是在`java.io`包下
    作用：操作文件的工具类（创建/删除/移动/重命名…）
    注意⚠️：Files类下的所有方法均为静态方法，无需创建对象即可使用（典型的工具类） 
    ### 常用方法
    - 判断方法
    | **方法** | **功能** | **传入参数** | **返回值** |
    | --- | --- | --- | --- |
    | `exists(Path)` | 判断文件或目录是否存在 | `Path`：文件路径 | `boolean`：布尔值 |
    | `notExists(Path)` | 判断文件或目录是否不存在 | `Path`：文件路径 | `boolean`：布尔值 |
    | `isDirectory(Path)` | 判断路径是否为目录 | `Path`：路径 | `boolean`：布尔值 |
    | `isRegularFile(Path)` | 判断路径是否为普通文件 | `Path`：路径 | `boolean`：布尔值 |
    | `isReadable(Path)` | 判断文件是否可读 | `Path`：路径 | `boolean`：布尔值 |
    | `isWritable(Path)` | 判断文件是否可写 | `Path`：路径 | `boolean`：布尔值 |
    | `isExecutable(Path)` | 判断文件是否可执行 | `Path`：路径 | `boolean`：布尔值 |
    | `isHidden(Path)` | 判断文件是否为隐藏文件 | `Path`：路径 | `boolean`：布尔值 |
    | `isSymbolicLink(Path)` | 判断路径是否为符号链接 | `Path`：路径 | `boolean`：布尔值 |
    | `isSameFile(Path, Path)` | 判断两个路径是否指向同一文件 | 两个 `Path` | `boolean`：布尔值 |
    - 创建方法
    | **方法** | **功能** | **传入参数** | **返回值** |
    | --- | --- | --- | --- |
    | `createFile(Path)` | 创建一个新的空文件（父目录必须已存在） | `Path`：新文件路径 | `Path`：创建的文件路径 |
    | `createDirectory(Path)` | 创建单级目录（父目录必须已存在） | `Path`：目录路径 | `Path`：创建的目录路径 |
    | `createDirectories(Path)` | 递归创建多级目录（父目录不存在时自动创建） | `Path`：目录路径 | `Path`：创建的目录路径 |
    | `createTempFile(String, String)` | 在系统临时目录创建临时文件 | 前缀（文件名）、后缀（扩展名） | `Path`：临时文件路径 |
    | `createTempFile(Path, String, String)` | 在指定目录创建临时文件 | 目录、前缀（文件名）、后缀（扩展名） | `Path`：临时文件路径 |
    | `createTempDirectory(String)` | 在系统临时目录创建临时目录 | 文件夹名 | `Path`：临时目录路径 |
    注意⚠️：系统临时目录关机即删
    Windows临时目录路径：C:\Users\用户名\AppData\Local\Temp
    Linux临时目录路径：/tmp
    - 删除方法
    | **方法** | **功能** | **传入参数** | **返回值** |
    | --- | --- | --- | --- |
    | `delete(Path)` | 删除文件或空目录（不存在时抛异常） | `Path`：待删除路径 | `void`（无返回值） |
    | `deleteIfExists(Path)` | 删除文件或空目录（不存在时静默跳过，不抛异常） | `Path`：待删除路径 | `boolean`：布尔值 |
    - 复制/移动方法
    | **方法** | **功能** | **传入参数** | **返回值** |
    | --- | --- | --- | --- |
    | `copy(Path, Path, CopyOption...)` | 复制文件或目录到目标位置 | 源路径、目标路径、选项（如 `REPLACE_EXISTING` 覆盖） | `Path`：目标路径 |
    | `copy(InputStream, Path, CopyOption...)` | 把输入流的内容写入文件（常用于下载保存） | 输入流对象、目标路径、选项 | `long`：复制的字节数 |
    | `copy(Path, OutputStream)` | 把文件内容读出写入输出流 | 源路径、输出流 | `long`：复制的字节数 |
    | `move(Path, Path, CopyOption...)` | 移动文件或重命名 | 源路径、目标路径、选项（如 `ATOMIC_MOVE` 原子移动） | `Path`：目标路径 |
    - 读取方法
    | **方法** | **功能** | **传入参数** | **返回值** |
    | --- | --- | --- | --- |
    | `readAllBytes(Path)` | 一次性读取整个文件的所有字节（仅适合小文件） | `Path`：文件路径 | `byte[]`：全部字节内容 |
    | `readAllLines(Path)` | 一次性读取整个文件的所有行（仅适合小文件） | `Path`：文件路径（默认 UTF-8） | `List<String>`：所有行的列表 |
    | `readAllLines(Path, Charset)` | 一次性读取所有行，并指定编码 | 路径、字符集 | `List<String>`：所有行的列表 |
    | `readString(Path)`（JDK 11+） | 一次性读取整个文本文件为字符串（仅适合小文件） | `Path`：文件路径 | `String`：整个文件内容 |
    | `lines(Path)` | 惰性逐行读取文件（按需加载，适合大文件） | `Path`：文件路径 | `Stream<String>`：行内容流 |
    | `newBufferedReader(Path)` | 打开带缓冲的字符读取流（适合逐行处理大文件） | `Path`：文件路径 | `BufferedReader`：缓冲读取流 |
    | `newInputStream(Path, OpenOption...)` | 打开文件字节输入流 | 路径、打开选项 | `InputStream`：字节输入流 |
    - 写入类
    | **方法** | **功能** | **传入参数** | **返回值** |
    | --- | --- | --- | --- |
    | `write(Path, byte[], OpenOption...)` | 把字节数组写入文件（默认覆盖，可加 `APPEND` 追加） | 路径、字节数组、选项 | `Path`：写入的文件路径 |
    | `write(Path, Iterable<CharSequence>, Charset, OpenOption...)` | 按行把字符串集合写入文件 | 路径、行集合、字符集、选项 | `Path`：写入的文件路径 |
    | `writeString(Path, CharSequence, OpenOption...)`（JDK 11+） | 把字符串写入文件 | 路径、字符串、选项 | `Path`：写入的文件路径 |
    | `newBufferedWriter(Path, OpenOption...)` | 打开带缓冲的字符写入流（适合逐行写出） | 路径、打开选项（如 `APPEND`） | `BufferedWriter`：缓冲写入流 |
    | `newOutputStream(Path, OpenOption...)` | 打开文件字节输出流 | 路径、打开选项 | `OutputStream`：字节输出流 |
    - 遍历方法
    | **方法** | **功能** | **传入参数** | **返回值** |
    | --- | --- | --- | --- |
    | `list(Path)` | 列出目录下的**直接子项**（不递归） | `Path`：目录路径 | `Stream<Path>`：子项流 |
    | `walk(Path)` | 递归遍历整个目录树的所有层级 | `Path`：起始目录 | `Stream<Path>`：所有条目流 |
    | `walk(Path, int)` | 递归遍历目录树，但限制最大深度 | 路径、最大深度 | `Stream<Path>`：限定深度的条目流 |
    | `find(Path, int, BiPredicate)` | 递归查找目录树中满足条件的条目 | 路径、深度、过滤条件（路径+属性 → boolean） | `Stream<Path>`：符合条件的条目流 |
    | `newDirectoryStream(Path)` | 打开目录流，可迭代遍历目录内容 | `Path`：目录路径 | `DirectoryStream<Path>`：可迭代的目录流 |
    - 获取属性方法
    | **方法** | **功能** | **传入参数** | **返回值** |
    | --- | --- | --- | --- |
    | `size(Path)` | 获取文件大小 | `Path`：文件路径 | `long`：文件大小（字节） |
    | `getLastModifiedTime(Path)` | 获取文件最后修改时间 | `Path`：文件路径 | `FileTime`：修改时间对象 |
    | `setLastModifiedTime(Path, FileTime)` | 设置文件最后修改时间 | 路径、时间对象 | `Path`：文件路径 |
    | `getOwner(Path)` | 获取文件所有者 | `Path`：文件路径 | `UserPrincipal`：所有者对象 |
    | `readAttributes(Path, Class<T>)` | 一次性读取文件的完整属性（大小、时间、类型等） | 路径、属性类型（如 `BasicFileAttributes.class`） | `T`：属性对象 |
    | `setAttribute(Path, String, Object)` | 设置文件的某个属性（如只读、权限） | 路径、属性名、属性值 | `Path`：文件路径 |
    # Q&A
    Q：前面的章节“文件字节/字符流”不是已经实现了输入/输出的方法了吗？为什么这里又实现一遍？
    A：这里并不是重复实现，这里的输入/输出方法本质还是调用的文件字节/字符流的方法，这里只是为了整合更完善的功能（支持直接编辑而不是先创建流）而做的包装
  缓冲流
    经过前面章节的学习，我们知道文件字节/字符流可以对文件进行读取或写入操作，但不论是文件字符流还是文件字节流，它们都是从直接从硬盘中读取（忽略系统优化）
    缓冲流则是一个~~预读取~~（实际上不是预读取，）操作，它可以提前将文件读取到内存中，这样等获取数据时就无需再从硬盘中读取了
    依旧分为字节缓冲流和字符缓冲流
    # 字节缓冲流
      来源：都在`java.io`包中，且字节缓冲流类都继承自相应的文件字节流类
      ### **BufferedInputStream（缓冲字节输入流）**
      作用：以字节为单位读取文件到内存中
      **构造方法：**
      | 构造方法签名 | 作用 | 传入 |
      | --- | --- | --- |
      | BufferedInputStream(InputStream in) | 创建字节缓冲流对象（默认大小） | 文件字节流对象 |
      | BufferedInputStream(InputStream in, int size)  | 创建字节缓冲流对象（自定义大小） | 文件字节流对象，缓存区大小（单位：字节） |
      ```java
BufferedInputStream(InputStream in)              
// 单参数，默认缓冲区大小 8192 字节，传入文件字节流对象
BufferedInputStream(InputStream in, int size)    
// 2参数，自定义缓冲区大小，传入文件字节流和缓存区大小
      ```
      **常用方法：**
      - 由于字节缓冲流类都继承自相应的文件字节流类，所以继承了文件字节流有的所有方法
      **使用方法：**
      1. 调用构造方法创建缓冲流
      1. 执行文件字节流操作或调用文件工具类
      1. 关闭缓冲流
      ### **BufferedOutputStream（缓冲字节输出流）**
      来历：位于 `java.io` 包中，接收一个 `OutputStream` 作为底层输出流，常用于包装文件字节输出流。
      作用：先将程序中的字节写入内存缓冲区，缓冲区满或调用刷新、关闭操作时，再批量写入底层输出流，以减少直接写入次数。
      **构造方法：**
      | 构造方法签名 | 作用 | 传入 |
      | --- | --- | --- |
      | `BufferedOutputStream(OutputStream out)` | 创建字节缓冲输出流（默认缓冲区大小） | 底层输出流 |
      | `BufferedOutputStream(OutputStream out, int size)` | 创建指定缓冲区大小的字节缓冲输出流 | 底层输出流、缓冲区大小（单位：字节） |
      ```java
BufferedOutputStream(OutputStream out)
// 使用默认大小的缓冲区
BufferedOutputStream(OutputStream out, int size)
// 自定义缓冲区大小，size 单位为字节
      ```
      **常用方法：**
      | 方法 | 功能 | 传入 | 返回 |
      | --- | --- | --- | --- |
      | `write(int b)` | 将一个字节写入缓冲区；缓冲区满时会写入底层输出流 | 一个字节值 | 无 |
      | `write(byte[] b, int off, int len)` | 将字节数组中指定范围的数据写入缓冲区 | 字节数组、起始下标、写入长度 | 无 |
      | `flush()` | 将缓冲区中尚未写出的数据刷新到底层输出流 | 空 | 无 |
      | `close()` | 刷新并关闭流，同时释放系统资源 | 空 | 无 |
      由于它继承了输出流的写入方法，也可以直接调用 `write(byte[] b)` 写入整个字节数组。
      **使用方法：**
      1. 创建底层文件字节输出流，并用缓冲流包装
      1. 调用 `write()` 写入字节
      1. 使用完关闭缓冲流（会自动刷新，并关闭底层流）
      ```java
byte[] data = {65, 66, 67};
try (BufferedOutputStream output = new BufferedOutputStream(
        new FileOutputStream("路径"))) {
    output.write(data);
    // 需要在关闭前确保数据写出时，可调用 output.flush()
} catch (IOException e) {
    e.printStackTrace();
}
      ```
    # 字符缓冲流
      ### **BufferedReader（缓冲字符输入流）**
      来历：位于 `java.io` 包中，接收一个 `Reader` 作为底层字符流，常用于包装 `FileReader`。
      作用：以字符为单位缓冲读取文本内容，并提供按行读取的功能。
      **构造方法：**
      | 构造方法签名 | 作用 | 传入 |
      | --- | --- | --- |
      | `BufferedReader(Reader in)` | 创建字符缓冲输入流（默认缓冲区大小） | 底层字符输入流 |
      | `BufferedReader(Reader in, int size)` | 创建指定缓冲区大小的字符缓冲输入流 | 底层字符输入流、缓冲区大小（单位：字符） |
      ```java
BufferedReader(Reader in)
// 使用默认大小的缓冲区
BufferedReader(Reader in, int size)
// 自定义缓冲区大小，size 表示字符数
      ```
      **常用方法：**
      | 方法 | 功能 | 传入 | 返回 |
      | --- | --- | --- | --- |
      | `read()` | 读取一个字符，读到末尾返回 `-1` | 空参调用 | 字符值（`int`），末尾返回 `-1` |
      | `read(char[] cbuf, int off, int len)` | 将字符读入数组，可指定存放位置和最多读取的字符数 | 字符数组、起始下标、最多读取长度 | 实际读取的字符数，末尾返回 `-1` |
      | `readLine()` | 读取一行文本，不包含行结束符 | 空参调用 | 行内容；读到末尾且没有更多内容时返回 `null` |
      | `ready()` | 判断下一次读取是否可以保证不阻塞 | 空 | `true` 或 `false` |
      | `close()` | 关闭流并释放系统资源 | 空 | 无 |
      **使用方法：**
      需要导入 `java.io` 包。读取文本时应注意字符集；下面示例使用 Java 11+ 的 `FileReader` 字符集构造方法。
      1. 创建 `FileReader`，并用 `BufferedReader` 包装
      1. 调用 `readLine()` 逐行读取，返回 `null` 时表示读完
      1. 使用完关闭缓冲流（底层流也会随之关闭）
      ```java
try (BufferedReader reader = new BufferedReader(
        new FileReader("路径", StandardCharsets.UTF_8))) {
    String line;
    while ((line = reader.readLine()) != null) {
        System.out.println(line);
    }
} catch (IOException e) {
    e.printStackTrace();
}
      ```
      **注意：**
      `readLine()` 会去掉行结束符；如果需要保留换行，应在处理每一行时自行添加。文件字符集应与读取时指定的字符集一致，避免乱码。
      ### **BufferedWriter（缓冲字符输出流）**
      来历：位于 `java.io` 包中，接收一个 `Writer` 作为底层字符流，常用于包装 `FileWriter`。
      作用：先将程序中的字符写入内存缓冲区，再批量写入底层字符输出流；还提供了写入平台适用换行符的方法。
      **构造方法：**
      | 构造方法签名 | 作用 | 传入 |
      | --- | --- | --- |
      | `BufferedWriter(Writer out)` | 创建字符缓冲输出流（默认缓冲区大小） | 底层字符输出流 |
      | `BufferedWriter(Writer out, int size)` | 创建指定缓冲区大小的字符缓冲输出流 | 底层字符输出流、缓冲区大小（单位：字符） |
      ```java
BufferedWriter(Writer out)
// 使用默认大小的缓冲区
BufferedWriter(Writer out, int size)
// 自定义缓冲区大小，size 表示字符数
      ```
      **常用方法：**
      | 方法 | 功能 | 传入 | 返回 |
      | --- | --- | --- | --- |
      | `write(int c)` | 写入一个字符到缓冲区 | 字符值（`int`） | 无 |
      | `write(char[] cbuf, int off, int len)` | 写入字符数组中的指定范围 | 字符数组、起始下标、字符数 | 无 |
      | `write(String str)` | 写入字符串 | 字符串 | 无 |
      | `newLine()` | 写入当前系统适用的换行符 | 空 | 无 |
      | `flush()` | 将缓冲区中的字符刷新到底层输出流 | 空 | 无 |
      | `close()` | 刷新并关闭流，同时释放系统资源 | 空 | 无 |
      **使用方法：**
      1. 创建底层字符输出流，并用缓冲流包装
      1. 调用 `write()` 写入字符或字符串；需要换行时调用 `newLine()`
      1. 使用完关闭缓冲流（会自动刷新，并关闭底层流）
      ```java
try (BufferedWriter writer = new BufferedWriter(
        new FileWriter("路径", StandardCharsets.UTF_8))) {
    writer.write("第一行");
    writer.newLine();
    writer.write("第二行");
} catch (IOException e) {
    e.printStackTrace();
}
      ```
      **注意：**
      `BufferedWriter` 的 `flush()` 可以在流关闭前提交缓冲区中的字符；关闭流时也会先刷新。若要在原文件末尾追加内容，应让底层 `FileWriter` 使用追加模式；默认构造方式会覆盖原有内容。写入文本时应明确并保持字符集一致。
    # 注意
    - 需要澄清一点事实：缓冲流仅优化了多次访问，它仍是读取到缓冲流这行才会运行的，并没有优先运行的能力
    - 字符缓冲流和普通流一样，关闭流内存就释放了（释放缓冲区），它只是提供了一个缓冲能力
  转换流
    转换流相当于文件字节/字符流的一个工具类
    如果想将一个类型的流传入另一个类型的流，传统的做法是遍历内容后写入另一个流
    那有老铁问了：我记得前面讲过转换流类型的方法呀
    这其实是个重大误区：前面有转换流流类型方法的类叫Stream[(Java 8) Stream流](https://app.notion.com/p/3f75a2dd827680bc91aecfd079a2a38c) ，它不隶属于java.io包，而是集合框架的东西，特性和方法完全不同（虽然都是流）
    转换流就是专门用于**字节流和字符流之间相互转换**的
    **（转换流转换的不是元素类型而是流类型）**
    # InputStreamReader类（字节流➡️字符流）
    作用：将字节流转换成字符流
    构造方法：
    ```java
// 1. 使用平台默认字符集
InputStreamReader(InputStream in)

// 2. 使用指定字符集名称（最常用）
InputStreamReader(InputStream in, String charsetName)
    // charsetName 如 "UTF-8"、"GBK"，无效时抛 UnsupportedEncodingException
    ```
    工作原理：传入字节流对象，返回字符流对象，这个类光调用构造方法就够用
    # OutputStreamWriter类（字符流➡️字节流）
    作用：将字符流转换成字节流
    构造方法：
    ```java
// 1. 使用平台默认字符集
OutputStreamWriter(OutputStream out)

// 2. 使用指定字符集名称（最常用）
OutputStreamWriter(OutputStream out, String charsetName)
    // charsetName 如 "UTF-8"、"GBK"，无效时抛 UnsupportedEncodingException

    ```
    工作原理：传入字符流对象，返回字节流对象，这个类光调用构造方法就够用
  打印流
    打印流也是文件字节/字符流的工具类
    分两种类
    # 打印流是干啥的
    我们知道，可以使用文件输出字节/字符流的方法从流中输出内容到文件中，但这会带来一个问题：文件是按字符写入的，而字节输出流是按字节写入的，如果不使用转换流将字节转换成字符，就会出现字节流输出97，写进文件中变成a了（因为 97 是 a 的 ASCII 码）
    因此使用普通输出流输出内容到文件就需要考虑格式转换
    而打印流则提供了方便的输出方法，无需考虑格式转换，必要时会自动转换
    # Q&A
    Q：a存储的是97，97存储的也是97，怎么确保没有歧义的？
    A：对于一般的数据结构，使用数据类型来标记到底是字符还是数字，但如果操作的是流的话，则需要手动处理一下
    Q：打印流只能打印到控制台上吗？
    A：并非，只是叫打印流这个名字，打印到哪里取决于构造时传入的参数（传入文件路径就打印到文件中，传入System.out就打印到控制台）
    # 关于System.out
    我们天天用System.out.println() 那你知道是什么意思吗？
    - System是个类：**Java 给你准备的“系统级工具箱”，提供与运行环境打交道的一堆现成工具。**
    - out是：一个静态变量，JVM启动时会将一个对象引用给它，这个对象就是控制台的输出流
    - 所以，System.out实际是控制台输出流对象，System.out.println() 就是调用这个对象的printlnln()方法
    - System.out是*PrintStream类型的对象*
    # **PrintStream类（字节打印流）**
    继承关系：继承自FilterOutputStream类  文件字节输出流（从流中输出）
    作用：提供简便的打印方法（省去类型转换的步骤）
    构造方法：（决定打印到哪里）（创建流）
    ```java
// 接收文件路径字符串（打印到文件）
PrintStream ps1 = new PrintStream("test.txt");

// 接收 File 对象（打印到文件）
PrintStream ps2 = new PrintStream(new File("test.txt"));

// 接收输出流，可开启自动刷新（打印到输出流/作为输出流的输入）
PrintStream ps3 = new PrintStream(
        new FileOutputStream("test.txt"), true);
    ```
    ```java
//或者直接给**PrintStream类型的变量赋值
//System.out是**控制台输出流对象
//只有System.out可以直接赋值给PrintStream，因为System.out是*PrintStream类型的对象*
PrintStream ps1 = **System.out；**
    ```
    常用方法：
    println()方法
    作用：换行打印，打印位置取决于构造方法
    重载：有多种重载，这确保了它什么数据类型都能打印

    print()方法
    作用：不换行打印，打印位置取决于构造方法
    重载：有多种重载，这确保了它什么数据类型都能打印
    ### 使用方法
    ```java
public static void main(String[] args) {
		//创建对象以获取流
    try(PrintStream stream = new PrintStream("文件路径")){
        // 向文件打印lbwnb
        stream.println("lbwnb");  
    }catch (IOException e){
        
    }
}
    ```
    # **PrintWriter类（字符打印流）**
    继承关系：FilterWriter文件字符输出流（从流中输出）
    和上面一模一样，不写了
  数据流（基本数据类型流）
    与字节/字符流不同，数据流（基本数据类型流）支持以基本数据类型为单位进行读写
    分两个类
    **注意⚠️：基本数据类型流只能作为普通流的包装来使用，不能单独使用**
    # **DataInputStream（输入数据流）**
    继承：**DataInputStream继承自FilterInputStream（文件字节输入流）**
    作用：用于读取数据（按基本数据类型）
    构造方法：
    | **构造方法** | **说明** |
    | --- | --- |
    | `DataInputStream(InputStream in)` | 传入一个DataInputStream类型对象 |
    常用方法：
    除了继承的方法，还有以下方法
    | **方法** | **返回类型** | **说明** | 传入参数 |
    | --- | --- | --- | --- |
    | `readBoolean()` | boolean | 读取 1 个字节，非 0 为 true | 无 |
    | `readByte()` | byte | 读取 1 个有符号字节 | 无 |
    | `readUnsignedByte()` | int | 读取 1 个无符号字节（0~255） | 无 |
    | `readShort()` | short | 读取 2 字节有符号短整数 | 无 |
    | `readUnsignedShort()` | int | 读取 2 字节无符号短整数 | 无 |
    | `readChar()` | char | 读取 2 字节字符 | 无 |
    | `readInt()` | int | 读取 4 字节有符号整数 | 无 |
    | `readLong()` | long | 读取 8 字节长整数 | 无 |
    | `readFloat()` | float | 读取 4 字节浮点数 | 无 |
    | `readDouble()` | double | 读取 8 字节双精度浮点数 | 无 |
    | `readUTF()` | String | 读取改良 UTF-8 编码的字符串 | 无 |
    批量读取
    | **方法** | **说明** | 传入参数 |
    | --- | --- | --- |
    | `read()` | 读取下一个字节 | 无 |
    | `read(byte[] b)` | 读若干字节存入缓冲数组 b | 数组引用 |
    | `read(byte[] b, int off, int len)` | 读最多 len 个字节到 b 的 off 位置起 | 数组引用，起始下标，读字节数 |
    | `readFully(byte[] b)` | **阻塞式**地读满整个 b 数组，否则抛 EOFException | 数组引用 |
    | `readFully(byte[] b, int off, int len)` | 阻塞式读满 len 个字节 | 数组引用，起始下标，读字节数 |
    | `skipBytes(int n)` | 跳过 n 个字节 | 字节数 |
    例子：
    ```java
try {
		DataInputStream dis = new DataInputStream(new FileInputStream("data.bin"));
    dis.readInt();
    dis.readDouble();
    dis.readUTF();
    dis.close();
    }
catch(IOException e){

} 
    ```
    # **DataOutputStream （输出数据流）**
    继承：**DataOutputStream 继承自 FilterOutputStream，并实现 DataOutput 接口**
    作用：用于按基本数据类型将数据写入底层输出流
    构造方法：
    | **构造方法** | **说明** |
    | --- | --- |
    | `DataOutputStream(OutputStream out)` | 传入一个 OutputStream 类型的对象，通常包装文件字节流等普通输出流 |
    常用方法：
    除了继承的方法，还有以下方法
    | **方法** | **说明** | 传入参数 |
    | --- | --- | --- |
    | `writeBoolean(boolean v)` | 写入 1 个字节，true 写为 1，false 写为 0 | 布尔值 |
    | `writeByte(int v)` | 写入 1 个字节（只写低 8 位） | 整数值 |
    | `writeShort(int v)` | 写入 2 个字节（只写低 16 位） | 整数值 |
    | `writeChar(int v)` | 写入 2 个字节的字符 | 字符值 |
    | `writeInt(int v)` | 写入 4 个字节的整数 | 整数值 |
    | `writeLong(long v)` | 写入 8 个字节的长整数 | 长整数值 |
    | `writeFloat(float v)` | 写入 4 个字节的浮点数 | 浮点数值 |
    | `writeDouble(double v)` | 写入 8 个字节的双精度浮点数 | 双精度浮点数值 |
    | `writeBytes(String s)` | 将字符串中每个字符的低 8 位写出；不适合写入一般 Unicode 文本 | 字符串 |
    | `writeChars(String s)` | 将字符串中的每个字符按 2 个字节写出 | 字符串 |
    | `writeUTF(String s)` | 以改良 UTF-8 格式写入字符串，并在前面写入字节长度 | 字符串 |
    批量写入
    | **方法** | **说明** | 传入参数 |
    | --- | --- | --- |
    | `write(int b)` | 写出一个字节（取低 8 位） | 整数值 |
    | `write(byte[] b)` | 将数组中的字节写出 | 字节数组 |
    | `write(byte[] b, int off, int len)` | 将数组从 off 位置开始的 len 个字节写出 | 字节数组，起始下标，写入字节数 |
    | `flush()` | 刷新输出流，将缓冲的数据写到底层流 | 无 |
    | `size()` | 返回目前写出的字节数 | 无 |
    注意：
    - 写入与读取时，数据类型和顺序必须对应；例如先 `writeInt()` 再 `writeDouble()`，读取时也应先 `readInt()` 再 `readDouble()`。
    - `writeUTF()` 写入的是改良 UTF-8 格式，应使用 `DataInputStream.readUTF()` 读取；字符串编码后的长度不能超过 65535 字节。
    - `DataOutputStream` 是普通输出流的包装流，关闭它时也会关闭底层输出流。
    例子：
    ```java
try (DataOutputStream dos =
         new DataOutputStream(new FileOutputStream("data.bin"))) {
    dos.writeInt(100);
    dos.writeDouble(3.14);
    dos.writeUTF("Java");
} catch (IOException e) {
    e.printStackTrace();
}
    ```
  对象流「未审核」
    # 对象流是什么
    对象流用于读写 Java 对象：把对象及其引用关系转换为字节序列，或从字节序列中恢复对象。这个过程分别称为**序列化**和**反序列化**。
    对象流写出的不只是字段值，还包含恢复对象所需的类描述信息和对象引用信息（对象图）；方法的代码不会被序列化。对象流通常包装普通字节流（如文件字节流）使用。
    | 操作 | 使用的类 | 作用 |
    | --- | --- | --- |
    | 序列化 | `ObjectOutputStream` | 将对象写入底层输出流 |
    | 反序列化 | `ObjectInputStream` | 从底层输入流中读取并恢复对象 |
    **注意：**对象流不是 `FilterInputStream` / `FilterOutputStream` 的子类，但构造时都需要传入一个普通输入或输出流。
    # ObjectOutputStream（对象序列化）
    作用：将对象及其对象图写入底层输出流。
    继承与实现：继承自 `OutputStream`，并实现 `ObjectOutput` 接口。
    构造方法：
    | 构造方法 | 说明 |
    | --- | --- |
    | `ObjectOutputStream(OutputStream out)` | 将对象写入指定的输出流；创建时会写入对象流头信息 |
    常用方法：
    | 方法 | 说明 | 传入参数 |
    | --- | --- | --- |
    | `writeObject(Object obj)` | 序列化对象并写出；对象及其可达引用对象也会按规则处理 | 对象引用 |
    | `writeUnshared(Object obj)` | 以非共享方式写出指定对象 | 对象引用 |
    | `reset()` | 重置对象流的共享引用状态，后续写出时不复用之前记录的对象句柄 | 无 |
    | `flush()` | 刷新输出流，将缓冲内容写到底层流 | 无 |
    | `close()` | 关闭对象流及其底层输出流 | 无 |
    `defaultWriteObject()`、`putFields()` 等方法用于类自定义序列化实现，通常在类的 `writeObject` 特殊方法中使用，初学时一般不需要直接调用。
    # ObjectInputStream（对象反序列化）
    作用：从底层输入流读取对象数据，并恢复对象。
    继承与实现：继承自 `InputStream`，并实现 `ObjectInput` 接口。
    构造方法：
    | 构造方法 | 说明 |
    | --- | --- |
    | `ObjectInputStream(InputStream in)` | 从指定输入流读取对象；会读取并校验对象流头信息 |
    常用方法：
    | 方法 | 返回类型 | 说明 | 传入参数 |
    | --- | --- | --- | --- |
    | `readObject()` | `Object` | 读取并恢复一个对象；可能抛出 `ClassNotFoundException` | 无 |
    | `readUnshared()` | `Object` | 以非共享方式读取一个对象 | 无 |
    | `available()` | `int` | 返回可在不阻塞情况下读取的字节数估计值，不代表对象数量 | 无 |
    | `close()` | `void` | 关闭对象流及其底层输入流 | 无 |
    `defaultReadObject()`、`readFields()` 等方法用于类自定义反序列化实现，通常不需要在普通读取代码中直接调用。
    # 使用示例
    对象所属的类需要实现 `Serializable`。它是一个标记接口，不需要实现额外方法。
    ```java
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;

public class ObjectStreamDemo {
    static class Person implements Serializable {
        private static final long serialVersionUID = 1L;

        private String name;
        private int age;

        Person(String name, int age) {
            this.name = name;
            this.age = age;
        }

        @Override
        public String toString() {
            return "Person{name='" + name + "', age=" + age + "}";
        }
    }

    public static void main(String[] args) {
        // 序列化：把对象写入文件
        try (ObjectOutputStream out = new ObjectOutputStream(
                new FileOutputStream("person.dat"))) {
            out.writeObject(new Person("小明", 18));
        } catch (IOException e) {
            e.printStackTrace();
        }

        // 反序列化：从文件恢复对象
        try (ObjectInputStream in = new ObjectInputStream(
                new FileInputStream("person.dat"))) {
            Person person = (Person) in.readObject();
            System.out.println(person);
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
    }
}
    ```
    # 序列化注意事项
    - **类必须支持序列化：**对象的类需要实现 `java.io.Serializable`。如果对象图中包含其他对象，这些对象通常也需要可序列化；否则写出时可能抛出 `NotSerializableException`。不需要保存的字段可考虑声明为 `transient`，或使用自定义序列化逻辑。
    - **静态字段不属于对象实例状态：**`static` 字段不会作为该对象的实例字段被序列化；`transient` 字段也不会按默认规则写出，反序列化后通常为默认值（如 `null`、`0`、`false`）。
    - **声明 `serialVersionUID`：**它用于检查序列化版本兼容性。类的版本不兼容时，反序列化可能抛出 `InvalidClassException`。显式声明可避免仅依赖编译器计算的默认值。
    - **读写顺序要对应：**连续写入多个对象时，读取端应按相同顺序调用 `readObject()`，并将返回的 `Object` 转换为正确类型。
    - **对象引用会被跟踪：**对象流能够保留对象之间的共享引用和循环引用。同一个对象重复写出时，流可能复用已记录的引用；若需要在同一流中重新写出对象的最新状态，可在适当位置调用 `reset()`。
    - **不要反序列化不可信数据：**反序列化可能触发对象构造相关逻辑，带来安全风险；只处理可信来源的数据。
    - 关闭对象流也会关闭它包装的底层流。优先使用 `try-with-resources` 管理资源。
    # 与数据流的区别
    | 对比项 | 对象流 | 数据流 |
    | --- | --- | --- |
    | 主要用途 | 读写对象及其对象引用关系 | 按基本数据类型读写值 |
    | 典型方法 | `writeObject()`、`readObject()` | `writeInt()`、`readInt()`、`writeUTF()`、`readUTF()` |
    | 使用要求 | 对象类需支持序列化 | 读写双方需约定相同的数据类型和顺序 |
    | 常见底层流 | 文件字节流、网络字节流等 | 文件字节流、网络字节流等 |
  字节数组流「未审核」
    # 字节数组流是什么
    字节数组流用 `byte[]` 作为数据来源或存放位置，在内存中读写字节，不直接操作文件。`ByteArrayOutputStream` 把写入的数据暂存在内部缓冲区；`toByteArray()` 可以取出这些数据。`ByteArrayInputStream` 则从已有的字节数组中读取数据。[[1]](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/ByteArrayOutputStream.html) [[2]](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/ByteArrayInputStream.html)
    # 两个核心类
    | 类 | 继承关系 | 作用 |
    | --- | --- | --- |
    | `ByteArrayOutputStream` | `OutputStream` | 把字节写入内存中的字节数组 |
    | `ByteArrayInputStream` | `InputStream` | 从已有的字节数组中读取字节 |
    常用构造方法：
    | 构造方法 | 说明 |
    | --- | --- |
    | `ByteArrayOutputStream()` | 创建一个内存输出流 |
    | `ByteArrayInputStream(byte[] buf)` | 用指定字节数组创建输入流 |
    | `ByteArrayInputStream(byte[] buf, int offset, int length)` | 只读取数组中指定范围的字节 |
    常用方法：
    | 类 | 方法 | 说明 |
    | --- | --- | --- |
    | `ByteArrayOutputStream` | `write(...)` | 把字节写入内存缓冲区 |
    | `ByteArrayOutputStream` | `toByteArray()` | 将已写入的数据复制到一个新的字节数组中 |
    | `ByteArrayOutputStream` | `size()` / `reset()` | 查看当前字节数 / 清空已写入的数据 |
    | `ByteArrayInputStream` | `read()` | 读取一个字节；读到末尾返回 `-1` |
    | `ByteArrayInputStream` | `available()` | 查看还剩多少字节可读 |
    # 使用示例
    下面先把 `A、B、C` 对应的字节写入内存，再从字节数组中读出来：
    ```java
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;

public class ByteArrayStreamDemo {
    public static void main(String[] args) {
        byte[] source = {65, 66, 67}; // ASCII 中分别表示 A、B、C

        // 输出流：把字节写入内存
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        out.write(source, 0, source.length);
        byte[] data = out.toByteArray();

        // 输入流：从字节数组中读取
        ByteArrayInputStream in = new ByteArrayInputStream(data);
        int value;
        while ((value = in.read()) != -1) {
            System.out.print((char) value);
        }
    }
}
    ```
    输出：`ABC`
    # 适用场景与注意事项
    - **适合临时处理内存中的字节数据**，例如先拼接数据，再交给其他流处理。
    - 和 [文件字节流](https://app.notion.com/p/3f95a2dd827680b3b95fc29f692a2525) 不同，它不直接读写磁盘文件；需要保存到文件时，可再把数据写入文件流。
    - 数据都放在内存中，处理特别大的数据时要留意内存占用。`toByteArray()` 会复制一份数据，也会额外占用内存。[[1]](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/ByteArrayOutputStream.html)
    - 这两个字节数组流的 `close()` 不会产生实际影响；它们不负责释放文件等外部资源。[[2]](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/ByteArrayInputStream.html) [[1]](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/ByteArrayOutputStream.html)
    **一句话记忆：**`ByteArrayOutputStream` 往内存里写，`ByteArrayInputStream` 从内存里的字节数组读。
