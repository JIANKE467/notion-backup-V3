---
{
  "id": "4025a2dd-8276-8060-b81f-c225260fe478",
  "url": "https://app.notion.com/p/4025a2dd82768060b81fc225260fe478",
  "created_time": "2026-10-23T12:12:00.000Z",
  "last_edited_time": "2026-10-24T08:08:00.000Z"
}
---

#  定时器

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
