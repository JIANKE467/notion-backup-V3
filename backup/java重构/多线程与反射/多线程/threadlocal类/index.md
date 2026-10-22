---
{
  "id": "4015a2dd-8276-80a1-8acb-cb356f207d08",
  "url": "https://app.notion.com/p/ThreadLocal-4015a2dd827680a18acbcb356f207d08",
  "created_time": "2026-10-22T09:36:00.000Z",
  "last_edited_time": "2026-10-22T10:49:00.000Z"
}
---

#  **ThreadLocal类**

**ThreadLocal类作用：同一个 ThreadLocal 变量，在每个线程中都有自己独立的一份值**（提供线程中的变量隔离）
# Q&A
Q：乂，不对啊，不是一个线程对象对应一个线程的吗（逻辑：同一个线程对象不能重复启动线程），那对象间本身就是隔离的，搞个这个类岂不是多此一举？
A：乂，这就是很恶心的一点了，有的写法会给业务类创建一个对象（A），然后在创建两个线程对象（α和β），然后将对象A作为参数传入α和β线程对象中，此时α和β对象间的隔离依然有效，但由于它们传入了同一个对象引用A，实际对A进行的操作是没有隔离的（给我听死了）🤮
**ThreadLocal类就是为了解决这种情况下隔离失效的问题的😭**
# 原理
创建一个**ThreadLocal类的方法就是创建了一个无论怎么折腾，它永远对线程间隔离的变量**
创建一个**ThreadLocal类**的对象一次只能获得一个变量，如果需要多个请使用不同的对象名多次创建（对象名用于标记该变量）
# 使用方法
### 创建
1. 创建**ThreadLocal类的对象（ThreadLocal类是泛型类，需要声明存储数据的类型）**（对象名用于标记该变量）
### 使用
使用`变量对象名.set()`来设置该变量的值
使用`变量对象名.get()`来查看该变量的值
### 注意
- 该变量在线程间是隔离的（每个线程都能调用该变量，但每个线程对该变量的操作都是独立的）
- 该变量无法被子线程使用，如果需要子线程也能使用该隔离变量需要使用InheritableThreadLocal来创建“线程隔离变量的对象”
### 例子
```java
public static void main(String[] args) throws InterruptedException {
    ThreadLocal<String> local = new ThreadLocal<>();  //注意这是一个泛型类，存储类型为我们要存放的变量类型
    Thread t1 = new Thread(() -> {
        local.set("lbwnb");   //将变量的值给予ThreadLocal
        System.out.println("线程1变量值已设定！");
        try {
            Thread.sleep(2000);    //间隔2秒
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("线程1读取变量值：");
        System.out.println(local.get());   //尝试获取ThreadLocal中存放的变量
    });
    Thread t2 = new Thread(() -> {
        local.set("yyds");   //将变量的值给予ThreadLocal
        System.out.println("线程2变量值已设定！");
    });
    t1.start();
    Thread.sleep(1000);    //间隔1秒
    t2.start();
}
```
