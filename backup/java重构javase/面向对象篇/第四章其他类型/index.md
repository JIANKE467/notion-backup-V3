---
{
  "id": "3b95a2dd-8276-80ec-9e8b-e4d744710f8c",
  "url": "https://app.notion.com/p/3b95a2dd827680ec9e8be4d744710f8c",
  "created_time": "2026-08-11T12:47:00.000Z",
  "last_edited_time": "2026-08-12T14:21:00.000Z"
}
---

#  第四章：其他类型

[枚举类](枚举类/index.md)
  枚举类是一种特殊的类，他提供了多个选项，调用时只能调用选项范围内的
  # 应用场景
  假如我们要存储一个状态，那可以这样写
  ```java
public class Student extends Person implements Study {

    private String status;   //状态，要求是跑步、学习、睡觉这三个之中的其中一种

}
  ```
  但这带来一个问题，外部可以传入任意值↓
  ```java
	Student test = new Student;
	test.status = "666";
  ```
  如果我们想将输入限制到我们规定的几个选项内，就需要用到枚举类
  # 语法
  枚举类不用class，而是用enum表示
  ```java
访问修饰符 enum 枚举类名 {   
    枚举对象一, 枚举对象二, 枚举对象三;    //直接写每个枚举项的名字即可，最后面分号可以不打，但是推荐打上
}
  ```
  - 由于枚举类的底层是普通类，所以枚举类中可以定义成员方法/成员变量/构造方法（这里构造方法只能用private修饰）
  # 使用
  ### 定义变量时
  定义变量时需要将变量引用给枚举类（创建枚举类型的变量）
  ```java
public class Student extends Person implements Study {

    private 枚举类名 status;   //这里要将变量引用给枚举类名

}
  ```
  ### 调用变量时
  使用`枚举类型.枚举对象`调用
  ```java
Student test= new Student;
test.statius= 枚举类型.枚举对象一;
  ```
  # Q&A
  Q：在getter中写if语句也可以限制传入的数据，为什么要这么做？
  A：这种方法也可以实现同样的效果，但无法在编译阶段发现错误，使用枚举类则可以
  Q：枚举类的实质是什么？
  A：通过反编译，我们可以发现，枚举类其实是一个继承了`java.lang.Enumd`的`public final`修饰的类，其中每个枚举对象都是该类的一个`public static final`的成员变量
  ```java
//这里使用javap命令对class文件进行反编译得到 Compiled from "Status.java"
public final class com.test.Status extends java.lang.Enum<com.test.Status> {
  public static final com.test.Status RUNNING;
  public static final com.test.Status STUDY;
  public static final com.test.Status SLEEP;
  public static com.test.Status[] values();
  public static com.test.Status valueOf(java.lang.String);
  static {};
}
  ```
[（Java16）记录类型](java16记录类型/index.md)
  Java 14 （预览版），Java16（正式版）中推出了一种新的类：记录类型
  它是用来存储不变的数据的类（它是普通类+final写法的简写）
  # 语法
  使用`record`声明
  ```java
public record 记录类型名() {   //记录类型的写法与普通类不太一样，类名后面需要带一个括号
}
  ```
  - 记录类型内可以自由编写方法（部分特殊方法除外，会自动生成）
  - 记录类型不能被继承，但可以实现接口
  - 记录类型内不可以定义成员变量，只能在括号内定义
  - 可以在括号中直接定义成员变量（该成员变量初始化后将无法被修改）
  ```java
public record TestDat(int a, String b) {  
}
  ```
  - 记录类型会自动生成与成员变量同名的getter方法（自动生成的getter方法，命名方式略有不同，参见[getter有两种命名方式：手写➡️get + 首字母大写的成员变量名自动生成➡️首字母大写的成员变量名（但其实从语法上讲 命什么名都行）](https://app.notion.com/p/3b15a2dd82768045b4e0d71b634b95d7#3ba5a2dd827680f7b345d644a168d96a) ）
  ```java
TestData test = new TestData(1,"测试");
test.a(); //这个方法是自动生成的
test.b(); //这个方法是自动生成的
  ```
  - 记录类型会自动生成 toString() 方法（并且自动重写成了：打印对象的所有成员变量及其值）[toString()方法](https://app.notion.com/p/3b45a2dd827680fea73cda9dfdc888a1#3b85a2dd82768066b9aad0b03197c98a) 
  - 记录类型会自动生成equals方法（并自动重写成了：比较两个对象的值 而非引用）[equals()方法](https://app.notion.com/p/3b45a2dd827680fea73cda9dfdc888a1#3b85a2dd82768036b7fbf1e72cb33944) 
  - 如果自动生成的方法不能满足需求，也可以直接在记录类型中重写对应的方法进行覆盖
  - 由于记录类型是不可修改的，所以记录类型内不能编写setter方法

  # Q&A
  Q：记录类型本质是什么？
  A：本质上在编译之后也是一个普通的类，不过是final且继承自`java.lang.Record`抽象类的，它会在编译时，会自动编译出 `public get` `hashcode` 、`equals`、`toString` 等方法。
[（Java16）密封类](java16密封类/index.md)
  密封类和`final`关键字一样，都是用来限制类的继承的
  不过它们存在一定区别
  密封类可以指定继承
  final修饰的任何类都不能继承
  # 语法
  ```java
public sealed class 密封类名 permits 允许继承的子类{   
//在class关键字前添加sealed关键字，表示此类为密封类型
//permits后面跟上允许继承的类型，多个子类使用逗号隔开

}
  ```
  - 密封类可以用于普通类，接口，抽象类（几乎所有类）
  - 必须有子类继承，且不能是匿名内部类或是lambda的形式（这些内容会在下一章介绍）
  - `sealed`写在原来`final`的位置，但是不能和`final`、`non-sealed`关键字同时出现，只能选择其一
  - 继承的子类必须显式标记为`final`（任何人都不能继承）、`sealed`（密封）或是`non-sealed`（解除密封）类型。
  父类标准声明格式如下：
  ```java
public sealed [abstract] [class/interface] 类名 [extends 父类] [implements 接口, ...] permits [子类, ...]{
		
}
  ```
  子类标准声明格式如下：
  ```java
public [final/sealed/non-sealed] class 子类 extends 父类 {   //必须继承自父类
			//final类型：任何类不能再继承当前类，到此为止，已经封死了。
  		//sealed类型：同父类，需要指定由哪些类继承。
  		//non-sealed类型：重新开放为普通类，任何类都可以继承。
}
  ```
