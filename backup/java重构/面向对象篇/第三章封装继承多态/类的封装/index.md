---
{
  "id": "3b15a2dd-8276-8045-b4e0-d71b634b95d7",
  "url": "https://app.notion.com/p/3b15a2dd82768045b4e0d71b634b95d7",
  "created_time": "2026-08-03T13:25:00.000Z",
  "last_edited_time": "2026-08-12T14:09:00.000Z"
}
---

#  类的封装

类的封装就是将类封闭起来，不让外部直接访问其中的成员
目的：隐藏细节以及输入审查，防止外部直接将错误的值赋给成员变量
方式：使用private修饰成员变量，并使用Getter和Setter方法传入/传出变量的值
# getter语法
### 定义：
```java
public 返回类型 get变量名() {
    return 成员变量;
}
```
- get变量名命名规则：`get + 首字母大写的成员变量名`
  - 这个return可以活用，你甚至可以在返回值里返回一个新建的对象↓（不使用new创建对象，而是使用自定义的方法创建对象）
```java
public class Person {
    private String name;
    private int age;
    private String sex;

    private Person(){}   //将构造方法私有,外部无法使用new关键字创建对象
    
    public static Person getInstance() {   //而是需要使用我们的独特方法来生成对象并返回
        return new Person();
    }
}
```
### 调用：
```java
	类.方法名();
```
# setter语法
```java
public void set变量名(数据类型 变量名) {
    this.成员变量 = 变量名;
}
```
# 注意
- 构造方法必须设为public，否则外部看不到就无法构造了
- setter方法头中定义的变量名最好与成员变量一致（不一致也行，因为该变量作用域仅限该方法）
- getter和setter方法使用static修饰后只能访问静态的成员变量
- getter有两种命名方式：手写➡️`get + 首字母大写的成员变量名`自动生成➡️`首字母大写的成员变量名`（但其实从语法上讲 命什么名都行）
- setter只有一种命名方式（但其实从语法上讲 命什么名都行）
# 单例模式（了解即可，这里不专门说明）
单例模式：全局只能创建和使用一个对象，不能创建更多的对象
利用这个特性：[这个return可以活用，你甚至可以在返回值里返回一个新建的对象↓（不使用new创建对象，而是使用自定义的方法创建对象）](https://app.notion.com/p/3b15a2dd82768045b4e0d71b634b95d7#3b15a2dd827680dab18ecaddefdbf6de) 
可以实现单例模式（这个代码看看大概，会有详细的章节专门解释）
```java
public class Test {
 private static Test instance;

 private Test(){}

 public static Test getInstance() {
     if(instance == null)   
         instance = new Test();
     return instance;
 }
}
```
