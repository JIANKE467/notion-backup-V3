---
{
  "id": "3aa5a2dd-8276-807d-beb3-eeb5e7ff1de5",
  "url": "https://app.notion.com/p/3aa5a2dd8276807dbeb3eeb5e7ff1de5",
  "created_time": "2026-07-27T14:10:00.000Z",
  "last_edited_time": "2026-08-11T12:47:00.000Z"
}
---

# 2️⃣ 面向对象篇

[第一章：类与对象](第一章类与对象/index.md)
  在面向对象编程中有对象，类，方法的概念
  # 对象
  对象 = 现实世界中某个“具体的东西”，在程序里的表示
  如：狗，桌子，人
  # 类
  类=对象的模板，在Java中，类就像是模具，而对象就是用模具做出来的月饼🥮
  ### 类和对象的关系
  先有类（模板）再有对象（产品），在Java中，对象是通过 `对象 = new 某个类()` 创建出来的
  ☞一个类可以对应多个对象
   ☞一个对象只属于一个类
  # 方法
  方法 = 定义在类里的“功能 / 动作”
  如果说对象是一条狗，那类就是制造狗的模板，方法就是狗的颜色/体重/品种…（每种分别对应一个方法）
  类定义与对象创建
    # 类创建
    在src目录下，创建一个新的.java文件，就是创建了一个新的类，也可以先在src下创建包再在包里创建.java文件（在SRC下创建是因为编译器默认在SRC目录读取源码，在bin目录输出编译，lib放第三方库）
    # 类定义
    语法
    ```java
修饰符 class 类名{
成员变量;
成员方法;
...
}
    ```
    - 类只有创建对象后才会实例化
    # 对象创建
    ```java
类名 对象名 = new 类名(传入参数)；
    ```
    - 创建对象时传入的参数是传给构造方法的
    # 匿名类
    - 匿名类是类定义+对象创建一步完成
    - 匿名类由于没有名字无法二次调用
    - 匿名类需要继承父类或实现接口才能使用（）
    语法
    ```java
类名 对象名=  new 类名(传入参数){
成员变量;
成员方法;
...
};
    ```
  对象的调用
    # 语法
    ```java
对象名.属性
    ```
    例：
    ```java
Animal.color=blue;
    ```
    # 注意
    - 对象名存储的是一个引用，而非对象本体
    - 数据类型分：基本数据类型，引用类型（开发者定义的所有“类”都是引用类型，以引用类型定义的变量只存储引用）（类似于指针）
    - 以引用类型定义的变量允许空引用（不推荐）（Java没有空指针检查，因此可以通过编译，但可能会在运行时报错）↓
    ```java
Animal a=null;
    ```
    - 普通变量使用前需要初始化，但对象中的变量不需要（JVM在创建对象时会自动初始化）
    - 同一作用域下，变量名不允许重复，即使所属的类不同（对象本质就是存储引用的变量）
  方法的创建与使用
    # 方法定义
    ```java
返回值类型 方法名(传入参数) {
		方法体...
}
    ```
    - 命名规范：小驼峰（多个单词）/ 全小写
    - 方法类似于函数，通过参数传入数据（多个参数用逗号隔开），通过返回值return传出参数
    # 方法调用
    ```java
对象名.方法名(参数);
    ```
    # 注意
    - 方法定义时的参数叫形式参数，运行时实际传入的叫实际参数
    - return后会退出方法，不能在return后编写代码
    - 如果方法的返回值类型不是void，就必须return
    - 没有要返回的值时可以直接写`return;`
    - **方法内操作的是传入参数的副本，不会改变原参数**
    - **如果传入的参数是引用类型，那方法内将直接操作原数据而不是副本**
    - **形参名不一定要和实参名一样，形参只作用于方法内↓（以下这两种都是可以的）**
    ```java
/* 形参名与实参名一致✅ */
//方法
void dog (int a){
}
//调用
xxx.dog(a);

/* 形参名与实参名不一致✅ */
//方法
void dog (int b){
}
//调用
xxx.dog(a);
    ```
    - 方法可以直接使用其所在类的成员变量
    ```java
public class Student{
  Sring name; //成员变量
  
  void a(){
  System.out.prinln("我是"+name);
  }
}
    ```
  就近原则和this关键字
    # 就近原则
    与c语言相同，当有同名变量时，优先使用最近的那个
    Q：为什么能定义同名变量？
    A：不能在同一作用域定义同名变量，但作用域不同是可以的
    举个例子：
    ```java
int a；
void ssbn（）{
	int a；
	a=1；
	System.out.println(a);
}
    ```
    ↑打印a变量时读取离得最近的，如果局部变量没有定义，则使用稍远的那个
    # this关键字
    对于局部变量和全局变量同名的情况，this关键字可以指定使用当前对象下的变量，而不是就近原则
    语法
    ```java
this.变量名
    ```
    例
    ```java
int a；
void ssbn（）{
int a；
a=1；
System.out.println(this.a);
}
    ```
  方法的重载
    ### 方法重载
    - 同一个类中，定义了多个同名的方法，这些方法有相似的功能
    - 每个方法有**不同的参数类型和形参**，这些同名的方法，构成了重载关系
    总结：同一个类中，方法名相同，参数类型不同，或顺序不同，就构成重载
    不看参数名，具体匹配值是用类型匹配的
    **Java特性：多个方法可以重名，调用时编译器会自动选择对应的那个方法（如果没有对应的，会触发自动格式转换，找最接近的）**
    （如果同时匹配到1个以上的方法，编译器会报错）
    ### 注意⚠️
    - 方法不调用就不会执行
    - 方法不能嵌套定义（可以递归）
    - 调用方法会优先调用形参和实参对应的，如果没有才会隐式转换
    - return作用：1. 结束方法  2. 将结果返回给调用处
    - void作用 ：没有返回值
  方法的互相调用
    除了外部调用，同一类下的方法也可以相互调用
    但有几点需要注意：
    1. 不能循环调用
    1. 可以递归调用（自己调用自己），但要注意设置出口
  构造方法
    # 构造方法（构造器）
    用来实现创建类时，按预设（按定义）自动初始化数据，不用像以前一样手动赋值或手动调用初始化函数
    定义语法：
    ```java
修饰符 类名(参数列表) {        
// 初始化代码    
}
    ```
    **注意**⚠️
    - **构造方法没有返回值，也不定义返回值类型**
    - **构造方法是创建类时自动执行的，无法从外部手动调用（但可以被子类手动调用）**
    - **构造方法的方法名必须与类名完全一致**
    - 构造方法也允许重载
    - 构造方法只能初始化成员变量，不能修改其他方法内的变量
    - 构造方法内定义的变量生命周期=该构造方法的生命周期
    调用语法：
    **无需手动调用，构造方法会在创建对象（调用类）时自动执行**
    # 空参构造（空参构造器）
    - 如果未定义构造方法，Java会自动添加一个空参构造
    - 如果定义了构造方法，Java不会自动添加空参构造
    - **使用构造方法（构造器）时，建议同时再写一个空参的构造器，避免创建对象时未传入参数报错**
    ```java
class SSBN {
int a;
  //有参构造↓
  SSBN (int a){
  a=1;
  }
  //空参构造↓
  SSBN(){
  }
}
    ```
    # 构造方法重载中调用（构造方法调用另一个构造方法）
    通过this关键字实现在一个构造方法中调用另一个构造方法
    前提：这两个构造方法是重载的关系
    ```java
this(参数);
    ```
    # 给构造方法传参
    在创建对象时传入的参数就是构造方法的参数
    ```java
Person p = new Person("Alice", 25);
    ```
    # 执行顺序
    很多人以为创建对象后会先执行构造方法，这不完全对
    在执行构造方法前还需要先执行成员变量初始化和执行初始化代码块（按照下面的顺序）
    1. 成员变量声明时初始化
    1. 初始化代码块
    1. 构造方法
    详见：[方法/初始化顺序](https://app.notion.com/p/3ae5a2dd827680dd9ff1f25c2863566b)
  静态变量和方法
    # 词意解释
    静态对应动态，在Java中有以下含义
    动态：每新建一个对象都要单独存储一份成员变量，不同对象的成员变量相互独立**（变量操作只在对象内生效，在对象间隔离）**
    静态：如果成员变量是静态的，每新建一个对象不会再次存储该成员变量，而是所有对象共用**（变量操作在对象间不隔离）**
    # 标准解释
    **Java中普通变量是属于对象的，不属于类（这个说法很抽象，普通变量定义在类中居然不属于类）**
    **静态变量属于类，而不属于对象**
    # 注意
    - 普通方法可以获取类中的成员变量，**静态方法无法获取成员变量（因为他不属于对象）**
    - **静态方法可以获取静态变量**
    - 静态变量随着类一起加载，而不随着对象一起加载

    # 调用
    可以使用`类名.静态成员名`调用
    ```java
类名.方法名
类名.变量名
    ```
    也可以通过对象调用（不推荐）
    ```java
对象名.方法名
对象名.变量名
    ```
    还可以通过静态导入调用
    静态导入：Java 5 引入的一种语法，它允许你**直接使用其他类中的静态变量或静态方法，而不用写类名**
    ```java
import static 包名.类名.静态成员名;
    ```
    # 批判Java
    既然都说了，静态成员属于类不属于对象
    那为什么又允许通过对象访问静态成员，然后又打个括号说不推荐（这能起到0个代码简化作用）
    纯纯Java老毛病：语法逻辑混乱
[第二章：包和访问控制](第二章包和访问控制/index.md)

  包声明和导入
    # 包的作用
    包用来给类分类，大项目有很多的类，这时我们可以使用包将功能类似的类放到一个包中
    # 包的命名
    建议使用域名反写来命名
    ```java
com.baidu
    ```
    ### 注意⚠️
    - **当一个类加入包中后，*****需要在类的最上面添加package关键字来指明当前类所处的包***
    ```java
package com.test;   //在放入包中，需要在类的最上面添加package关键字来指明当前类所处的包

public class Main {   //将Main类放到com.test这个包中
    public static void main(String[] args) {

    }
}
    ```
    # 包的导入
    > **使用同一个包下的类，不需要导入包**
      **使用不同包下的类需要先导入包（使用import关键字）**
    ```java
package com.test;

import com.test.entity.Person;   //使用import关键字导入其他包中的类

public class Main {
    public static void main(String[] args) {
        Person person = new Person();   //只有导入之后才可以使用，否则编译器不知道这个类从哪来的
    }
}
    ```
    - 可以使用`*`表示导入这个包中全部的类
    - Java中会默认导入`java.lang`这个包下的所有类（所以println等常用方法无需导入也能使用）
    - 主方法一般这样简写`public static void main(String[] args) `，但如果发生歧异（在当前包里创建了String类），就需要写全来显示声明`public static void main(java.lang.String[] args) `
    - **在调用方法/变量时，如果不声明包名，则默认为在当前包下寻找（不声明类名，默认在当前类下寻找）**
    - Java 5 引入了静态导入，它允许你**直接使用其他类中的静态变量或静态方法，而不用写类名**
      ```java
import static 包名.类名.静态成员名;
import static 包名.类名.*;  //可以使用*通配符导入所有静态成员
      ```
    # 吐槽
    Java为什么允许创建名叫Sring的类啊？这下好了，又多一个特性
    想保持逻辑统一性你就让他把主方法写全呀，现在主方法已经有三种写法了（难绷）
  访问权限控制
    Java通过访问控制修饰符，来控制方法，包，类，以及变量的访问权限
    - `private` - 私有，标记为私有的内容无法被除当前类以外的任何位置访问。
    - `什么都不写` - 默认，默认情况下，只能被类本身和同包中的其他类访问。
    - `protected` - 受保护，标记为受保护的内容可以能被类本身和同包中的其他类访问，也可以被子类访问
    - `public` - 公共，标记为公共的内容，允许在任何地方被访问。
    | 访问修饰符 | 当前类 | 同一个包下的类 | 不同包下的子类 | 不同包下的类 |
    | --- | --- | --- | --- | --- |
    | public | ✅ | ✅ | ✅ | ✅ |
    | protected | ✅ | ✅ | ✅ | ❌ |
    | 默认 | ✅ | ✅ | ❌ | ❌ |
    | private | ✅ | ❌ | ❌ | ❌ |
    # 注意
    - 创建普通类不能是`private`权限（外部没办法访问）
    - 如果类中存在静态方法/变量，可以通过静态导入，直接调用该静态方法/变量（无需创建对象）
[第三章：封装，继承，多态](第三章封装继承多态/index.md)
  类的封装
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
    # 例子
    定义：
    ```java
public class Student {
    // 私有字段 —— 封装的核心
    private String name;
    private int age;
    private double score;

    // ========== name 的 getter/setter ==========
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    // ========== age 的 getter/setter ==========
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    // ========== score 的 getter/setter ==========
    public double getScore() {
        return score;
    }

    public void setScore(double score) {
        this.score = score;
    }
}
    ```
    使用：
    ```java
public class BasicDemo {
    public static void main(String[] args) {
        Student student = new Student();

        // 通过 setter 赋值
        student.setName("张三");
        student.setAge(20);
        student.setScore(92.5);

        // 通过 getter 取值
        System.out.println("姓名: " + student.getName());  // 张三
        System.out.println("年龄: " + student.getAge());   // 20
        System.out.println("成绩: " + student.getScore()); // 92.5
    }
}
    ```
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
  类的继承
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
  顶层Object类
    除非手动指定要继承的类，否则所有类都默认继承Object类
    换一种说法，所有类的顶层都是Object类
    # 重要特性
    > 方法参数如果是父类类型，那么可以接收这个父类本身的对象，也可以接收所有子类对象。
    人话：如果一个方法希望传入一个父类的对象，那传入子类的对象也是允许的
    ```java
/*方法*/
void main (Father a){
}//方法期望传入父类对象
    ```
    ```java
/*父类*/
public class Father{
}

/*子类*/
public class Son extends Father{
}
    ```
    ```java
/*方法调用*/
对象名.test(new Father()); //✅方法传入父类对象
对象名.test(new Son()); //✅方法法传入子类对象
    ```
  （java16）类型判断模式匹配
    # 本节介绍`instanceof`关键字
    `instanceof`用于判断某对象是否属于某类，及其子类
    语法：
    ```plain text
对象 instanceof 类名
    ```
    返回结果是：
    - `true`：是这个类型
    - `false`：不是这个类型
    # 应用
    我们可以基于instanceof关键字，做一个简单的类型路由（对于同一个父类下的不同子类的对象采取不同的处理逻辑）
    ```java
/*父类*/
public class Animal{
}

/*子类1*/
public class Dog extends Animal{
} 

/*子类2*/
public class Cat extends Animal{
} 
    ```
    ```java
/*类型路由*/
void test(Animal x){
	if(x instanceof Dog){
	System.out.println("大狗狗，是狼");//如果对象来自dog类型，则显示这句话
	}else if(x instanceof Cat){
	System.out.println("圆头耄耋");//如果对象来自cat类型，则显示这句话
	}
	
}
    ```
    - 关于为什么要求传入Animal类，但却可以传入子类dog和cat类，请参考上一节的内容
    - 由于test方法使用animal类来接收参数，传入的dog和cat类的对象会自动变成Animal类（把对象引用给了Animal类），因此是无法使用Dog和cat类中的属性的（父类看不到子类内容），如果需要使用子类中的属性则要强制类型转换成原来的类⬇️
    ```java
void test(Animal x){
	if(x instanceof Dog){
	Dog y = (Dog)x;
	
	调用dog属性...
	
	}else if(x instanceof Cat){
	Cat z = (Cat)x;
	
	用cat属性...
	
	}
	
}
    ```
    # Java16新特性
    对于上面需要强制类型转换的问题，Java 16做了简化（可以直接在类名后跟变量名，系统会自动帮你强制转换）（变量名用于接收强转后的引用）
    ```java
void test(Animal x){
	if(x instanceof Dog y){
	
	调用dog属性...
	
	}
    ```
  方法/变量的重写
    注意不要与方法的重载搞混淆：方法重载是多个同名的不同参数方法，方法的重写是子类重写父类的方法。
    # 方法重写：
    👉 子类重新实现父类中已经存在的方法，从而改变或扩展其行为。
    ### 语法
    ```java
class 父类 {
    返回值类型 方法名(参数列表) {
            // 原方法    }}
class 子类 extends 父类 {
    @Override
    返回值类型 方法名(参数列表) {
            // 新实现    }}
    ```
    1. **方法名、参数，返回值类型必须与父类方法完全相同**
    1. 访问权限不能变小「权限变小会在多态的时造成逻辑冲突：」
    1. 不能重写 private（私有） 方法
    1. 不能重写 final（不可修改） 方法
    1. static（静态） 方法不能被重写
    1. @Override要写在方法重写的第一行
    1. 使用重写方法还是原有方法取决于创建的是父类对象还是子类对象（如果创建的是子类对象优先调用子类重写的方法，但可使用`super.方法`调用父类方法）
    `@Override `的作用：是虚拟机注解（不是注释），这会告诉编译器这个方法是用来“重写父类方法”的**（不写@override注解也能实现重写效果，只是编译器不会帮你检查问题）**
    # 同名变量（变量重写）
    Java可以在子类中定义和父类同名的变量（类似于方法重写）
    - 与方法重写不同的是，使用重写变量还是原有变量不取决于创建的对象的类型，而是取决于该变量属于父类还是子类（可以在子类对象中调用父类变量，不能在父类对象中调用子类变量）
    # 要点总结：
    取类中的变量看的是编译时类型（变量属于哪个类）
    用类中的方法看的是运行时类型（哪个类创建的对象）
    # 拓展
    ### equals()方法
    equals（）方法：用于判断两个对象的值是否相等（默认是比较是否为同一个对象）
    这就是equals（）源码：
    ```java
public boolean equals(Object obj) {
    return this == obj;
}
    ```
    - 使用该方法需要重写equals()（不重写默认是比较两个对象的“指针”是否相同）
    - 另外，String类型重写了equals（）方法，所以可以直接使用`字符串变量1.equals（字符串变量2）`来比较字符串内容（返回true或false）
    - 所有类都继承了该方法
    Q：就这点？为什么不交给开发者自己实现？
    A：这里讲的根本就不是基础语法，而是Java“预制”的模块
    ### toString()方法
    toString()方法：将对象转换为字符串，一般与println()一起使用用来打印“引用”（并不是严格意义上的引用）
    - 所有类都继承了该方法
    - 使用该方法需要重写toString()（不重写，默认输出包名+类名+哈希标识，人看不懂）
    - 该方法一般用于实现日志
  抽象类
    # 抽象类
    抽象类，顾名思义，它是对一个类的抽象表达（只表明了类的大概意思，缺少部分细节）
    抽象类是使用`abstract`修饰的类，它不能被实例化（不能创建对象）
    ```java
public abstract class Test{
}
    ```
    - 抽象类不是具体的类定义，它只是一个类的抽象模板，它的作用就是被子类继承
    - 抽象类中可以写普通方法/抽象方法，其中抽象方法必须被实现（重写）
    - 抽象类不能实例化
    - 抽象类的子类也可以是抽象类
    - 抽象类的访问权限不能是`private`
    一般来说，抽象的事物就会放到抽象类里，如猫狗都属于动物，动物并不是一个具体的东西，那就可以先定义一个名叫动物的抽象类，具体的猫狗则用来实现子类
    # 抽象方法
    ```java
public abstract void test(){
}
    ```
    - 抽象方法只有方法头，没有方法体
    - 抽象方法只能存在于抽象类中
    - 抽象方法必须被实现（子类是普通类，则需要子类实现。子类是抽象类，则需要子类的子类实现）（重写就是实现）
    # 抽象类与接口的区别
    抽象类可能实现了部分方法，它是一个类的半成品
    而接口完全不实现任何方法，它只有方法的定义，它是对一个具体功能的描述
  接口
    # 接口
    接口不是一种类（没有class）
    接口比抽象类更抽象，抽象类中还可以实现部分方法，接口中不会实现任何方法
    接口只描述了某一具体功能，不含任何细节（静态的除外）
    接口使用关键字`interface`修饰
    ```java
public interface Test { 
}
    ```
    - 在接口中定义方法会被自动添加public和abstract两个修饰符（Java会默认添加这两个修饰符，无需手写）
    - 接口也不能实例化
    - 接口中不允许存在成员变量和成员方法（只能有方法定义）
    - 接口中定义的方法只能是public权限（必须让子类能看到才能实现）
    # 接口实现
    接口不通过继承实现，而是通过关键字`implements`实现
    ```java
public class Student extends Person implements 接口名{ 
}
    ```
    另外，接口可以同时实现多个
    ```java
public class Student extends Person implements Study, A, B, C {  //多个接口的实现使用逗号隔开
  
}
    ```
    # 将对象引用给接口
    可以将对象引用给接口，和多态一样，此时对象只能使用接口中定义过的方法，不能使用类中有但接口中未定义过的方法
    - 将对象引用给接口后，可以使用强制类型转换将其类型转换回对象原本的类型（向下转型）
    # 接口继承
    - 接口不能被类继承，但接口可以被接口继承，并且接口支持多继承
    ```java
public  子接口 extends 父接口A,B,C {
}
    ```
    - 接口的继承其实就是接口功能融合
  （Java8）接口的默认和静态方法
    # 接口的默认实现
    相较于先前接口中只能写方法头，从Java8开始接口添加了以下新特性
    - 可以写方法的默认实现（用default关键字修饰）
    ```java
public interface Study {
    default void test() {   //使用default关键字为接口中的方法添加默认实现
        System.out.println("我是默认实现");
    }
}
    ```
    - 如果方法在接口中有默认实现，则子类中可以不实现（不强制）
    - 可以写静态方法和静态变量
    # 调用接口中的静态成员
    语法：
    ```java
接口名.成员名
    ```
  （Java9）接口中的私有方法
    从Java9开始，接口多了如下特性：
    - 允许在接口内定义private方法，该方法只能被接口中的默认方法使用（静态方法不能使用private修饰的方法）
    - private关键字可以和static关键字连用
[第四章：其他类型](第四章其他类型/index.md)
  枚举类
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
  （Java16）记录类型
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
  （Java16）密封类
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
