---
{
  "id": "3fe5a2dd-8276-808c-bfa6-de506976e2f8",
  "url": "https://app.notion.com/p/3fe5a2dd8276808cbfa6de506976e2f8",
  "created_time": "2026-10-19T09:08:00.000Z",
  "last_edited_time": "2026-10-20T08:56:00.000Z"
}
---

#  **线程的休眠/中断/终止**

线程的休眠/中断/终止分别由几个方法控制
# sleep()休眠
`对象.sleep()`静态方法用于让线程从运行状态切换到 `TIMED_WAITING`（限时等待）状态
期间会释放CPU，不释放锁（读写锁什么的）
传入参数：等待时间（单位毫秒）
注意：必须使用**try-catch**捕获异常（当休眠中调用interrupt()方法中断时会抛出异常**`InterruptedException`**）
PS：**`sleep()`**** 期间被**interrupt()**打断，**中断标志会被清除，需要在catch 里要手动`对象.currentThread().interrupt()` 补回来
```java
public class SleepDemo {
    public static void main(String[] args) {
        System.out.println("开始休息...");
        
        try {
            Thread.sleep(2000);          // 当前线程休眠 2 秒
            // TimeUnit.SECONDS.sleep(2); // 更易读的写法
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt(); // 恢复中断状态
        }
        
        
        System.out.println("睡醒了");
    }
}

```
# wait()等待
对象.wait()
# interrupt()中断标志
`对象.interrupt()`是一个中断标记，它提醒线程应该停止了，但不会强行停止线程，线程不做相关处理等于没听见
有三种不同的标记方法
| **方法** | **谁的** | **是否清除标志** |
| --- | --- | --- |
| `t.interrupt()` | 目标线程 t | —（是设置方） |
| `t.isInterrupted()` | 目标线程 t | **不清除**，可反复检查 |
| `Thread.interrupted()`（静态） | **当前线程** | **清除**，一次性检测**csdn.net+1** |
# **stop()停止**
这个方法在jdk1.1就被标记为弃用，原因是stop（）方法不安全，会强制抛出 `ThreadDeath` 异常并解锁它持有的所有锁（强制停止）
线程运行完会自动终止，不需要调用stop()关闭
