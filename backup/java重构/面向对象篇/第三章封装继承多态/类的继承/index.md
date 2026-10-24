---
{
  "id": "3b25a2dd-8276-80f3-96e5-da67fc09deb0",
  "url": "https://app.notion.com/p/3b25a2dd827680f396e5da67fc09deb0",
  "created_time": "2026-08-04T13:06:00.000Z",
  "last_edited_time": "2026-08-04T14:41:00.000Z"
}
---

#  类的继承

可以创建一个父类，用子类去继承父类，就可以直接使用父类中非私有的属性，这能有效降低冗余代码
# 继承语法
子类使用`extends`关键字继承父类
```java
public class 子类名 extends 父类名{
    
}
```
`final`关键字表示该类不可被继承
```java
public final class 类名{
    
}
```
# 注意
- 子类可以直接使用父类的非私有方法/变量（不用写父类名）
- 子类可以定义与父类同名的属性（按就近原则访问）
- 当子类与父类属性同名，可以使用super来指定使用父类属性，如：`super.name`
- 但是注意子类无论如何也访问不到“爷类”，即不允许`super.super.xxx`的写法
# 父类参数需要通过子类传入的情况（父类不是空参构造）
由于Java只会将参数传递给new的那个类，而不会考虑他是否有父类
因此
**子类必须在构造方法中为父类的构造方法传入参数（****父类是空参构造时则不用，空参构造允许传入参数为空****）**
也就是所谓的“在子类构造中调用父类构造”
```java
/*父类*/
	public class Person {
    protected String name;   //因为子类需要用这些属性，所以说我们就将这些变成protected，外部不允许访问
    protected int age;
    protected String sex;
    protected String profession;

  	//构造方法也改成protected，只能子类用
    protected Person(String name, int age, String sex, String profession) {
        this.name = name;
        this.age = age;
        this.sex = sex;
        this.profession = profession;
    }

    public void hello(){
        System.out.println("["+profession+"] 我叫 "+name+"，今年 "+age+" 岁了!");
    }
}
```
```java
/*子类*/
public class Student extends Person{
    public Student(String name, int age, String sex) {    //因为学生职业已经确定，所以说学生直接填写就可以了
        super(name, age, sex, "学生");   //使用super代表父类，父类的构造方法就是super()
    }

    public void study(){
        System.out.println("我的名字是 "+name+"，我在学习！");
    }
}
```
我们前面说过：[构造方法是创建类时自动执行的，无法从外部手动调用（但可以被子类手动调用）](https://app.notion.com/p/3ad5a2dd82768038a36ae51e095e3510#3ad5a2dd8276809cbddec75321431590) 
这里就是父类构造被子类手动调用的情况（父类不是空参构造）（用以下方法）
```java
super(参数值1, 参数值2,...);
```
需要注意，这是此时参数的传递方向：
```java
new 子类() → 子类构造方法 → super() → 父类构造方法
```
但初始化顺序依然是：
```java
父类➡️父类构造方法➡️子类➡️子类构造方法
```
# 多态（这里并不细讲）
多态就是将子类创建的对象引用给父类（将子类当作父类使用）
```java
父类名 对象名 = new 子类名（参数）；//这是多态
类名 对象名 = new 类名（参数）；//这是正常创建对象
```
同样的，也可以使用强制类型转换，将一个被当做父类使用的子类对象，转换回子类(前提是他原本就属于那个子类)
```java
public static void main(String[] args) {
    Person person = new Student("小明", 18, "男");
    Student student = (Student) person;   //使用强制类型转换（向下转型）
    student.study();
}
```
