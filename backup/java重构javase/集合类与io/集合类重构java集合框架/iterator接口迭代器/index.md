---
{
  "id": "3e85a2dd-8276-8059-8e6e-fa2e1bef754c",
  "url": "https://app.notion.com/p/Iterator-3e85a2dd827680598e6efa2e1bef754c",
  "created_time": "2026-09-27T06:53:00.000Z",
  "last_edited_time": "2026-10-12T10:08:00.000Z"
}
---

#  *Iterator接口（*迭代器）

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
