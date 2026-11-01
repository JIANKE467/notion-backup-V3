---
{
  "id": "4035a2dd-8276-802d-a45f-f4b832714603",
  "url": "https://app.notion.com/p/4035a2dd8276802da45ff4b832714603",
  "created_time": "2026-10-24T08:08:00.000Z",
  "last_edited_time": "2026-10-24T08:43:00.000Z"
}
---

#  守护线程

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
