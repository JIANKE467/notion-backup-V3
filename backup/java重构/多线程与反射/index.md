---
{
  "id": "3fe5a2dd-8276-8024-a824-dd83cf18de05",
  "url": "https://app.notion.com/p/3fe5a2dd82768024a824dd83cf18de05",
  "created_time": "2026-10-19T08:02:00.000Z",
  "last_edited_time": "2026-10-25T09:25:00.000Z"
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
  定时器
    我们可以使用前面学的`Thread.sleep()`（线程睡眠的静态方法）来实现一个最简单的定时器（如：三秒后执行下一句代码）
    但自己实现的定时器可能存在逻辑上的bug或功能上的不足，因此Java提供了多套定时框架↓（仅介绍Timer定时器）
    # Timer定时器
    来源：`java.util.Timer` 
    它是JDK1.3自带的最早的定时器，虽然现在不推荐使用Timer而是更新的**ScheduledExecutorService（线程池），**但仍需了解
    它涉及两个核心类
    ### TimerTask类
    TimerTask类是一个抽象类，该类实现了Runnable接口（Runnable接口就是定义线程实现的接口），该抽象类抽象的是”需要定时执行的任务本身”
    使用：
    1. 需要实现TimerTask抽象类并重写其定义的run()方法「需要定时器执行的代码写在这里」
    ```java
//抽象类不支持Lambda表达式
//抽象类支持匿名内部类
//当然下面↓这个不是匿名内部类（图文不符了说是）
TimerTask task = new TimerTask() {
      @Override
      public void run() {
          System.out.println("任务执行：" + new Date());
      }
  };
    ```
    ### Timer类
    该类是定时器的调度器，也就是接收定时时间及控制抽象类TimerTask的实现类以何种方式运行（是按接收的规定时间循环，还是只运行一次）
    三个启动方法：
    - schedule()：一次性任务「传入TimerTask对象，毫秒数」
    - schedule()：循环任务（以上次执行结束时间为基准，执行时计时器不停，如果某次执行超时，所有任务会延迟）「传入TimerTask对象，开始延迟毫秒数，循环等待毫秒数」
    - scheduleAtFixedRate()：（循环任务以上次执行开始时间为基准，执行时计时器不停，如果某次执行超时，下次执行不会等待而是立即补执行）「传入TimerTask对象，开始延迟毫秒数，循环等待毫秒数」
    取消方法：
    - this.cancel()：取消任务「空参调用」
    ```java
//可以在run方法的重写中调用cancel方法
//使用一个外部的变量作为计数器+if语句，到指定循环次数后取消任务
TimerTask task = new TimerTask() {
    int count = 0;
    @Override
    public void run() {
        count++;
        System.out.println("第 " + count + " 次执行");
        if (count >= 5) {
		        
            this.cancel();  
            System.out.println("任务已取消");
        }
    }
};
timer.schedule(task, 0, 1000);

    ```
    - **Timer对象.cancel()：终止整个计时器「空参调用」**
    - **purge()：清理已取消的任务(任务取消后仍在内存中，调用这个释放内存)「空参调用」**
    使用：
    1. 创建调度器对象
    1. 调用Timer对象的方法并传入TimerTask对象及时间参数
    ```java
public class TimerDemo {
    public static void main(String[] args) {
		    //创建调度器对象
        Timer timer = new Timer();
        
				//需要定时器执行的代码↓
        TimerTask task = new TimerTask() {
            @Override
            public void run() {
                System.out.println("任务执行：" + new Date());
            }
        };

        // 
        timer.schedule(task, 2000);
    }
}

    ```
    ### 缺陷
    Timer定时器之所以不推荐使用是因为它有诸多缺陷
    - 它是单线程的，创建多个Timer对象（定时器）并不会以多线程运行，本该相互独立且不相干的定时器间会相互等待，时间容易打乱
    - 由于是单线程，某个计时器出现异常会把整个程序杀掉（因为整个程序就一个线程）
  守护线程
    注意守护线程和守护进程不是一个概念，更与SB厂商针对Android的流氓保活没有关系，切莫自动联想到安卓保活手段（人家有的保活手段就叫什么守护进程，啊非常误人子弟）
    # 是什么
    守护线程是一种“后台服务线程”，它默默地为其他普通线程（用户线程）提供服务。**当所有用户线程结束时，守护线程会自动结束，不管它有没有执行完。**
    ### 例如
    - **垃圾回收器（GC）**：Java 中最典型的守护线程，默默清理内存
    - **JIT 编译线程**：默默优化代码执行
    # 如何定义
    和正常类定义线程一样，只需要在线程启动前调用该线程对象的`setDaemon(true)`方法将其设置成守护线程
    例子：
    ```java
public static void main(String[] args) throws InterruptedException{
    Thread t = new Thread(() -> {
        while (true){
            try {
                System.out.println("程序正常运行中...");
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    });
    
    
    //设置为守护线程（必须在开始之前，中途是不允许转换的）
    t.setDaemon(true); 
    
     
    t.start();
    for (int i = 0; i < 5; i++) {
        Thread.sleep(1000);
    }
}
    ```
    # 注意
    1. **`setDaemon(true)`**** 必须在 ****`start()`**** 之前调用 ⚠️**
    1. 守护线程会被强行终止，不应该运行任何重要代码
    1. 在守护线程中创建的进程（子进程）默认也是守护线程
  再谈集合类
    我们会发现随着线程的引入，很多原先的集合类都出现了线程不安全的问题（由于这些集合类没有加锁，可能出现同时两个线程更改同一个数据的问题造成冲突）
    其实不仅仅是集合类，还有很多类并不具备线程安全
    这些问题我们将在后面解决（也许）
  (Java 8) 并行流
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
  (Java21)线程构建器
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
  (Java21)虚拟线程
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
[反射](反射/index.md)
  这章不是很重要，主要讲的是JVM的部分工作原理（重点是Class类）
  我认为柏码这章顺序有点问题，所以大幅调整了顺序和标题以及内容（几乎全部重编）
  class类/对象
    说一个新鲜的：为了贯彻一切皆对象的理念，Java的class其实也是一个类，也能创建对象
    # Class类
    Java中Class类定义的是类的模板，其对象存储的是每个类的元数据
    在机器上运行时，开发者每定义一个类，JVM就会创建一个Class类的对象（不一定真的创建，Java采取的是懒加载策略，不使用就不会创建），每个类都对应一个Class类的对象
    以下是Class类的定义↓
    ```java
Class<?> clazz = Dog.class;

clazz.getName();                  // 类名："com.example.Dog"
clazz.getFields();                // 所有 public 字段
clazz.getDeclaredFields();        // 所有字段（含 private）
clazz.getMethods();               // 所有 public 方法
clazz.getConstructors();          // 所有构造器
clazz.getSuperclass();            // 父类是谁
clazz.getInterfaces();            // 实现了哪些接口
clazz.getAnnotations();           // 头上标了哪些注解
clazz.isInterface();              // 是不是接口

    ```
    可以发现Class类中的各种方法都用于存储类的元数据（类的基础信息）
    这就相当于为各个类提供了统一格式的目录，而Class类本身便是这个目录的模板，Class类的对象就是目录本体
    # Class类的对象
    上面基本上已经解释清楚了，Class类的对象隶属于Class类，在运行期间首次使用某个类时由JVM自动创建，每个类只有一个对应的class对象，且后续该类的创建只会参考该class对象，而不会参考原本的类定义
    从硬件角度讲：
    类定义位于硬盘中，首次使用后在内存中创建该类的class对象，后续该类对象的创建只参考内存中的class对象，不会参考硬盘中的类定义（在运行期间将所有类加载进内存后删除源代码，程序仍可运行就能证明这点）
    # 注意
    - 我们常写的类定义中的class和这个没有关系，它仅仅是个关键字（Java的设计没那么妙）
    ```java
//就这东西里面的class
public class Test {
}
    ```
    - Class类的对象不能被开发者手动创建（不能new），只能由JVM自动创建（不过开发者可以通过触发JVM创建class对象来间接创建）
    # 为什么这么设计？
    Java在运行时需要一个知道各类的基础信息，用以分配内存，明确继承关系，进行各种管理… Java选择了和照片exif元数据类似的思路来管理（定义Class类，运行时自动为各类创建Class对象）
  获取class对象
    上节我们了解到，Class类的对象不能由开发者手动创建（不能new，只能由JVM自动创建），但我们可以获取JVM已经创建的class对象
    # 获取class对象的三种方法
    ### `类名.class` 来获取
    ```java
Class<String> clazz = String.class;
Class<Integer> intClass = int.class;  // 基本类型也可以
    ```
    有没有发现这种写法很怪，怪就对了，因为这根本就不是对象调用（调用对象没有这种`类名.对象`的写法），这就是个语法糖（而且class对象也不隶属于用户写的类，它隶属于Class类）
    注意：
    - 不会触发类加载，编译期确定

    ### `对象.getClass()` 方法获取
    getClass()方法用于获取该对象对应类的class对象
    ```java
String str = "hello";
Class<?> clazz = str.getClass();
    ```
    传入参数：空参调用
    注意：由于运行时才会创建对象，因此该方法需要在对象创建后使用
    ### `Class.forName()` 方法获取
    使用Class类的forName方法来获取对应路径类的class对象
    传入参数：相应类路径的字符串
    ```java
Class<?> clazz = Class.forName("java.lang.String");
    ```
    注意：会触发类的静态初始化
    ### 通过**ClassLoader 加载**
    通过ClassLoader类的getSystemClassLoader()方法先获取系统类加载器，然后再调用`loadClass()` 方法获取class对象
    ```java
Class<?> clazz = ClassLoader.getSystemClassLoader()
        .loadClass("java.lang.String");
    ```
    getSystemClassLoader()方法空参调用
    `loadClass()` 方法传入相应类路径的字符串
    注意：不会触发类静态初始化
    # 注意⚠️
    - 基本数据类型虽然不是类，但也有相应的class对象
    - Class类是泛型类，需要在使用的时候明确泛型类型
  Class对象的使用
    我们已经了解了如何获取class对象引用，那么接下来，我们看看class对象中记录了什么信息，有什么方法（研究一下Class类定义）
    # Class类记录的字段
    详细的字段名称这里就不说了，反正一般人谁没事重写Class类的方法啊
    | **类别** | **内容** |
    | --- | --- |
    | 基本信息 | 完整类名、简单类名、修饰符、包信息 |
    | 继承关系 | 父类、实现的接口列表 |
    | 字段信息 | 字段名、类型、修饰符（对应 `Field` 对象） |
    | 方法信息 | 方法名、参数、返回值、异常（对应 `Method` 对象） |
    | 构造器 | 参数列表、修饰符（对应 `Constructor` 对象） |
    | 注解 | 类上标注的注解 |
    | 泛型信息 | 编译时保留的泛型声明 |
    | 其他 | 类加载器引用、类型判断信息（接口/枚举/数组等） |
    # Class类的方法
    ## 获取基本信息
      ```java
getName();          // 完整类名（含包名）
getSimpleName();    // 简单类名
getPackage();       // 所在包
getModifiers();     // 修饰符（int 编码，配合 Modifier 解析）
getSuperclass();    // 父类的 Class
getInterfaces();    // 实现的接口数组
      ```
    ## 获取成员字段的方法
      ### **1. ****`getField(String name)`**
      - **作用**：获取指定名称的**单个字段**
      - **范围**：只能获取 **public** 字段
      - **包含继承**：✅ 能获取本类 + 所有父类的 public 字段
      - **找不到时**：抛 `NoSuchFieldException`
      - 返回值：返回字段值
      - 传参：字段名字符串
      ### **2. ****`getFields()`**
      - **作用**：获取**所有** public 字段（返回 `Field[]`）
      - **范围**：本类 + 所有父类（直至 Object）的 public 字段
      - 传入：空参调用
      - 返回：返回一个 Field 类的对象，它反映此 Class 对象所表示的类或接口的指定公共成员字段。
      ### **3. ****`getDeclaredField(String name)`**
      - **作用**：获取本类声明的**单个字段**
      - **范围**：**任意修饰符**（public / protected / 默认 / private）
      - **包含继承**：❌ 只看本类，父类字段拿不到
      - 返回值：返回字段值
      - 传参：字段名字符串
      ### **4. ****`getDeclaredFields()`**
      - **作用**：获取本类声明的**所有**字段（返回 `Field[]`）
      - **范围**：任意修饰符，仅本类
      - 传入：空参调用
      - 返回：返回一个 Field 类的对象，它反映此 Class 对象所表示的类或接口的指定公共成员字段。
    ## 获取成员方法的方法
      ### **1. ****`getMethod(String name, Class<?>... paramTypes)`**
      - **作用**：获取指定的**单个方法**（需传方法名 + 参数类型列表来精确定位）
      - **范围**：只能获取 **public** 方法
      - **包含继承**：✅ 本类 + 父类的 public 方法，**还包括 Object 类的 public 方法**（如 `toString`、`hashCode`）
      - **找不到时**：抛 `NoSuchMethodException`
      - 传入：方法名，参数类型列表
      - 返回：Method 对象，它是一个“方法描述对象”，封装了目标方法的全部元数据。
      ### **2. ****`getMethods()`**
      - **作用**：获取**所有** public 方法
      - **范围**：本类 + 父类 + Object 类的全部 public 方法
      - 传入：空参调用
      - 返回：Method数组
      ### **3. ****`getDeclaredMethod(String name, Class<?>... paramTypes)`**
      - **作用**：获取本类声明的**单个方法**
      - **范围**：**任意修饰符**（含 private、static、final 等修饰的方法）
      - **包含继承**：❌ 只看本类
      - 传入：方法名，参数类型列表
      - 返回：Method数组
      - 访问私有属性的方法需要调用`setAccessible(true)`这个方法打开强行访问私有权限
      ### **4. ****`getDeclaredMethods()`**
      - **作用**：获取本类声明的**所有**方法
      - **范围**：任意修饰符，仅本类
      - 传入：空参调用
      - 返回：Method 对象，它是一个“方法描述对象”，封装了目标方法的全部元数据。
      - 需要调用`setAccessible(true)`这个方法打开强行访问私有权限
    ## 类型判断
    ```java
isInterface();               // 是否接口
isArray();                   // 是否数组
isEnum();                    // 是否枚举
isAnnotation();              // 是否注解类型
isPrimitive();               // 是否基本类型
isInstance(obj);             // obj 是否为该类实例（相当于 instanceof）
    ```
    ## 注解相关
    ```java
isAnnotationPresent(MyAnno.class);  
// 是否有某注解
getAnnotation(MyAnno.class);        
// 获取注解对象
    ```
    ## 其他
    ```java
getClassLoader();              
// 获取类加载器
getResource("/xx");            
// 获取资源文件
cast(obj);                     
// 安全类型转换（替代强转）
asSubclass(clazz);             
// Class 泛型收窄（判断父类是否一致）
isAssignableFrom(clazz2);      
// clazz2 是否可赋值给当前类
    ```
  通过Class对象创建类的对象
    # Q&A
    Q：什么意思？
    A：Class对象既然是类的元数据，那能不能不使用传统的`new 类型`创建对象，而是直接使用class对象创建类的对象（答案当然是可以）
    Q：蛋疼吧？不用new创建对象，用class对象创建对象有什么意义？
    A：这引入了一个重要特性：动态加载（代码写完不代表写死了，更改一行配置就改变了）（这是引入SpringBoot的一环）
    # 方法1**（JDK 8 及以前）**
    调用class的**`newInstance()`**** **方法获取对象
    ```java
//先获取class对象
Class<?> clazz = Class.forName("com.example.User");
//调用class对象的newInstance()方法获取类对象
User user = (User) clazz.newInstance();  
    ```
    - 类必须有无参构造方法
    - 构造方法必须是 public 的
    - 无参构造器必须存在，否则抛出 `InstantiationException`
    这种方式已经过时，不推荐使用
    # 方法2**（推荐，JDK 9+）**
    省流：先获取构造方法，再创建对象
    先调用class的**`getConstructor()`**** **方法获取该class对应类的构造方法，返回一个 `Constructor` 对象
    然后再调用`Constructor` 对象的`newInstance()`方法来创建类的对象
    ```java
//引入这个包
import java.lang.reflect.Constructor;
//获取class对象
Class<?> clazz = Class.forName("com.example.User");

// 获取无参构造方法
Constructor<?> constructor = clazz.getConstructor();
//创建类的对象
User user = (User) constructor.newInstance();

    ```
    注意⚠️：
    - Java8以前的获取方法之所以被淘汰是因为只支持无参构造，而`getConstructor()`方法既支持无参构造也支持有参构造
    - 如果类没有无参构造，那`getConstructor()`方法必须带参数，`getConstructor()`方法的传入参数为构造方法参数的class对象
    ```java
Class<?> clazz = Class.forName("com.example.User");

// 获取指定参数类型的构造器
Constructor<?> constructor = clazz.getConstructor(String.class, int.class);

// 传入实际参数创建对象
User user = (User) constructor.newInstance("张三", 25);
    ```
    - 如果构造方法为私有的，getDeclaredConstructor()可以强行访问，但需要调用`setAccessible(true)`这个方法打开强行访问权限
    ```java
// 获取class对象
Class<?> clazz = Class.forName("com.example.Singleton");
//获取构造方法
Constructor<?> constructor = clazz.getDeclaredConstructor();  
//突破私有访问限制
constructor.setAccessible(true);  
//创建类的对象
Singleton instance = (Singleton) constructor.newInstance();

    ```
  反射调用方法
    可以通过反射调用实例的方法
    # invoke()方法
    反射依靠使用invoke()方法来调用实例中的方法
    ### 作用
    **在运行时以动态方式调用该方法对象所代表的底层方法**，等价于编译期写死的 `对象.方法名(参数)` 调用，但方法名和参数都是运行时才确定的。
    ```java
// 直接调用
user.sayHello("hi");

// 反射调用 —— 效果完全一致
method.invoke(user, "hi");
    ```
    ### 传入参数
    先看方法签名：
    ```java
public Object invoke(Object obj, Object... args)
        throws IllegalAccessException, IllegalArgumentException, InvocationTargetException
    ```
    参数列表第一个参数：
    - 要调用方法为实例方法时，传入该类的实例对象
    - 要调用方法为静态方法时，传 `null`
    - 要调用方法为私有方法时，传入该类的实例对象（需要事先调用setAccessible(true)以解除访问限制）
    参数列表后面的参数：为要传给底层方法的实参列表
    ### 返回值
    原方法类型不同返回值不同：
    | **底层方法返回类型** | **invoke 返回** | **处理方式** |
    | --- | --- | --- |
    | `void` | `null` | 无需处理 |
    | `int/long/double...` | `Integer/Long/Double...` | 强转对应包装类 |
    | `String/Object...` | 原对象 | 直接强转 |
    | `boolean` | `Boolean` | `(Boolean) result` |
    | `null` 引用 | `null` | 判空 |
    ### 注意
    - 参数一 ：必须是**声明该方法的类（或其子类）的实例**，否则抛出异常：*`IllegalArgumentException`*
    - 后面的参数：如果是无参调用那就**不传或传空数组**
    - 后面的参数：如果需要传nul需要强制类型转换成Object类，否则抛异常*`IllegalArgumentException`*
    - 后面的参数：理论上只支持Object类型，不支持基本数据类型，但实际上基本数据类型会自动装箱成对应包装类，所以可以传
    - invoke方法默认不能访问私有方法，强行访问需要使用`getDeclaredMethod`**+**`setAccessible(true)`详见：[3. getDeclaredMethod(String name, Class<?>... paramTypes)](https://app.notion.com/p/4075a2dd827680f08728cb60e4e017a7#4075a2dd827680b79bfdcb287108e988) 
    ### 可能抛的异常
    ```java
try {
    method.invoke(user, arg);
} catch (IllegalAccessException e) {
    // ① 访问权限不足：私有/受保护方法未 setAccessible(true)
} catch (IllegalArgumentException e) {
    // ② 参数问题：实参数量不对、类型不兼容、obj 类型不匹配
} catch (InvocationTargetException e) {
    // ③ 方法内部抛出的异常被“包装”后抛出
    Throwable 真实异常 = e.getCause(); // 必须用 getCause() 取出
    真实异常.printStackTrace();
}

    ```

    # 示例：调用public方法
    1. 先通过class获取类的对象
    1. 再获取方法
    1. 最后调用方法
    获取对象和获取方法还是前面讲的那几板斧↓
    [通过Class对象创建类的对象](https://app.notion.com/p/4075a2dd827680d7af7ae239a8e92d2f)
     [获取成员方法的方法](https://app.notion.com/p/4075a2dd827680f08728cb60e4e017a7#4075a2dd82768085bc70f0c20d3add54) 
    ```java
import java.lang.reflect.Method;

public class ReflectionDemo {
    public static void main(String[] args) throws Exception {
        // 步骤1：获取 Class 对象
        Class<?> clazz = Class.forName("User"); // 或 User.class / new User().getClass()

        // 步骤2：通过class对象创建实例
        Object user = clazz.getDeclaredConstructor().newInstance();

        // 步骤3：获取 Method 对象
        // getMethod()用于获取实例的成员方法
        Method method = clazz.getMethod("sayHello", String.class);

        // 步骤4：调用invoke方法以调用方法
        // invoke(对象实例, 实际参数...)
        method.invoke(user, "你好，反射！");
    }
}

    ```
  修改类属性
    可以通过反射访问一个类中定义的成员字段也可以修改一个类的对象中的成员字段值
    整体看就几个步骤：
    1. 获取class对象[获取class对象](https://app.notion.com/p/4055a2dd82768017a32be1c6b6b0dd72) 
    1. 调用相关方法获取字段[获取成员字段的方法](https://app.notion.com/p/4075a2dd827680f08728cb60e4e017a7#4075a2dd827680c2b491dfa4f9d08e08) 
    1. 调用set方法对成员字段进行修改
    # set()方法
      注意⚠️：set()方法与getter和setter没有任何关系，前者是反射的API，后者是用于封装私有字段的方法
      ### 方法签名
      `set()` 是 `java.lang.reflect.Field` 类中定义的方法，属于 `Field` 继承自 `AccessibleObject` 的字段操作 API：
      ```java
public void set(Object obj, Object value)
        throws IllegalArgumentException, IllegalAccessException
      ```
      `Field` 还提供了一组针对基本类型的重载方法：
      ```java
void setInt(Object obj, int value)      // int
void setLong(Object obj, long value)    // long
void setDouble(Object obj, double value) // double
void setBoolean(Object obj, boolean value) // boolean
void setFloat(Object obj, float value)  // float
void setShort(Object obj, short value)  // short
void setByte(Object obj, byte value)    // byte
void setChar(Object obj, char value)    // char
      ```
      ### 参数说明
      | **参数** | **类型** | **含义** |
      | --- | --- | --- |
      | **obj** | `Object` | 目标**实例对象**。静态字段传 `null`；非静态字段必须传该 Field 声明类的实例 |
      | **value** | `Object` | 要设置的新值。类型必须与字段类型**兼容**，否则抛异常 |
      ### 返回值
      没有返回值
      ### 注意
      - `set()` 会做**宽松类型匹配（Widening + 装箱）**
      - 调用`setAccessible(true)`即可修改private私有字段和final修饰符的常量
      ### 例子
      ```java
public class User {
    public String name = "张三";
    public static int count = 0;
}

//获取指定字段的Field对象
Field nameField = User.class.getField("name");
//获取指定字段的Field对象
Field countField = User.class.getField("count");

// 1. 非静态字段：必须传实例
User user = new User();
nameField.set(user, "李四");     // ✅

// 2. 静态字段：传 null（推荐）
countField.set(null, 100);       // ✅

// 3. 静态字段：传任意实例也可以（会自动忽略 obj）
countField.set(user, 200);       // ✅ 也能成功，obj 被忽略

// 4. 非静态字段传 null —— 报错
nameField.set(null, "王五");     // ❌ NullPointerException

// 5. 传不相关的类型实例 —— 报错
Cat cat = new Cat();
nameField.set(cat, "赵六");      // ❌ IllegalArgumentException

      ```
    # 注意
    还是那句话，反射可以绕过Java原本的权限限制，甚至修改常量，开发者应该慎重使用越权能力
  (Java9)模块化机制
    # 解决什么痛点
    Java9以前，访问权限由修饰符控制↓
    | 访问修饰符 | 当前类 | 同一个包下的类 | 不同包下的子类 | 不同包下的类 |
    | --- | --- | --- | --- | --- |
    | public | ✅ | ✅ | ✅ | ✅ |
    | protected | ✅ | ✅ | ✅ | ❌ |
    | 默认 | ✅ | ✅ | ❌ | ❌ |
    | private | ✅ | ❌ | ❌ | ❌ |
    但这带来一个问题：包可以被伪造！
    我可以写一个类，然后声明它属于某个包（即使它不属于这个包），这样就突破了传统的访问权限限制了
    例子：
    ```java
//我不是Java.io包的类，但我就声明为Java.io，怎么滴😜
package java.io;
public class Hacker {
    //这里写恶意代码你不炸了😅
}
    ```
    模块化机制则在向前兼容的同时，彻底堵死了通过乱声明包名来绕过权限控制的漏洞
    # 模块化机制原理
    通过在模块根目录创建`module-info.java`文件，并在该文件中定义哪些包可被外部访问
    文件结构示例：
    ```java
demo/                          ← 根目录
├── greeting.module/           ← 模块1：提供功能
│   ├── module-info.java
│   └── com/
│       └── shop/
│           ├── api/
│           │   └── Greeter.java
│           └── internal/
│               └── SecretUtil.java
└── app.module/                ← 模块2：使用功能
    ├── module-info.java
    └── com/
        └── myapp/
            └── Main.java

    ```
    - **`module-info.java`****文件权限控制的粒度是“包”，不能精确到“类”。** 你无法在 module-info 里写 “只导出 `Greeter` 这一个类”，只能声明暴露哪个包
    # `module-info.java`文件
    下面讲解`module-info.java`文件的编辑
    ### **完整语法骨架**
    ```java
[open] [注解] module 模块名 {
    requires  [static] [transitive] 模块名;
    exports   包名 [to 模块1, 模块2];
    opens     包名 [to 模块1, 模块2];
    uses      接口全名;
    provides  接口全名 with 实现类全名;
}
    ```
    ### **七大指令速查**
    **module —— 模块声明**
    ```plain text
module com.shop.payment { }
    ```
    - 模块名是唯一必须写的部分
    - 命名惯例：反转域名（和包名一样），全局唯一
    - 模块体内**什么都可以不写** —— 最小合法模块
    **requires —— 我依赖谁**
    ```java
requires java.sql;                  
// 基本依赖(不能缺少）
requires static jackson.databind;   
// 可选依赖（运行时允许缺席）
requires transitive java.logging;   
// 传递依赖（下游自动继承）
    ```
    - `static`：编译需要，运行可无 → 适合可选功能
    - `transitive`：我的 API 签名用到了某模块的类型时必写 → 下游不用重复声明
    - `java.base` 自动依赖，永远不用写
    **exports —— 开放编译期访问（粒度=包）**
    ```java
exports 包名;                      
// 对所有模块开放的包
exports 包名 to 模块名;      
// 对特定模块开放的包
    ```
    - ⚠️ 只能写**包名**，不能写到类
    - ⚠️ 不递归：`com.shop.api` 和 `com.shop.api.model` 要各写一行
    - 未导出的包 → 外部编译期 import 直接报错
    **opens —— 开放运行期深反射**
    ```java
opens 包名;
// 允许所有模块对该包进行深反射
opens 包名 to 模块名;
// 只允许指定模块对该包进行深反射
    ```
    - `opens` 解决的是运行时反射访问（例如框架反射读取私有字段），不是让外部代码在编译期 `import` 这个包
    - `opens` 和 `exports` 不同：`exports` 面向普通编译期/运行期访问；`opens` 面向反射
    **uses —— 声明我需要哪种服务**
    ```java
uses com.shop.spi.PaymentGateway;
    ```
    - 写在服务消费者模块的 `module-info.java` 中
    - 配合 `ServiceLoader` 查找服务实现；服务接口所在包必须对消费者可访问
    **provides —— 声明我提供哪种服务实现**
    ```java
provides com.shop.spi.PaymentGateway
    with com.shop.payment.internal.AlipayGateway;
    ```
    - 写在服务提供者模块中，`with` 后面是实现类
    - 实现类所在包不必 `exports`；模块系统仍可通过服务机制找到实现
    - 实现类需有 `public` 无参构造器，或提供符合规则的 `public static provider()` 方法
    **open —— 整个模块开放深反射**
    ```java
open module com.shop.payment {
    // 其他 requires / exports / uses / provides 指令
}
    ```
    - `open` 是 `module` 的修饰符，不是独立的模块指令；这里为便于速查，把它作为第七项
    - 它会让模块内所有包都可被其他模块深反射，但不会让这些包在编译期自动可见，也不等于 `exports`
    - `open module` 中不能再单独写 `opens` 指令；若只想开放少数包，应使用普通 `module` 加定向 `opens`

    # 示例
    ```java
module com.shop.payment {
    requires java.sql;
    requires transitive java.logging;
    requires static jackson.databind;

    exports com.shop.api;                    // 对外门面包
    exports com.shop.spi to com.shop.app;    // 定向导出

    opens com.shop.model to spring.core, jackson.databind;

    uses com.shop.spi.RiskChecker;
    provides com.shop.spi.PaymentProvider
        with com.shop.internal.AlipayProvider;
}

    ```
