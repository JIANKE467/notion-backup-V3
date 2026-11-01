---
{
  "id": "4015a2dd-8276-8012-adfb-f2d36337ff1a",
  "url": "https://app.notion.com/p/wait-notify-4015a2dd82768012adfbf2d36337ff1a",
  "created_time": "2026-10-22T08:42:00.000Z",
  "last_edited_time": "2026-10-22T09:22:00.000Z"
}
---

#  wait和notify方法

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
