---
{
  "id": "3ba5a2dd-8276-80ba-8cce-ea65a4ffe676",
  "url": "https://app.notion.com/p/Java16-3ba5a2dd827680ba8cceea65a4ffe676",
  "created_time": "2026-08-12T14:21:00.000Z",
  "last_edited_time": "2026-08-12T15:10:00.000Z"
}
---

#  （Java16）密封类

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
