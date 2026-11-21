---
{
  "id": "3e85a2dd-8276-805b-9d59-cb6db13bc494",
  "url": "https://app.notion.com/p/3e85a2dd8276805b9d59cb6db13bc494",
  "created_time": "2026-09-27T08:09:00.000Z",
  "last_edited_time": "2026-09-27T08:11:00.000Z"
}
---

# 🗑️ 归档页面

这里是垃圾站，废稿在这里
[集合类（Java集合框架）](集合类java集合框架/index.md)
  # 省流：
  这章讲的是Java集合框架
  什么是集合框架：Java针对“集合”做的一系列 创建/操作 的标准 方法/类/接口
  什么是集合：集合是针对Java不同数据结构做的标准的 创建/操作 的 方法/类/接口
  集合框架的设计分为三层：接口（定义行为），实现类（实现接口），通用算法（将实现类组合起来，做成一些常用算法）
  JavaSE非常贴心的将这三层全部自带了，开发者几乎不需要自己实现任何东西
  # 注意
  java集合框架位于java.util包中，别忘了import（导入包）
  # 啰嗦：
  （其实和省流版讲的不太一样，没必要看这个）
  ~~集合类是Java中非常重要的存在，使用频率极高。集合其实与我们数学中的集合是差不多的概念，集合表示一组对象，每一个对象我们都可以称其为元素。不同的集合有着不同的性质，比如一些集合允许重复的元素，而另一些则不允许，一些集合是有序的，而其他则是无序的。~~
  ~~集合类其实就是为了更好地组织、管理和操作我们的数据而存在的，包括列表、集合、队列、映射等数据结构。从这一块开始，我们会从源码角度给大家讲解（先从接口定义对于集合需要实现哪些功能开始说起，包括这些集合类的底层机制是如何运作的）不仅仅是教会大家如何去使用。~~
  ~~集合跟数组一样，可以表示同样的一组元素，但是他们的相同和不同之处在于：~~
  1. ~~它们都是容器，都能够容纳一组元素。~~
  ~~不同之处：~~
  1. ~~数组的大小是固定的，集合的大小是可变的。~~
  1. ~~数组可以存放基本数据类型，但集合只能存放对象。~~
  1. ~~数组存放的类型只能是一种，但集合可以有不同种类的元素~~

  在这里我们重申一些概念：
  **接口不能创建对象，但对象可以引用给接口**
  集合根接口
    所有集合的祖先都是集合根接口`Collection`，我们这节通过根接口了解集合的相关功能
    # 说在最前面
    集合依旧是创建一个对象➡️数据存在对象中➡️用类中的各种方法操作数据
    # **Java 集合类与数组的区别**
    **核心区别：数组是固定长度、存储基本类型与对象的基础数据结构；集合是可动态扩容、只能存储对象、提供丰富操作方法的框架体系。** 数组是语言层面的"哑"容器，集合是构建其上的"管理生态"。
    # 功能
    **添加功能**
    | **方法** | **说明** |
    | --- | --- |
    | `boolean add(E e)` | 添加一个元素 |
    | `boolean addAll(Collection<? extends E> c)` | 添加一个集合的所有元素 |
    **删除功能**
    | **方法** | **说明** |
    | --- | --- |
    | `boolean remove(Object o)` | 删除指定元素 |
    | `boolean removeAll(Collection<?> c)` | 删除指定集合中包含的所有元素（交集） |
    | `boolean removeIf(Predicate<? super E> filter)` | 根据条件删除（JDK 8+） |
    | `void clear()` | 清空集合 |
    **判断功能**
    | **方法** | **说明** |
    | --- | --- |
    | `boolean contains(Object o)` | 判断是否包含指定元素 |
    | `boolean containsAll(Collection<?> c)` | 判断是否包含指定集合的所有元素 |
    | `boolean isEmpty()` | 判断集合是否为空 |
    | `boolean equals(Object o)` | 比较相等 |
    **获取功能**
    | **方法** | **说明** |
    | --- | --- |
    | `int size()` | 返回元素个数 |
    | `Iterator<E> iterator()` | 返回迭代器，用于遍历 |
    | `Spliterator<E> spliterator()` | 返回可分割迭代器（并行遍历用） |
    | `Stream<E> stream()` | 返回顺序流（JDK 8+） |
    | `Stream<E> parallelStream()` | 返回并行流（JDK 8+） |
    **转换功能**
    | **方法** | **说明** |
    | --- | --- |
    | `Object[] toArray()` | 转成对象数组 |
    | `<T> T[] toArray(T[] a)` | 转成指定类型的数组 |
    **保留功能**
    | **方法** | **说明** |
    | --- | --- |
    | `boolean retainAll(Collection<?> c)` | 保留指定集合中包含的元素（取交集 |
  List列表
    List是庞大集合类中的一种类，**它的主要特性有：**
    - 是一个有序的集合，插入元素默认是插入到尾部，按顺序从前往后存放，每个元素都有一个自己的下标位置
    - 列表中允许存在重复元素
    List列表也被抽象成了接口，它继承自SequencedCollection（Java21）或Collection（Java21以前）接口
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
    # 常用列表类
    **ArrayList 动态数组**（线性表的一种）：更适合随机访问，因为可以直接读取某个下标的元素。插入则性能较差，因为需要移动一组元素，让出空间。
    **LinkedList 双向链表：**不适合随机访问，因为无法直接获取某个元素，只能遍历查找。插入性能较好，因为可以直接改变链表中结点的指向。
    # 列表基本操作（以ArrayList为例）
    上面说这么多下面直接演示
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
    # 是什么
    迭代器是一种**遍历集合元素**的工具。由于不同集合类的数据结构不同，导致实现不同，因此遍历的方式也不同，而迭代器对于不同的集合类提供了相同的接口，用户只需要使用相关接口，而不需要知道集合内部的实现细节，更加灵活

    其中Iterator 是 Java 迭代器最简单的实现，ListIterator 是 Collection API 中的接口， 它扩展了 Iterator 接口。
    # Iterator接口中定义的方法
    - **next()** - 返回迭代器的下一个元素，并将迭代器的指针移到下一个位置。
    - **hasNext()** - 用于判断集合中是否还有下一个元素可以访问。
    - **remove()** - 从集合中删除迭代器最后访问的元素（可选操作）
    # 注意
    **注意：**Java 迭代器（特指Iterator接口）是一种单向遍历机制，即只能从前往后遍历集合中的元素，不能往回遍历。同时，在使用迭代器遍历集合时，不能直接修改集合中的元素（可能会导致 ConcurrentModificationException 异常），而是需要使用迭代器的 remove() 方法来删除当前元素。
    # 基本使用（以ArrayList+Iterator为例）
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
