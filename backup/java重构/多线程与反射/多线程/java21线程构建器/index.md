---
{
  "id": "4045a2dd-8276-80f6-95b8-dec242265706",
  "url": "https://app.notion.com/p/Java21-4045a2dd827680f695b8dec242265706",
  "created_time": "2026-10-25T07:23:00.000Z",
  "last_edited_time": "2026-10-25T08:38:00.000Z"
}
---

#  (Java21)线程构建器

原先我们创建线程需要三步：
1. 继承Thread类并重写run()方法/实现Runnable接口并重写run()方法
1. 创建线程对象
1. 调用start()方法启动线程
而Java21推出了**Thread.ofPlatform() 方法**可以实现一步创建并启动线程（在链式调用中完成线程定义）
Java推出这个就是针对传统复杂的线程创建方式的替代
# **Thread.ofPlatform() 方法**
它是Thread类下的静态方法，它本身的作用是返回一个 `Thread.Builder.OfPlatform` 构建器对象，主要依靠链式调用一下几个特定的方法来使用（下面介绍）
### API列表
| **方法签名** | **作用** | **注意事项** |
| --- | --- | --- |
| `name(String name)` | 设置线程名 | 未设置时默认 `Thread-N` |
| `name(String prefix, long start)` | 设置"前缀+计数器"命名模式 | 计数器在每创建一个线程后自增 |
| `daemon(boolean on)` | 设置守护线程状态 | `true` 为守护线程 |
| `daemon()` | 等价于 `daemon(true)` | 默认方法 |
| `priority(int priority)` | 设置线程优先级 | 取值须在 `MIN_PRIORITY`(1) ~ `MAX_PRIORITY`(10)，否则抛 `IllegalArgumentException` |
| `stackSize(long stackSize)` | 设置期望栈大小（字节） | 仅是"建议"，JVM 可忽略；0 被忽略，负数抛异常 |
| `group(ThreadGroup group)` | 设置线程组 | 平台线程独有，虚拟线程无此方法 |
| `uncaughtExceptionHandler(Thread.UncaughtExceptionHandler ueh)` | 设置未捕获异常处理器 | 线程因未捕获异常终止时回调 |
| `inheritInheritableThreadLocals(boolean inherit)` | 是否继承创建线程的可继承 ThreadLocal | 默认 `true` 继承 |
结束方法（将run()方法重写作为参数传入）：
| **方法** | **返回值** | **行为** |
| --- | --- | --- |
| `unstarted(Runnable task)` | `Thread` | 创建但不启动，仍需手动调 `thread.start()` |
| `start(Runnable task)` | `Thread` | 创建并**立即启动** |
| `factory()` | `ThreadFactory` | 返回线程工厂，供线程池等场景复用 |
# 怎么用
使用链式调用来快速 创建/定义/启动 线程
具体步骤：
1. 先调用**Thread.ofPlatform() 方法**获取构建器对象
1. 接着链式调用上述的几个定义线程的方法
1. 最后调用结束方法以启动/不启动/返回线程工厂
例子：
```java
				//获取构建器对象
Thread t = Thread.ofPlatform()
				//设置线程名
        .name("worker")
        //设置是否为守护线程
        .daemon()
        //结束方法（run()方法重写在这里以参数传入）
        .start(() -> System.out.println("任务执行中"));
```
# 注意
- 别看**Thread.ofPlatform() 方法**可以链式调用就以为Thread支持链式调用，上述方法虽然看着好像是从Thread类调用的，但其实他们不属于Thread，而是属于**Builder（构建器），**所以Thread中的方法是完全不支持链式调用的，是构建器支持链式调用
- 线程构建器构建的是且只能是平台线程（线程分两种：平台线程&虚拟线程）（虚拟线程&平台线程将在下一节详细讲解）
