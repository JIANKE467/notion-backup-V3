---
{
  "id": "3e75a2dd-8276-808d-91af-c5d34c7aaffa",
  "url": "https://app.notion.com/p/Queue-Deque-3e75a2dd8276808d91afc5d34c7aaffa",
  "created_time": "2026-09-26T07:46:00.000Z",
  "last_edited_time": "2026-09-27T08:11:00.000Z"
}
---

#  Queue和Deque接口

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
