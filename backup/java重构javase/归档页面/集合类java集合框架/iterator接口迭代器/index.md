---
{
  "id": "3e65a2dd-8276-80bb-a5df-dfb984b69b17",
  "url": "https://app.notion.com/p/Iterator-3e65a2dd827680bba5dfdfb984b69b17",
  "created_time": "2026-09-25T08:51:00.000Z",
  "last_edited_time": "2026-09-27T07:24:00.000Z"
}
---

#  *Iterator接口（*迭代器）

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
