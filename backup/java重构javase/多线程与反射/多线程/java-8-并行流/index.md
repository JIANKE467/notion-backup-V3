---
{
  "id": "4035a2dd-8276-8019-b654-f4772949b7ed",
  "url": "https://app.notion.com/p/Java-8-4035a2dd82768019b654f4772949b7ed",
  "created_time": "2026-10-24T08:55:00.000Z",
  "last_edited_time": "2026-10-24T10:01:00.000Z"
}
---

#  **(Java 8) 并行流**

先回顾一个Java集合框架中的知识：迭代器[Iterator接口（迭代器）](https://app.notion.com/p/3e85a2dd827680598e6efa2e1bef754c) 
简而言之：迭代器iterator是帮助遍历集合的工具，开发者无需关心集合底层实现就可以使用相同的方法遍历每种集合
这节同样介绍一个迭代器，不过它是支持多线程的
# Spliterator接口
**Spliterator（Splittable Iterator，可拆分迭代器）是 Java 8 引入的接口，它既能像 Iterator 一样顺序遍历元素，还能把数据"劈"成两半交给多线程并行处理，是整个 Stream API 和并行流的底层引擎。**
### 定义的方法
`tryAdvance()`：遍历（单步执行） 「传入：要对该元素执行的操作的Lambda表达式」
`forEachRemaining()`** **: 遍历（批量执行）「传入：要对该元素执行的操作的Lambda表达式」
`trySplit()` ：切分（切分成两部分，这样就能多线程访问了）「空参调用」
`estimateSize()`：估计**剩余**元素的个数「空参调用」
`getExactSizeIfKnown()`：返回精确**剩余**元素的个数「空参调用」
`characteristics()`：返回当前集合特性位掩码（如：有序，无需，无重复…）「空参调用」
# 如何使用
Q：说了这么多，Spliterator只是个接口，怎么用呢？实现类呢？用我手动实现吗？
A：Java8+后，所有的集合类都实现了Spliterator接口，因此无需手动实现，集合框架的实现类就是Spliterator接口的实现类，只需要调用Spliterator接口相关方法即可，而无需实现接口
# 并行流
讲了这么久才进入正题，其实上面的东西不重要，因为日常开发几乎不会手动调用这些，了解即可
上面说的东西就是并行流的底层原理，那接下来将并行流的使用及作用
### 作用
一般的流都是针对单线程设计的，无法实现多线程运行，而并行流就是专门为多线程设计的
这里我们说的流是集合框架的[(Java 8) Stream流](https://app.notion.com/p/3f75a2dd827680bc91aecfd079a2a38c) ，而不是JavaIO的文件流
parallelStream()就是并行流，使用方法和Stream流完全一样，只是在链式调用获取流时不要使用`stream()`方法，而是使用`parallelStream()`方法来获取流，详情请看[(Java 8) Stream流](https://app.notion.com/p/3f75a2dd827680bc91aecfd079a2a38c) 
一行代码就能切换：
```java
**list.stream().filter(...).count()              // 顺序流：单线程
list.parallelStream().filter(...).count()      // 并行流：多线程**
```
