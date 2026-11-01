---
{
  "id": "4015a2dd-8276-80dc-a3c5-e1e454d0dfef",
  "url": "https://app.notion.com/p/4015a2dd827680dca3c5e1e454d0dfef",
  "created_time": "2026-10-22T08:11:00.000Z",
  "last_edited_time": "2026-10-22T08:42:00.000Z"
}
---

#  死锁

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
