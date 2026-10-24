---
{
  "id": "3ff5a2dd-8276-80d4-870e-f60c7c8913cb",
  "url": "https://app.notion.com/p/3ff5a2dd827680d4870ef60c7c8913cb",
  "created_time": "2026-10-20T08:56:00.000Z",
  "last_edited_time": "2026-10-20T09:13:00.000Z"
}
---

#  线程优先级

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
