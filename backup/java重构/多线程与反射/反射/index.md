---
{
  "id": "4045a2dd-8276-80c8-880f-dcf24242ce85",
  "url": "https://app.notion.com/p/4045a2dd827680c8880fdcf24242ce85",
  "created_time": "2026-10-25T09:25:00.000Z",
  "last_edited_time": "2026-10-26T10:23:00.000Z"
}
---

#  反射

这章不是很重要，主要讲的是JVM的部分工作原理（重点是Class类）
我认为柏码这章顺序有点问题，所以大幅调整了顺序和标题以及内容（几乎全部重编）
[class类/对象](class类对象/index.md)
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
[获取class对象](获取class对象/index.md)
  上节我们了解到，Class类的对象不能由开发者手动创建（不能new，只能由JVM自动创建），但我们可以获取JVM已经创建的class对象
