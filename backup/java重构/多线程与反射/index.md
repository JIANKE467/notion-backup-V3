---
{
  "id": "3fe5a2dd-8276-8024-a824-dd83cf18de05",
  "url": "https://app.notion.com/p/3fe5a2dd82768024a824dd83cf18de05",
  "created_time": "2026-10-19T08:02:00.000Z",
  "last_edited_time": "2026-10-19T08:03:00.000Z"
}
---

# 6️⃣ 多线程与反射


[多线程](多线程/index.md)
  这章讲的内容是Java多线程框架
  如果想让一个程序同时处理多个任务，有两种方案：
  1. 创建多个进程（开销太大，同步复杂）
  1. 一个进程创建多个线程（开销小，同步简单）
  显然，我们这里将的是多线程
  线程的创建和启动
    在面向过程及前面的面向对象中Java默认只有一个线程（不使用多线程默认只有一个线程）
    # 创建线程
    ### 方法1：继承Thread类
    步骤：
    1. 定义一个继承Thread类的类
    1. 重写run()方法「重写内容即是新线程的逻辑」
    ```java
class MyThread extends Thread {
    @Override
    public void run() {
        // 把这个线程要干的活写在 run() 里
        System.out.println("我是一条线程，正在干活~");
    }
}

// 创建（只是造出对象，线程还没运行）
MyThread t = new MyThread();   // 👈 创建
    ```
    注意⚠️：
    - 类定义部分继承Thread类并重写了run方法并不代表线程已经被创建出来，创建该类的对象也不代表线程已经运行，线程真正运行还需要调用start()方法「后面介绍」
    ### 方法2：实现Runnable接口（推荐✅）
    步骤：
    1. 写一个Runnable接口的实现类
    1. 重写run()方法「重写内容即是新线程的逻辑」
    ```java
class MyTask implements Runnable {
    @Override
    public void run() {
        System.out.println("我是任务，被线程执行中~");
    }
}

// 创建分两步：先造任务，再把任务“装进”线程
MyTask task = new MyTask();        // 👈 创建任务
Thread t = new Thread(task);       // 👈 创建线程
    ```
    优点：Java只能继承一个类，但可以实现多个接口，尽量不使用继承从而提高代码扩展性
    注意⚠️：使用方法2实现多线程的，启动线程不能直接调用start()方法，而是需要3步走↓
    1. 创建Runnable实现类对象
    1. 创建Thread类的对象，将刚创建Runnable实现类对象作为构造方法参数传入
    1. 调用Thread类的对象下的start方法
    ### 方法3：Lambda表达式
    这种就是方法2 Lambda表达式，和方法2原理一样
    # 启动线程
    ### 方法1的启动方法（直接继承Thread类）
    两步走
    1. 创建继承了Thread类的类的对象
    1. 调用该对象下start()方法
    ```java
//线程定义
class MyThread extends Thread {
    @Override
    public void run() {
        // 把这个线程要干的活写在 run() 里
        System.out.println("我是一条线程，正在干活~");
    }
}

// 创建（只是造出对象，线程还没运行）
MyThread t = new MyThread();   // 👈 创建
// 启动
T.start();
    ```
    ### 方法2的启动方法（实现Runnable接口）
    三步走
    1. 创建Runnable实现类对象
    1. 创建Thread类的对象，将刚创建Runnable实现类对象作为构造方法参数传入
    1. 调用Thread类的对象下的start方法
    ```java
// 线程定义
class MyTask implements Runnable {
    @Override
    public void run() {
        for (int i = 1; i <= 3; i++) {
            System.out.println("子线程执行：" + i);
        }
    }
}



public class Test {
    public static void main(String[] args) {

        // 1步：创建线程定义的对象
        MyTask task = new MyTask();       
	        // 2步: 创建Thread类对象,传入1步的对象
        Thread t = new Thread(task);      
        // 3步：调用 Thread 的 start() 启动
        t.start();                       
    }
}

    ```
    PS：为什么这么SB？
    因为Java不支持多继承，所以不想占用宝贵的继承位就只能把自己写的东西作为构造方法参数传进去（从继承结构上看像挂上去的），而不是继承后直接调用方法
    # 注意
    - 一个对象只能创建一个线程，想要创建多个相同线程不能重复调用start()方法，而是需要创建多个对象并调用不同对象的start()方法
    - 启动时是调用start()方法而不是run()方法，普通开发者无论何时都不该调用run()方法
  线程的休眠/中断/终止
    # 备注
    Q ：本节中除了**interrupt()**方法是实例方法外，其他方法均为静态方法，但对象中不包含静态方法，假如要执行sleep()方法JVM怎么知道对哪个对象执行？
    A：根据线程的设计理念“线程间是协作而非强制”我们知道，线程只能对自己进行操作，而不应该去操作别的线程，所以静态方法默认就是对自己执行的
    PS：对于实例方法，不要使用`Thread.xxx()`调用实例方法，这直接报错
    PS：对于静态方法，不要使用`对象.xxx()`这种调用方式，虽然能运行，但这是不规范的，且无论前面写哪个对象，最后都是执行到当前对象上了
    # **休眠方法**
      ## **Thread.sleep()（静态）**
      **作用**：让**当前线程**暂停执行指定时长，进入 `TIMED_WAITING` 状态，期间不占用 CPU，但**不释放持有的锁**。
      **传入参数**：
      - `sleep(long millis)`：休眠毫秒数
      - `sleep(long millis, int nanos)`：毫秒 + 纳秒（0~999999，越界抛 `IllegalArgumentException`）
      **简单示例**：
      ```java
try {


    Thread.sleep(2000);              // 当前线程睡 2 秒
    // Thread.sleep(2000, 500);      // 2 秒 + 500 纳秒
    
    
    //下面内容看不懂可以先往后看
} catch (InterruptedException e) {   // 受检异常，必须处理
    Thread.currentThread().interrupt(); // 恢复中断标志
}
      ```
      **注意事项**：
      1. 是**静态方法**，作用于“当前正在执行的线程”，和 `t.sleep()` 写法无关（别被误导）
      1. **不释放锁**——在 `synchronized` 块里睡会卡死其他等锁线程
      1. 时间不精确，有毫秒级误差，不能当精确定时器用
      1. 睡眠中只能被 `interrupt()` 惊醒（抛异常），**没有温和唤醒方式**
      ## **TimeUnit.sleep()（静态）**
      **作用**：`Thread.sleep()` 的可读性封装，单位更直观。
      **传入参数**：该枚举对应的时间数量，如 `TimeUnit.SECONDS.sleep(5)`。
      **简单示例**：
      ```java
TimeUnit.SECONDS.sleep(1);       // 睡 1 秒
TimeUnit.MILLISECONDS.sleep(500); // 睡 500 毫秒
TimeUnit.MINUTES.sleep(2);       // 睡 2 分钟
      ```
      **注意事项**：
      - 底层仍调用 `Thread.sleep()`，行为完全一致
      - 也抛 `InterruptedException`，同样需要处理
      - **推荐**：代码里别写 `sleep(3600000)` 这种魔法数字，用 `TimeUnit.HOURS.sleep(1)`
    # **中断方法**
      ## **interrupt()**
      **作用**：给目标线程设置一个“中断标志”（布尔值），是一种**协作式停止请求**，**不会强杀线程**。若目标线程正处于 `sleep()/wait()/join()` 等可中断阻塞中，它会立即退出阻塞（打断睡眠/等待）并抛 `InterruptedException`（同时清除标志）。
      **传入参数**：**无参数**。目标是“调用它的线程对象”。
      **简单示例（通过中断标志唤醒睡眠进程t，而非结束线程）**：
      ```java
//线程t定义
Thread t = new Thread(() -> {

//对于线程t的睡眠中断的异常捕获（规范写法）
//当然不写这些也行，那就不对中断标记进行处理了，中断了也没用
    try {
        Thread.sleep(10_000);
    } catch (InterruptedException e) {
        System.out.println("睡眠被打断！");
        Thread.currentThread().interrupt(); // 补回标志
    }
});


//启动线程t
t.start();
//当前线程睡眠（不是睡眠线程t，也没这权限）
Thread.sleep(1000);
//中断线程t
t.interrupt();   // 1 秒后向 t 发出中断请求
      ```
      **实例二（线程收到中断标志后结束线程）：**
      ```java
//循环执行任务，直到Thread.currentThread().isInterrupted()不成立
//Thread.currentThread()是调用Thread类的静态方法，返回当前线程对象
//isInterrupted()方法是检查中断标记状态，有标记返回真
while (!Thread.currentThread().isInterrupted()) {
    System.out.println("【worker】干活中... count=" + System.currentTimeMillis() % 10000);

    try {
        Thread.sleep(500);   // 模拟每干一活歇0.5秒
    } catch (InterruptedException e) {
        // sleep 被打断时标志已被 JVM 清除，
        // 必须补回来，否则上面的 while 永远感知不到！
        Thread.currentThread().interrupt();   // ★ 铁律：恢复标志
        System.out.println("【worker】睡眠中被叫醒，准备收工");
        // break 可写可不写——不写的话循环条件下一轮也会退出
    }
}
      ```
      **注意事项**：
      1. 线程正常运行时，`interrupt()` **只设标志不影响执行**，需要线程自己检查标志才有效
      1. 抛出 `InterruptedException` 的同时**标志已被清除**，所以 catch 里要补 `Thread.currentThread().interrupt()`**就这特性**
      1. 对于休眠中的进程，无论开发者是否处理都会被“惊醒”。而对于正常运行状态的进程，开发者不处理中断信号就被吞掉了
      1. 再次强调，标准的中断处理流程：
      ```java
try {
          可能抛异常的语句；
          
    } catch (InterruptedException e) {
    
        Thread.currentThread().interrupt();   
   
    }
      ```
      ## **isInterrupted()**
      这个方法不是用来中断的，而是检查中断标记的，通常在中断处理时使用
      **作用**：查询目标线程的中断标志状态，**不清除**标志。
      **传入参数**：无。查的是“调用它的线程对象”。
      **简单示例**：
      ```java
Thread worker = new Thread(() -> {
    while (!Thread.currentThread().isInterrupted()) { // 反复检查
        // 干活...
    }
    System.out.println("检测到中断，退出");
});
      ```
      **注意事项**：
      - 可反复调用，状态不会因查询而改变
      - 响应中断的标准写法：循环条件 + `isInterrupted()`
      ## **Thread.interrupted()（静态）**
      这个不是用来中断的，而是检查中断标记的，通常在中断处理时使用
      **作用**：查询**当前线程**的中断标志，**检查后清除标志**（置回 false）
      **传入参数**：无。
      **简单示例**：
      ```java
Thread.currentThread().interrupt();
System.out.println(Thread.interrupted()); // true（并清除）
System.out.println(Thread.interrupted()); // false（已清除）
      ```
      **注意事项**：
      - 和 `isInterrupted()` 唯一区别：**会清除标志**，是“一次性”检测
      - 适合“检查一次然后复位”的场景；循环里反复检查应该用 `isInterrupted()`
      - 两者记混是常见 bug 来源
      ##  Thread.currentThread()（静态）
      这个方法不是用来中断的，是用来返回当前线程对象的
      什么？你问为什么不直接用对象名
      因为代码可能被多个线程复用，总不能每个线程都写个重复的逻辑吧，因此这个方法看的是实际运行时的线程对象
      作用：返回当前线程对象，一般在中断处理部分使用，和**interrupt()**连用
    # **等待方法（未审核）**
      ## **Object.wait()（静态）**
      **作用**：当前线程在持有的锁对象上进入等待状态，**释放锁**，直到被 `notify()/notifyAll()` 唤醒、超时、或被中断。用于线程间协作（典型：生产者-消费者）。
      **传入参数**（三个重载）：
      - `wait()`：无限等待
      - `wait(long timeout)`：最长等毫秒数（**timeout=0 等价于无限等待**）
      - `wait(long timeout, int nanos)`：毫秒 + 纳秒（0~999999）
      **简单示例**：
      ```java
synchronized (lock) {              // 必须先持有 lock 的锁
    while (!condition) {           // 必须用 while 检查！
        try {
            lock.wait(5000);       // 最多等 5 秒，期间释放锁
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            return;
        }
    }
    // 条件满足，继续执行（已重新拿到锁）
}
      ```
      **注意事项**：
      1. **必须在 synchronized 块中调用**，否则抛 `IllegalMonitorStateException`
      1. **释放锁**（与 sleep 最大区别）
      1. 条件检查必须用 `while` 而非 `if`——防**虚假唤醒**、防条件被抢
      1. `wait` 和 `notify` 必须作用在**同一个对象**上，否则通知送达不了
      1. 被唤醒后要**重新竞争锁**才能从 `wait()` 返回
      ## **notify() / notifyAll()**
      **作用**：唤醒在该对象上等待的线程。`notify()` 随机唤醒一个；`notifyAll()` 唤醒全部。
      **传入参数**：无。**无法指定唤醒哪个线程**。
      **简单示例**：
      ```plain text
synchronized (lock) {
    ready = true;
    lock.notifyAll();   // 唤醒所有等待者，让它们各自重查条件
}
      ```
      **注意事项**：
      1. `notify()` 随机挑人，可能唤醒“不该醒的”，造成**信号丢失**
      1. **初学者默认用 ****`notifyAll()`**，正确性优先，性能差异可忽略
      1. 同样必须在 `synchronized` 中调用
      1. `notify` 先于 `wait` 执行时信号会丢失——用条件变量 + while 循环兜底
      ## **Thread.join()**
      **作用**：当前线程阻塞等待目标线程执行结束（相当于“等它跑完我再走”）。

      **传入参数**：
      - `join()`：无限等到目标线程死亡
      - `join(long millis)`：最多等指定毫秒，超时就算对方没结束也继续
      - `join(long millis, int nanos)`：毫秒 + 纳秒
      **简单示例**：
      ```plain text
Thread t = new Thread(() -> {
    try { Thread.sleep(3000); } catch (InterruptedException e) {}
});
t.start();
t.join();         // main 阻塞，直到 t 结束
// t.join(1000);  // 最多等 1 秒，超时放行
System.out.println("t 结束了，main 继续");
      ```
      **注意事项**：
      1. 底层实现就是 `wait(0)`，所以等待期间可被 `interrupt()` 打断
      1. 等待期间**释放的是目标线程对象的锁**，不释放调用者持有的其他锁
      1. 典型用途：主线程等所有子任务完成后汇总结果
      ## **Condition.await() / signal()**
      **作用**：`ReentrantLock` 下的 wait/notify 升级版，支持多个独立条件队列、可限时、可中断。
      **传入参数**：
      - `await()`：无限等待
      - `await(long time, TimeUnit unit)`：限时等待，返回 true 表示超时前被唤醒
      - `awaitNanos(long nanos)`：传**纳秒**
      - `awaitUntil(Date deadline)`：等到绝对时刻
      **简单示例**：
      ```plain text
ReentrantLock lock = new ReentrantLock();
Condition cond = lock.newCondition();   // 一个锁可建多个 Condition
volatile boolean ready = false;

// 等待方
lock.lock();
try {
    while (!ready) {
        cond.await(5, TimeUnit.SECONDS);
    }
} finally { lock.unlock(); }

// 唤醒方
lock.lock();
try { ready = true; cond.signalAll(); } finally { lock.unlock(); }
      ```
      **注意事项**：
      1. 必须在 `lock()` 和 `unlock()` 之间调用，否则抛 `IllegalMonitorStateException`
      1. 多个 Condition 可把不同条件的等待者分开，间接实现“指定唤醒哪一类”——比 notify 强
      1. 同样要配合 `while` 检查条件
      1. 别和 `wait()/notify()` 混用——`synchronized` 和 `ReentrantLock` 是两套机制
      ## **LockSupport.park() / unpark()**
      **作用**：最底层的阻塞/唤醒原语（JUC 的 AQS 就靠它）。不依赖锁对象；`unpark` 可以在 `park` 之前先“发放许可”，**不会信号丢失**。
      **传入参数**：
      - `park()`：无限阻塞
      - `parkNanos(long nanos)`：阻塞**纳秒数**（注意单位！）
      - `parkUntil(long deadline)`：阻塞到 Unix 时间戳（毫秒）
      - `unpark(Thread thread)`：传入**目标线程对象**——全 Java 唯一能“点名”唤醒的 API
      **简单示例**：
      ```plain text
Thread t = new Thread(() -> {
    LockSupport.parkNanos(TimeUnit.SECONDS.toNanos(10)); // 最多停10秒
    System.out.println("醒了");
});
t.start();
LockSupport.unpark(t);   // 可在 park 前调用，许可会保存
      ```
      **注意事项**：
      1. **单位是纳秒不是毫秒**！直接写 `parkNanos(10)` 等于没停；用 `TimeUnit.X.toNanos(n)` 换算
      1. 被中断时**直接返回但不抛异常**，需自己检查 `isInterrupted()`
      1. 许可只有 0/1 两个状态，多次 unpark 只记一次
      1. 一般不直接用于业务代码，是框架级工具
    # **停止**
      ## **Thread.stop()（已弃用，勿用）**
      **作用**：强制杀死线程，立刻解锁它持有的所有锁。
      **传入参数**：无。
      **简单示例**：
      ```plain text
// ❌ 错误示范，仅供了解，不要写！
t.stop();
      ```
      **注意事项**：
      1. **JDK 1.1 起弃用**：线程可能在修改共享数据改到一半时被杀，锁被强制释放，其他线程读到“半成品”数据
      1. 抛出的 `ThreadDeath` 是静默的，损坏可能很久之后才暴露，极难排查
      1. `suspend()`/`resume()` 也因死锁风险一同被弃用
      1. 结论：**线程生死只能由它自己决定，外力只能协商**
      ## **volatile 布尔标志（推荐方式一）（未审核）**
      **作用**：用共享变量通知线程“该停了”，线程自己检查标志并从 `run()` 正常返回。
      **传入参数**：无（就是自定义的 `volatile boolean` 字段）。
      **简单示例**：
      ```java
class Worker implements Runnable {
    private volatile boolean running = true; // volatile 保证可见性

    public void shutdown() { running = false; }

    public void run() {
        while (running) {
            System.out.println("工作中...");
            // 干活
        }
        System.out.println("线程正常结束");
    }
}

// 使用
Worker w = new Worker();
Thread t = new Thread(w);
t.start();
Thread.sleep(2000);
w.shutdown();   // 优雅请求停止
      ```
      **注意事项**：
      1. **必须加 ****`volatile`**，否则修改对其他线程可能不可见，线程停不下来
      1. 若线程正在 `sleep()` 中，要等它睡完才能看到标志——响应不够快
      1. 建议同时配合中断检查，双保险
      ## **中断标志终止（推荐方式二）**
      **作用**：结合 `isInterrupted()` 与 `interrupt()`，既能响应正常状态下的停止请求，又能立刻惊醒阻塞中的线程。**是 Java 官方推荐的终止方式**。
      **传入参数**：无。
      **简单示例**：
      ```plain text
Thread worker = new Thread(() -> {
    while (!Thread.currentThread().isInterrupted()) {
        try {
            Thread.sleep(500);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt(); // 补回标志，让循环条件生效
            break;
        }
    }
    System.out.println("清理资源，线程自然结束");
});
worker.start();
worker.interrupt();   // 请求停止
      ```
      **注意事项**：
      1. 记住铁律：**catch 里必须补 ****`Thread.currentThread().interrupt()`**，否则标志已被 JVM 清除，外层循环永远感知不到
      1. 千万别写空的 catch 吞掉异常——中断信号丢失，线程变“僵尸”
      1. 终止的本质是**让 ****`run()`**** 尽快跑完**，而不是外力杀掉
      ## **Future.cancel() / 线程池 shutdownNow()（工程封装）（未审核）**
      **作用**：工程中标准的取消/关闭手段，底层就是 `interrupt()`。
      **传入参数**：
      - `future.cancel(boolean mayInterruptIfRunning)`：true = 允许中断正在运行的任务
      - `executor.shutdownNow()`：无参数，中断池中所有线程
      **简单示例**：
      ```plain text
ExecutorService pool = Executors.newSingleThreadExecutor();
Future<?> f = pool.submit(() -> {
    while (!Thread.currentThread().isInterrupted()) { /* 干活 */ }
});

f.cancel(true);      // 中断这个任务
pool.shutdownNow();  // 中断池里所有线程
      ```
      **注意事项**：
      1. `cancel(true)` 只对尚未开始或正在运行且响应中断的任务有效
      1. `shutdownNow()` 返回未执行完的任务列表，注意处理
      1. 无论封装多高级，**底层都要求任务代码自己响应中断**——不配合的线程谁也停不了
    # **附：核心速记表**
    | **方法** | **参数** | **单位** | **释放锁** | **提前唤醒方式** |
    | --- | --- | --- | --- | --- |
    | `sleep(m)` | 1 | 毫秒 | ❌ | 仅 interrupt（抛异常） |
    | `wait(t)` | 0/1/2 | 毫秒（0=无限） | ✅ | notify / interrupt / 超时 |
    | `join(t)` | 0/1/2 | 毫秒 | — | interrupt / 超时 |
    | `await(t, unit)` | 2 | 数量+单位 | ✅ | signal / interrupt / 超时 |
    | `parkNanos(n)` | 1 | **纳秒** | ❌ | unpark / 中断（不抛异常） |
    | `interrupt()` | 0 | — | — | 它是唤醒方 |
    | `unpark(t)` | 1 | 目标线程 | — | 唯一能“点名”的唤醒 |
    **终极一句话：Java 线程控制哲学是“协作而非强制”——sleep 是自愿休息，wait 是持锁让位等通知，interrupt 是协商叫停，终止靠线程自己配合退出。**
  线程优先级
    Java不使用平均分配的方式为线程分配CPU资源，而是使用抢占式资源分配，按三种优先级顺序来分配CPU资源
    # 线程优先级
    - MIN_PRIORITY 最低优先级（最后运行）
    - NOM_PRIORITY 常规优先级（次优先运行）
    - MAX_PRIORITY 最高优先级（最优先运行）
    # 为线程设置优先级
    使用setPriority()方法为线程设置优先级
    ### setPriority()方法
    作用：设置线程优先级
    传入参数：Thread类的常量
    - Thread.MIN_PRIORITY（最低）
    - Thread.NORM_PRIORITY（正常）
    - Thread.MAX_PRIORITY（最高）
    例子：
    ```java
public static void main(String[] args) {
    //Lambda表达式（线程定义+创建线程对象）
    Thread t = new Thread(() -> {
        System.out.println("线程开始运行！");
    });
    
    //设置线程优先级
    t.setPriority(Thread.MIN_PRIORITY);  //通过使用setPriority方法来设定优先级
    //运行线程
    t.start();
}
    ```
    # 注意
    - 建议在线程启动前设置优先级，但启动后设置优先级也是可以的
    - 高优先级≠一定先得到CPU（只是概率比较大）
    - 子线程会继承父线程的优先级
    - setPriority()方法传入的常量实际上是1～10的优先级数字，当然也可以直接传入优先级数字（传入数字越界会抛`IllegalArgumentException`）
  线程的礼让和加入
    # 线程礼让
    线程礼让就是让当前线程让出时间片，可以在线程定义中使用`Thread.yield()`方法来实现这一效果
    ### Thread.yield()
    作用：Thread类中的静态方法，写在线程定义中，用来让出当前线程的时间片
    传入参数：空参调用
    例子:
    ```java

    Thread t1 = new Thread(() -> {
            Thread.yield();
});
  
    ```
    注意⚠️：
    - 线程礼让`Thread.yield()`方法只是对于调度器的一种提示，**不是“命令”**——调度器完全可以无视这个提示，让当前线程继续跑
    - `Thread.yield()`不会改变当前线程优先级，也不是暂时让出优先级，只是给调度器的一个提示
    - 几乎没有生产代码用这个方法，因为它没什么用（提升不了多少效率，且礼让后的调度行为完全由调度器决定）
    # 线程加入
    **线程加入（****`t.join()`****）的作用是：让当前线程停下来，等目标线程 ****`t`**** 执行完毕（死亡）后，当前线程再继续往下走。** 它解决的是“主线程（或调用线程）要等别的线程干完活才能继续”这一最经典的协作问题。
    ### join()
    作用：写在线程定义中，让当前线程执行到join()时停下，并在目标线程结束后继续执行
    传入参数：
    - 空参调用
    - join(timeout)：传入等待时间（超时放弃加入）
    例子：
    ```java
//线程t1定义
Thread t1 = new Thread(() -> {
    内容...;
});

//线程2定义
Thread t2 = new Thread(() -> {
   
  //线程加入
  //join方法可能抛异常，因此使用try-catch 
  try {
      t1.join();    
  } catch (InterruptedException e) {
      e.printStackTrace();
  }
 
});

    ```
    注意⚠️：
    - `join()`底层调用的是`wait()`因此可能抛`InterruptedException`异常，需要使用try-catch捕获异常，因此也是可被中断标记打断的
    - **要加入哪个线程就在本线程定义中调用那个线程对象的join方法，而不是调用本线程的join方法！！**！
    - 线程加入不是将两个线程合并，而是一个线程结束后，JVM唤醒另一个
    - 当前线程调用join前需要先启动
    - 不要`Thread.currentThread().join()`调用本线程的join方法，自己等自己死，程序卡死
    - 两个线程不要相互调用对方的join，会相互等待，造成死锁
    - 依旧别忘了处理中断（不处理就会吞中断）
    原理：调用t.join()**不是 t 线程“主动”唤醒本线程的——是 JVM 在 t 线程死亡时“自动”替它通知的**
  线程锁和线程同步
    # 前置知识
    共享变量：静态方法/静态变量 是所有线程（对象）共享的，就是所谓的共享变量「内存中的堆和方法区被所有线程共享」
    JMM 规定：**共享变量存于主内存，每个线程有自己的工作内存，其中保存了该线程读/写共享变量的副本**
    两种内存：在Java代码运行时内存分两种独立的类型，**工作内存（存放各线程私有数据）**和**主内存（存放共享数据）**
    - 各线程的工作内存也相互独立，没有权限修改其他线程的工作内存
    - 工作内存无法直接访问主内存中的共享变量（需要通过工作内存中的共享变量副本访问）
    ### 带来的问题：
    多个线程同时修改一个共享数据可能出现冲突，本节便是致力于解决该问题
    # synchronized关键字
    synchronized关键字是一把锁，它确保只能同时有一个线程使用某方法/代码块/静态方法
    ### 写法一：修饰方法
    将synchronized关键字写到方法的修饰符列表，以声明：该方法只允许同时有一个线程使用（其他需要使用该方法的线程无限期阻塞）
    例子：
    ```java
public class Counter {
    private int count = 0;
		
		//使用synchronized关键字修饰方法
    public synchronized void increment() {  
        count++;
    }
}

    ```
    ### **写法二：修饰代码块**
    这种方法需要先创建锁（就是创建一个object类型的空对象，我们只需要它的对象名）
    然后在原代码中使用`{}`将需要同步的代码包住，形成代码块，在代码块前添加：`synchronized (锁对象名)`以修饰代码块，代表使用该锁的代码块不能同时运行
    例子1：括号里传入一个锁对象
    ```java
//创建锁（使用private权限防止被外部类调用）
//就是创建一个空类，为了要它的名字
private final Object lock1 = new Object();


//使用该锁lock1锁住代码块A
synchronized (lock) {  
    count++;
}


//使用锁lock1锁住代码块B   
synchronized (lock) {  
    count--;
}

//结果：并行的两个线程中的代码块A与代码块B不能同时运行
    ```
    例子2：括号里传入this
    ```java
 synchronized (this) {   
        count++;
    }
//将this（当前对象名）作为锁名这种写法完全等价于修饰方法

    ```
    ### 写法三：修饰静态方法
    依旧是在静态方法的修饰符列表使用synchronized关键字
    ```java
public class Counter {
    private static int count = 0;

    public static synchronized void increment() {  // 锁的是 Counter.class
        count++;
    }
}
    ```
    # 注意
    - 锁只能定义并施加给共享变量/共享方法，不能也不应该在各线程中定义或施加锁（它们的方法/变量不是共享的）
    - 写法一只是写法二将this（当前对象名）作为锁名时的语法糖🍬，写法一实际上是有锁名的（当前对象名）
    - 写法三只是写法二将xxx.class（当前类名）作为锁名时的语法糖🍬，写法三实际上是有锁名的（当前类名.class）
    - 不建议在写法二中将this作为锁名，会有安全风险（当前对象是public权限的，那外部类都能随便调用锁）
    核心思维及底层原理就是创建写法二：创建/找一个对象名/类名作为锁名，仅仅需要一个名字来区分锁
  死锁
    在操作系统中我们学过，死锁就是两个消费者相互等待对方的资源导致程序卡死
    Java中的死锁和这个概念一样，上节讲过可以使用synchronized关键字修饰方法/代码块/静态方法从而锁住该资源防止冲突，但当线程A持有线程B的锁，线程B持有线程A的锁时就会发生相互等待，这便是死锁
    # 死锁的检测
    如果你怀疑某个程序有死锁，可以按照以下的步骤排查
    1. 运行该程序
    1. 在另一个终端中执行`jps -l`以输出程序的pid（进程号）
    1. 记住对应的进程号，用`jstack -l 进程号 > thread_dump.txt` 打印线程快照
    1. 打开 `thread_dump.txt` 文件，看是否有类似这样的内容
    ```plain text
Found one Java-level deadlock:
=============================
"Thread-1":
    waiting to lock monitor 0x0000000016b4e668 (object 0x000000076b0081c0, a java.lang.Object),
    which is held by "Thread-0"

"Thread-0":
    waiting to lock monitor 0x0000000016b4c198 (object 0x000000076b0081d0, a java.lang.Object),
    which is held by "Thread-1"
    ```
    或者使用简单办法（图像化工具）
    使用IDEA中的**JConsole工具：**
    在命令行输入`jconsole` 启动，选中你的 Java 进程连接后，切换到"线程"标签页，点击"检测死锁"按钮，工具会直接高亮显示死锁线程及其调用栈
  wait和notify方法
    # wait()方法
    作用：让当前线程释放锁等待
    传入参数：
    空参调用（无限等待）
    毫秒数（等待指定毫秒数）
    毫秒数，纳秒数（等待指定毫秒数+纳秒数）
    注意⚠️：
    - wait()方法必须在**synchronized 代码块中使用！（wait() 会释放锁，如果你没持有锁，谈何释放？）**
    - wait()方法也有可能抛异常（被interrupt()中断会抛`InterruptedException`），因此需要使用try-catch捕获异常
    - wait()方法也可以使用notify()方法正常唤醒
    - **需要使用锁对象来调用wait方法，而不是线程对象**
    语法：
    ```java
synchronized (锁名) {
    try {
        锁名.wait(); // 等待
    } catch (InterruptedException e) {
        e.printStackTrace();
    }
}               
    ```
    例子：
    ```java
public class WaitDemo {
    public static void main(String[] args) {
        Object lock = new Object();
        boolean[] hasCake = {false};

        // 消费者线程
        Thread consumer = new Thread(() -> {
            synchronized (lock) {
                while (!hasCake[0]) {
                    System.out.println("顾客：还没蛋糕，我等等...");
                    try {
                        lock.wait(); // 等待蛋糕
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
                System.out.println("顾客：终于有蛋糕了，开吃！🍰");
            }
        });

        // 生产者线程
        Thread producer = new Thread(() -> {
            try {
                Thread.sleep(2000); // 花2秒做蛋糕
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            synchronized (lock) {
                hasCake[0] = true;
                System.out.println("厨师：蛋糕做好了！");
                lock.notify(); // 通知顾客
            }
        });

        consumer.start();
        producer.start();
    }
}

    ```
    # **notify()方法**
    作用：用于随机唤醒一个已经进入**WAITING 状态的线程**（执行过wait()方法的线程）
    传入参数：空参调用
    注意⚠️：
    - notify()方法依然必须在**synchronized 代码块中使用！**
    -  `notify()` 唤醒**一个**在此对象上等待的线程，**随机选择**，无法指定
    - 它**不释放锁**，只是"发通知"，执行完synchronized 代码块才会释放锁
    - 通常用于加锁代码块执行完毕后拉起别的等待锁的进程
    - wait/notify/notifyAll 三兄弟**必须在同一个锁对象**上配合使用
    - **需要使用锁对象来调用wait方法，而不是线程对象**
    语法：
    ```java
synchronized (锁名) {
		//前置代码...
    锁名.notify(); // 只能叫醒一个，随机
   
} // 出了这个大括号，锁才真正释放

    ```
    # notifyAll()方法 
    作用：唤醒所有已经进入**WAITING 状态的线程，**这些线程共同竞争锁
    传入参数：空参调用
    注意⚠️：
    - notifyAll()方法依然必须在**synchronized 代码块中使用！**
    -  `notifyAll()` 唤醒**一个**在此对象上等待的线程，**随机选择**，无法指定
    - 它**不释放锁**，只是"发通知"，执行完synchronized 代码块才会释放锁
    - 通常用于加锁代码块执行完毕后拉起别的等待锁的进程
    - wait/notify/notifyAll 三兄弟**必须在同一个锁对象**上配合使用
    - **需要使用锁对象来调用wait方法，而不是线程对象**
    - 推荐使用notifyAll()方法而不是notify()方法（不容易漏喊）
    语法：
    ```java
synchronized (锁名) {
		//前置代码...
    锁名.notifyAll(); // 全部叫醒后竞争一个锁
   
} // 出了这个大括号，锁才真正释放
    ```
  ThreadLocal类
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
