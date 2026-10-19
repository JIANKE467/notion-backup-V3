---
{
  "id": "3fe5a2dd-8276-805a-9562-e94f4ae93641",
  "url": "https://app.notion.com/p/3fe5a2dd8276805a9562e94f4ae93641",
  "created_time": "2026-10-19T08:03:00.000Z",
  "last_edited_time": "2026-10-19T09:13:00.000Z"
}
---

#  线程的创建和启动

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
