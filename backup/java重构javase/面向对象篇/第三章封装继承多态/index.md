---
{
  "id": "3b15a2dd-8276-8010-8532-dcdb8a917aa2",
  "url": "https://app.notion.com/p/3b15a2dd827680108532dcdb8a917aa2",
  "created_time": "2026-08-03T13:24:00.000Z",
  "last_edited_time": "2026-08-11T12:38:00.000Z"
}
---

#  第三章：封装，继承，多态

[类的封装](类的封装/index.md)
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
[类的继承](类的继承/index.md)
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
[顶层Object类](顶层object类/index.md)
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
[（java16）类型判断模式匹配](java16类型判断模式匹配/index.md)
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
[方法/变量的重写](方法变量的重写/index.md)
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
[抽象类](抽象类/index.md)
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
[接口](接口/index.md)
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
[（Java8）接口的默认和静态方法](java8接口的默认和静态方法/index.md)
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
[（Java9）接口中的私有方法](java9接口中的私有方法/index.md)
  从Java9开始，接口多了如下特性：
  - 允许在接口内定义private方法，该方法只能被接口中的默认方法使用（静态方法不能使用private修饰的方法）
  - private关键字可以和static关键字连用
