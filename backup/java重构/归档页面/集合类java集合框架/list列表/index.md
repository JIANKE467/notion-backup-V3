---
{
  "id": "3e55a2dd-8276-8040-8233-d62acce9236c",
  "url": "https://app.notion.com/p/List-3e55a2dd827680408233d62acce9236c",
  "created_time": "2026-09-24T09:37:00.000Z",
  "last_edited_time": "2026-09-25T08:51:00.000Z"
}
---

#  List列表

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
