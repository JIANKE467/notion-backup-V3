---
{
  "id": "4045a2dd-8276-8017-82df-da3121859075",
  "url": "https://app.notion.com/p/Java21-4045a2dd8276801782dfda3121859075",
  "created_time": "2026-10-25T08:35:00.000Z",
  "last_edited_time": "2026-10-25T09:25:00.000Z"
}
---

#  (Java21)虚拟线程

# 剧情引入
线程大类上分为两种：平台线程&虚拟线程
平台线程：“真线程”，一个线程就会在真机内核上创建一个线程，由操作系统直接调度，开销大
虚拟线程：“假线程”，多个Java线程可能映射到几个真实线程上，JVM可以管理其调度，开销低（本质是对操作系统真实线程的二次封装）
![](assets/4045a2dd-8276-80c8-931c-e78c519e6cf1.webp)
# 虚拟线程
### 创建方式1（调用Thread.startVirtualThread()方法）
调用Thread.startVirtualThread()方法，run()方法以Lambda表达式的形式作为参数传入
```java
Thread.startVirtualThread(() -> {
    System.out.println("我是虚拟线程");
});
```
注意：
- 虚拟线程默认就是守护线程且不可更改
- 虚拟线程默认执行内容可能不会显示到控制台上（虚拟线程生命周期长于主进程时，主线程关闭会强行停止守护线程），在主线程使用join方法阻塞等待虚拟线程执行完毕后再继续运行即可保障虚拟线程的运行
```java
Thread.startVirtualThread(() -> {
    System.out.println("我是虚拟线程");
}).join();
```
### 创建（使用线程构建器）
这个线程构建器不是上节那个，上节那个是创建平台线程的，这里的线程构建器`Thread.ofVirtual()`是他的兄弟，专门用来创建虚拟线程的
使用方法同样是链式调用
```java
Thread.ofVirtual()
        .name("虚拟线程 01")
        .start(() -> System.out.println("我真的是虚拟线程"));
```
注意，虚拟线程不支持使用`stop`结束线程，调用会报错（stop早在Java1.1就废弃了，别的场景也不建议使用）
