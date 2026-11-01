---
{
  "id": "3bb5a2dd-8276-80dc-adca-f035e98ed32a",
  "url": "https://app.notion.com/p/3bb5a2dd827680dcadcaf035e98ed32a",
  "created_time": "2026-08-13T12:28:00.000Z",
  "last_edited_time": "2026-09-17T11:25:00.000Z"
}
---

# 3️⃣ 面向对象高级


[第一章：基本类型包装类](第一章基本类型包装类/index.md)
  包装类介绍
    Java存在两种数据类型，基本数据类型和引用数据类型
    基本数据类型是按照面向过程的逻辑去设计的，因此无法使用面向对象的特性（如对象/类/接口等）
    包装类就是用来将基本数据类型转换成引用数据类型的
    # 赋值语法
    语法一：创建一个包装类的对象（已弃用）
    语法二：和基本数据类型 赋值语法一致
    语法三：调用`valueOf()`方法赋值
    PS：其中第一 ，三种方法完全等价，第二种方法会给每个变量创建对象，不会使用缓存（见本节最后）[关于缓存](https://app.notion.com/p/3bb5a2dd827680018081d0f360743366#3bb5a2dd8276808ab1f2fefc468984b6) 
    ```java
包装类名 对象名 = new 包装类名(值); //语法一
包装类名 变量名 = 值; //语法二
包装类名 对象名 = 包装类名.valueOf(值); //语法三
    ```
    ```java
//这里以integer（int的包装类）为例
Integer a = 10; //写法一（自动装箱）
Integer a = new Integer(10);  //写法二（已弃用 不推荐使用）
Integer a = Integer.valueOf(10);  //写法三
    ```
    | 基本数据类型 | 对应包装类 | 名称 |
    | --- | --- | --- |
    | int | Integer（注意第一个字母是大写i不是l） | 整形 |
    | byte | Byte | 字节型 |
    | boolean | Boolean | 布尔类型 |
    | short  | Short | 短整形 |
    | char | Character | 字符型 |
    | long  | Long | 长整型 |
    | float  | Float | 浮点型 |
    | double | Double | 双精度浮点型 |
    # 自动装箱/自动拆箱
    自动装箱：基本数据类型的值可以自动类型转换成对应的包装类
    ```java
int a = 10;
Integer b = a;
    ```
    自动拆箱：包装类的值可以自动类型转换成对应的基本数据类型
    ```java
Integer a = 10;
int b = a;
    ```
    > 通过自动拆箱和自动装箱包装类的变量也可以轻松参与运算，而不用手动类型转换
    # 注意
    包装类和包装类之间比较是否相等时，比较的是引用
    ```java
Integer a = new Integer(100);
Integer b = new Integer(100);

System.out.println(a == b);
//运行结果是false
    ```
    包装类和基本数据类型的变量之间比较是否相等时，比较的是值
    ```java
Integer a = new Integer(10);
int b = 10;

System.out.println(a == b); 
//运行结果是true
    ```
    # 原理
    ### 包装类
    包装类利用了封装的思想，将基本数据类型封装成了引用数据类型。
    我们可以通过查看相应类的代码得知，包装类就是把基本数据类型的变量封装到了类里，并提供了可供调用的的方法（以integer为例）
    ```java
public final class Integer extends Number{

.....

	private final int value;  //类中实际上就靠这个变量在存储包装的值
	
	public Integer(int value) {
	    this.value = value;
	}
}
    ```
    # 关于缓存
    Java 对部分包装类对象进行了缓存。自动装箱时，如果值在缓存范围内，可能直接复用已有对象，而不是创建新对象。
    ```java
//使用自动装箱
Integer a = 10;
Integer b = 10;
System.out.println(a == b);
//运行结果是true
    ```
    ```java
//不使用自动装箱
Integer a = new Integer(100);
Integer b = new Integer(100);
System.out.println(a == b);
//运行结果是false
    ```
    - 上面所说的语法1和语法3都是自动装箱 都会使用缓存
    - 语法2 会给每个变量创建对象，不会使用缓存
    - 使用缓存后，多个值相同的变量会被指向同一个对象
    - 缓存只在一定范围内生效，出了缓存范围，将会给每一个变量创建对象。如对于 `Integer`：**默认缓存范围是 ****`-128 ~ 127`**
    # 包装类中的其他方法
    decode()方法：十六进制和八进制的字符串转成十进制
    valueOf()方法：除了传入变量的值外，还可以将字符串转化为字符型（内部）
    toHexString()方法：将十进制转化为其他进制
    略
  特殊包装类
    有两个特殊的包装类上节并没有提及，现在此说明
    这两个数据类型在使用及语法上与其他数据类型没有差异
    # BigInteger包装类（针对超大数）
    BigInteger包装类没有对应的基本数据类型
    在基本数据类型中，long是最大的数据类型，其包装类Long上节课已经提及
    而BigInteger包装类是用于超大数字的数据类型（没有位数限制，取决于机器内存大小）
    # BigDecimal包装类（精确计算小数）
    BigDecimal包装类没有对应的基本数据类型
    我们前面提到浮点类型无法精确计算
    BigDecimal包装类则解决了这个问题，无论多大的数，无论小数点多少位，它都可以精确计算
[第二章：数组](第二章数组/index.md)
  一维数组
    存储相同类型数据集合的数据结构
    # 定义（两种写法）
    ### 写法1（推荐）
    定义一个数组变量：
    ```java
数据类型[] 数组名;
    ```
    ```java
//例子
int[] arr;
    ```
    ### 写法2（和c语法相同）
    ```java
数据类型 数组名[];
    ```
    ```java
//例
int arr[];
    ```
    # 创建数组
    注意⚠️：与C语言不同，Java中的数组并不是基本数据类型，而是一种类，因此使用数组时需要先创建对象
    ```java
数据类型 变量名 = new 数组名[数组长度];
    ```
    ```java
//例
int arr1 = new arr[10];
    ```
    - 当然你也可以不指定数组长度，但这不是动态数组，仍是静态数组（不指定数组长度Java会在运行时根据数据个数创建数组，但不能在数组创建后扩展空间）
    # 初始化
    可以按以下方式初始化
    ```java
类型[] 变量名称 = new 类型[数组大小];
类型 变量名称[] = new 类型[数组大小];  //支持C语言样式，但不推荐！

类型[] 变量名称 = new 类型[]{...};  //静态初始化（直接指定值和大小）
类型[] 变量名称 = {...};   //同上，但是只能在定义时赋值
    ```
    注意⚠️：数组在创建后会被赋默认值；
      如果是基本数据类型➡️赋0或false；
      如果是引用数据类型➡️赋nul
    # 调用
    数组通过下标访问
    ```java
arr1[0]=888;
    ```
    # 其他要点
    1. 数组下标从0开始，而不是1
    1. 由于Java中数组是一种类，因此数组也有一些属性，如：length（长度）
    1. 当前讨论的是静态数组，数组长度在创建后不可修改
    1. 访问数组中的所有数需要使用for循环遍历
    1. 基本数据类型的数组不支持自动拆箱/装箱（需要手动转换类型）
    1. 引用类型的数组支持自动拆箱/装箱
    1. Java不原生支持动态数组，需要手动实现
  多维数组
    这里的多维数组与c一致
    # 定义
    依然有两种写法
    ### 写法1（推荐）
    ```java
数据类型 [][] 数组名;
    ```
    ```java
int[][] arr;
    ```
    ### 写法2（兼容c）
    ```java
数据类型 数组名[][];
    ```
    ```java
	int arr[][];
    ```
    # 访问
    访问与一唯数组一致
    # 其他要点
    与一维数组一致
  可变长参数
    可变长参数是：一个方法可以接数量不固定个参数
    # 语法
    在参数类型后面加 `...`
    ```java
void test(数据类型... 变量名) {
    }
//这里void，test仅做演示，不是一定是void，test
    ```
    这样，调用时可以这样↓
    ```java
test(1, 2, 3, 4, 5);
    ```
    # 注意
    可变长参数本质上是一个数组
    另外,
    主方法中 String[] args代表：这里接收数量不固定的字符串参数（命令行参数）
    ```java
public static void main(String[] args) { }
    ```
    当然，也能写成这样
    ```java
public static void main(String... args) { }
    ```
[第三章：字符串](第三章字符串/index.md)
  字符串类型与char（字符类型）不同，
  字符串类型可以保存多个字符，字符类型只能保存一个字符，
  而且，
  字符串是一种类，而字符类型是基本数据类型

  String类
    String本身也是一个类，只不过它比较特殊，每个用双引号括起来的字符串，都是String类型的一个实例对象：
    ```java
public static void main(String[] args) {
    String str = "Hello World!";
}
    ```
    注意⚠️：使用双引号创建的两个字符串，如果内容相同，JVM会优化为同一个对象
    注意⚠️：使用构造方法创建的两个字符串，内容相同，也不会被优化为一个对象
    # 语法
    ```java
String 变量名;
    ```
    和基本数据类型使用方法一致，不再赘述
    # String类拥有的方法
    String的对象名就是String引号内的字符串
    ### 获取字符串信息
    1. `length()`获取长度
    1. `isEmpty()` 判断是否为空字符串
    1. `isBlank()`判断是否为空或空白
    1. `charAt(i)` 获取第i个字符
    ### 查找字符串
    - `indexOf()`：第一次出现的位置
    - `lastIndexOf()`：最后一次出现的位置
    - `contains()`：是否包含
    - `startsWith()`：是否以某内容开头
    - `endsWith()`：是否以某内容结尾
    ### 比较字符串内容
    - `equals()`：比较内容是否相同
    - `equalsIgnoreCase()`：忽略大小写比较内容
    - `compareTo()`：比较字典顺序
    - `compareToIgnoreCase()`：忽略大小写比较顺序
    ### 截取字符串
    - `substring(6)`：从指定位置截取到结尾
    - `substring(0, 5)`：截取 `[0,5)`
    ### 替换字符串
    - `replace()`：替换所有匹配内容
    - `replaceFirst()`：替换第一个匹配内容
    - `replaceAll()`：使用正则表达式替换
    ### 去除空白
    - `trim()`：去除首尾空白
    - `strip()`：去除首尾 Unicode 空白
    - `stripLeading()`：去除开头空白
    - `stripTrailing()`：去除结尾空白
    ### 转换大小写
    - `toUpperCase()`：转大写
    - `toLowerCase()`：转小写
  StringBuilder类
    # 什么是StringBuilder类？
    由于String类不可修改的特性，每次拼接/截取都会产生新的对象，极大影响了效率
    因此诞生了StringBuilder类
    StringBuilder类和String类一样，都是存储字符串的数据类型，
    但StringBuilder类允许修改存储内容，修改内容不会产生新对象，提高了效率
    # 用法
    注意⚠️：StringBuilder类不能像String一样直接赋值（String直接赋值实际上是语法糖，底层还是new一个对象），需要new一个对象，将要存储的值作为参数传入
    ```java
StringBuilder a = new StringBuilder("hello word")
    ```
    # StringBuilder拥有的方法
    | 方法 | 作用 | 示例 |
    | --- | --- | --- |
    | `append()` | 追加内容 | `sb.append("Hello")` |
    | `insert()` | 在指定位置插入 | `sb.insert(0, "Hi ")` |
    | `delete()` | 删除一段字符 | `sb.delete(0, 2)` |
    | `deleteCharAt()` | 删除指定位置字符 | `sb.deleteCharAt(0)` |
    | `replace()` | 替换一段字符 | `sb.replace(0, 5, "Java")` |
    | `reverse()` | 字符串反转 | `sb.reverse()` |
    | `toString()` | 转换成 `String` | `String s = sb.toString()` |
    | `length()` | 获取当前长度 | `sb.length()` |
    | `capacity()` | 获取当前容量 | `sb.capacity()` |
    | `setCharAt()` | 修改指定位置字符 | `sb.setCharAt(0, 'J')` |
    | `charAt()` | 获取指定位置字符 | `sb.charAt(0)` |
    | `substring()` | 截取字符串 | `sb.substring(0, 3)` |
  正则表达式
    正则表达式用于匹配字符串，避免了为了匹配字符串而写一大堆逻辑
    以下是正则表达式速查表
    | 类别 | 语法 | 含义 | 示例 | 示例含义 |
    | --- | --- | --- | --- | --- |
    | **普通字符** | `abc` | 匹配普通字符 | `abc` | 匹配 `abc` |
    | **任意字符** | `.` | 任意一个字符 | `a.c` | `abc`、`a1c` |
    | **字符集合** | `[abc]` | 匹配 a/b/c 中任意一个 | `[abc]` | `a`、`b`、`c` |
    | **字符范围** | `[a-z]` | a 到 z 任意一个 | `[a-z]` | `a`、`m`、`z` |
    |  | `[A-Z]` | A 到 Z 任意一个 | `[A-Z]` | `A`、`M`、`Z` |
    |  | `[0-9]` | 0 到 9 任意一个 | `[0-9]` | `0`、`5`、`9` |
    | **排除集合** | `[^abc]` | 除 a/b/c 外的字符 | `[^0-9]` | 非数字 |
    | **数字** | `\d` | 一个数字 | `\d` | `0`～`9` |
    | **非数字** | `\D` | 一个非数字字符 | `\D` | `a`、`@` 等 |
    | **单词字符** | `\w` | 字母、数字、下划线 | `\w` | `a`、`A`、`3`、`_` |
    | **非单词字符** | `\W` | 非 `\w` 字符 | `\W` | `@`、`#` 等 |
    | **空白** | `\s` | 空白字符 | `\s` | 空格、`\n`、`\t` |
    | **非空白** | `\S` | 非空白字符 | `\S` | `a`、`1` 等 |
    | **数量** | `*` | 0 次或多次 | `a*` | `""`、`a`、`aa` |
    |  | `+` | 1 次或多次 | `a+` | `a`、`aa` |
    |  | `?` | 0 次或 1 次 | `a?` | `""`、`a` |
    |  | `{n}` | 恰好 n 次 | `a{3}` | `aaa` |
    |  | `{n,}` | 至少 n 次 | `a{3,}` | `aaa`、`aaaa`… |
    |  | `{n,m}` | n～m 次 | `a{2,4}` | `aa`、`aaa`、`aaaa` |
    | **边界** | `^` | 字符串开头 | `^abc` | 以 `abc` 开头 |
    |  | `$` | 字符串结尾 | `abc$` | 以 `abc` 结尾 |
    | **分组** | `()` | 将多个字符组成一个整体 | `(ab)+` | `ab`、`abab` |
    | **选择** | `|` | 或者 | `cat|dog` | `cat` 或 `dog` |
    | **转义** | `\` | 取消特殊含义 | `\.` | 匹配真正的 `.` |
    注意⚠️：
    正则表达式存在双重转义，即部分符号需要转义表达，转义的符号需要双重转义表达
    更多详见：[https://www.runoob.com/regexp/regexp-syntax.html](https://www.runoob.com/regexp/regexp-syntax.html)
  字符串类增强（Java11）
    在Java11后String类增加了一些功能
    ### `strip`方法
    String类型新增了strip方法，他会自动去除字符串的**前后的空格**
    ### stripLeading方法
    String类型新增了stripLeading方法，他会自动去除字符串的**前的空格**
    ### stripTrailing方法
    新增stripTrailing方法，它能自动去除字符串**后的空格**
    ### isBlank方法
    新增isBlank方法，它能识别字符串是否为纯空格组成
    ### repeat方法
    新增repeat方法，它可以让字符串重复排列（传入参数为重复次数）
  文本块（Java15）
    Java15 String类引入了文本块功能，和Python一样，用三引号标识文本块
    ```java
String string = """
					abc
					123
					hello
					Java15
        """;
    ```
    可以在文本块中随意使用特殊符号而不用顾及转义字符，这对内嵌其他语言代码非常方便
    PS：Java15 的文本块实际上是语法糖，实际还是会编译成有转义字符的形式
  Switch模式匹配（Java21/22/25）
    **这节是复制的，而且太新了，有部分还是预览功能，看看就好，不重要**

    前面我们介绍了switch表达式，相比传统的switch语法，它可以非常方便地实现分支判断和结果返回：
    ```java
public static Integer test(String str) {
    return switch (str) {  //直接使用switch表达式的结果作为返回值
        case "A" -> 1;
        case "B" -> 2;
        default -> 0;
    };
}
    ```
    在Java 14中对switch进行了进一步增强，引入了模式匹配，可以直接判断目标类型，此功能最终在Java 21实装。原来我们如果要实现类型判断的分支语句，需要像这样编写：
    ```java
if(obj instanceof String) {
    System.out.println("String");
} else if(obj instanceof Integer){
    System.out.println("Integer");
} else {
    System.out.println("Other");
}
    ```
    现在switc支持模式匹配后，我们可以像这样编写：
    ```java
public static void test(Object obj) {
    String type = switch (obj) {
        case String s -> "String";   //直接在case后写上类型和变量名称即可进行类型匹配
        case Integer i -> "Integer";
        case null -> "Null";   //甚至还可以直接判断null
        default -> "Other";
    };
    System.out.println(type);
}
    ```
    我们注意到，模式匹配中的类型后面必须跟一个变量名字，哪怕我根本就不用它，这似乎有点鸡肋，能否有一种办法省略掉呢？在Java 22之后，我们可以使用`_`下划线来直接取代，表示这是一个后续不会使用的未命名的变量：
    ```java
String type = switch (obj) {
    case String _ -> "String";   //直接使用_表示未命名变量
    case Integer _ -> "Integer";
    case null -> "Null";
    default -> "Other";
};
    ```
    还新增了when守卫条件，对记录类内部成员的类型嵌套匹配
[第四章：内部类](第四章内部类/index.md)

  成员内部类
    成员内部类就是在类内在定义一个类（类嵌套）
    # 注意
    成员内部类和成员方法、成员变量一样，是对象所有的，而不是类所有的，如果我们要使用成员内部类，那么就需要创建对象
    # 定义
    成员内部类的定义就是直接将内部类嵌套进外部类中
    ```java
public class Out {

	public class In{
	}
	
}
    ```
    这没什么可说的
    # 创建对象
    > 创建内部类的对象需要先创建外部类的对象
    ```java
Out a1 = new Out();
Out.In a2 = a1.new In();
    ```
    注意⚠️：创建内部类的对象语法是`Out.In a2 = a1.new In();`，而不是`Out.In a2 = new a1.In();`
      > 要先“打开“外部类对象再创建内部类对象，不能在创建内部类对象的时候扔一个”路径“，因为编译器只允许new后面跟类名，编译器分不清“对象.类类名”这种写法到底是对象还是类
    # 对象调用
    在创建了内部类的对象之后，内部类的对象可以直接被调用，**不需要**写成 `outer.inner.test()` 这种路径式的形式
    ```java
a2.test();
    ```
    # PS
    - 在成员内部类中可以访问到外层的成员变量，而且Java有一个特殊之处：**外部类可以访问内部类的 private 成员**
    - Java的特殊设计——外部类和内部类被视为“一家人”，**外部类可以直接访问内部类的私有成员**
    - 内部类的方法允许与外部类的成员重名，调用时遵守就近原则
  静态内部类
    前面我们介绍了成员内部类，它就像成员变量和成员方法一样，是属于对象的，同样的，静态内部类就像静态方法和静态变量一样，是属于类的，我们可以直接创建使用。
    ```java
public class Test {
    public static class Inner {
       
        }
}
    ```
    ### 注意⚠️
    - 静态内部类不需要创建外部类的对象即可直接创建内部类的对象
    - 静态内部类无法访问外部类的内容（因为整个静态内部类处于静态上下文中，静态上下文中并没有外部类）
  局部内部类
    局部内部类是**在方法中定义的类**
    ```java
public class Outer {
    public void hello(){
        class Inner {    //直接在方法中创建局部内部类
            
        }
    }
}
    ```
    ### 注意⚠️
    - 局部内部类的作用域为该方法
  匿名内部类
    我们知道接口和抽象类是无法实例化的，
    但，
    匿名内部类可以无视这条规则，直接将接口或抽象类实例化
    哎，那又有老铁问了：设计出来接口不让它实例化，现在又搞个匿名内部类实例它，是不是闲的蛋疼？
    这其实是为了**解决“我需要一个只用一次的类，专门为它建一个文件/起个名字太重了，时间长了项目里一堆垃圾类还不知道有没有用”的问题**
    所以我们干掉了类名（匿名）解决了类名维护的问题，将其嵌套在接口/抽象类中（内部类）解决了项目树膨胀的问题
    ### 原理如下
    接口/抽象类想要实例化 必须先实现接口/继承并实现抽象类，再创建对象
    而匿名内部类则可以在创建对象的时候顺手完成接口/抽象类的实现
    匿名内部类 实际上还是抽象类的子类/接口的实现类
    ### 下面用代码说明
    **核心要点：在创建对象的语句后加上花括号（花括号内就是匿名内部类，在此处实现接口/ 抽象类未实现的方法）**
    ```java
//定义一个抽象类
public abstract class Outer{
	public void test ();
}
    ```
    ```java
//用匿名内部类在创建对象的时候顺手完成抽象类的实现
Outer outer = new Outer(){//在new的时候，后面加上花括号，把未实现的方法实现了
	@Override 
	public void test (){
	.....
	}
}

    ```
    ### 注意⚠️
    匿名内部类在new的时候起的名字是对象名 ，而不是匿名内部类的名字，注意别搞混了
    由于匿名内部类没有名字，所以该类无法服复用，但其对象不受影响
    建议将匿名内部类当临时类使用，因为该类无法复用
    # 启发
    原来：接口→实现类→创建对象→`对象.方法`调用/`实现类 对象`作为参数传入
    现在：接口→匿名内部类直接创建对象→`对象.方法`调用/`接口 对象`作为参数传入
    其实就是把接口当普通类用（不过需要匿名内部类）
  Lambda表达式
    这个是匿名内部类的语法糖（不全是）
    先回顾一下匿名内部类：[核心要点：在创建对象的语句后加上花括号（花括号内就是匿名内部类，在此处实现接口/ 抽象类未实现的方法）](https://app.notion.com/p/3db5a2dd8276806190c1d8e1efcba247#3e15a2dd827680188e7cef58a8665457) 
    **如果一个接口中有且只有一个待实现的抽象方法**，那么我们可以将匿名内部类简写为Lambda表达式
    ### 语法
    ```java
Study test = () -> System.out.println("我是学习方法！"); 

//上面的等价于下面的写法

Study test = new Studay(){
	@Override
	public void main(){
	System.out.println("我是学习方法！");
	} 
}
    ```
    
• 标准格式为：`接口名 对象名 = ([参数类型 参数名称,]...) ‐> { 代码语句，包括返回值 }`
    ### 注意⚠️
    - **Lambda表达式只能应用于接口，抽象类不行**
    -  接口内部必须有且仅有一个抽象方法（可以有多个方法，但是必须保证其他方法有默认实现，必须留一个抽象方法出来）
    - Lambda表达式有多种省略写法↓
    ```java


// ① 完整形态：有括号、有类型、有大括号、有 return
c = (String a, String b) -> { return a.length() - b.length(); };

// ② 省略参数类型（编译器根据接口自动推断）
c = (a, b) -> { return a.length() - b.length(); };

// ③ 方法体只有一句时，去掉大括号和 return（必须一起去掉）
c = (a, b) -> a.length() - b.length();

// ④ 只有一个参数时，括号也可以省
Consumer<String> printer = s -> System.out.println(s);

// ⑤ 零个参数：括号不能省
Runnable r = () -> System.out.println("hello");

    ```
    # 要点：
    接口只有一个待实现方法，其匿名内部类可以写成lambda表达式
    依旧是创建对象语句，只不过等号右边换成`(参数列表)->{代码}`
  方法引用
    方法引用是基于上一节Lambda表达式的基础上的
    方法引用就是将一个已在别处实现的方法，直接作为接口中抽象方法的实现（需要方法定义一致）
    ### 用代码说明
    ```java
//接口定义
public interface Study {
    int sum(int a, int b);   //待实现的求和方法
}
    ```
    ```java
//在别处实现的求和方法
public class Other{
	public static int plus(int a, int b){
		return a+b;
		}
}
    ```
    ```java
//用匿名内部类实现接口（Lambda写法）
Studay studay = (int a, int b)->Other.plus(a,b)
    ```
    直接在箭头右侧写上相关方法的引用即可
[第五章：异常机制](第五章异常机制/index.md)
  首先声明：各种的异常，就是不同的异常类 (详见下面各类继承树)
  ```java
Throwable                    ← 异常体系的根
├── Error                    ← 严重错误，不该捕获
│   ├── OutOfMemoryError
│   ├── StackOverflowError
│   └── NoClassDefFoundError
│
└── Exception                ← "异常"主体
    ├── RuntimeException     ← 运行时异常（非受检）
    │   ├── NullPointerException
    │   ├── IndexOutOfBoundsException
    │   ├── ClassCastException
    │   └── ArithmeticException
    │
    └── 其他 Exception 子类   ← 受检异常
        ├── IOException
        ├── SQLException
        └── InterruptedException

  ```

  异常类型

    ### 运行时异常`RuntimeException`
    这种异常可以通过编译器，但运行时会报错，所有的运行时异常都继承自`RuntimeException`
    ### 编译时异常（受检异常）`Exception`
    一般是逻辑错误，无法通过编译器，默认继承自`Exception`类的异常都是编译时异常
    ### 错误
    错误比异常更严重，可能导致严重后果，如：`OutOfMemoryError`内存溢出错误可能导致JVM崩溃
    所有错误都继承自Error类
  自定义异常
    自定义异常就是对异常类的定义，JavaSE自带了700多种异常，但他们是通用的技术性错误，在实际业务中，我们需要更确切的信息表达具体异常信息，如：余额不足，文件过大…
    这就需要我们自定义异常类
    # 语法
    自定义异常实际上就是定义`RuntimeException`或`Exception`或`Error`类的子类
    ```java
public class 自定义异常名 extends 父类异常{
  异常内容...
}
    ```
    # 注意⚠️
    - 不要再异常类体中写异常处理逻辑，虽然这在语法上完全允许，但在设计上一定要避免（设计原则上：异常应该是轻量，只读，无副作用的）
    - 异常类只做异常的传递，具体的处理由另外的模块负责（设计规范，非语法强制）
    ```plain text
异常发生点          异常类（信使）           处理点
┌──────────┐      ┌──────────────┐      ┌──────────────┐
│ throw new├─────→│  携带信息      ├─────→│  try-catch / │
│ MyEx(...)│      │  code、msg 等  │      │  全局处理器    │
└──────────┘      └──────────────┘      └──────────────┘
  抛出异常           只装数据            写处理逻辑

    ```
  异常抛出
    - 异常抛出就是创建异常类的对象
    - 抛出异常（创建对象）时，传入的参数一般是异常信息和异常路径
    - 和return类似，异常抛出后（执行到throw）方法将被终止，后续代码不会执行

    # 手动抛异常
    为了防止传入非法参数，我们可以在业务方法中对参数进行判断，不符合范围则手动抛出异常
    ```java
//业务逻辑
public int test(int a,int b){
	if(b == 0){
		throw new RuntimeException("被除数不能为0");
	}
	return a/b;
} 
    ```
    ### 语法：
    ```java
throw new 异常类名(参数);
    ```
    # 自动抛异常
    除了手动抛异常外，Java还能自动检测一些异常（该能力是由JDK 类库里写的 throw，但对使用者来说“感觉是自动的”）
    自动抛异常不需要开发者手动写throw和判断逻辑
    ### Java能自动检测如下异常：
    1. 空指针
    1. 除0
    1. 数组越界
    1. 类型转换错误
    1. 内存溢出/栈溢出
    1. 数字格式错误
    # throws声明
    `throws` 用于方法声明中，表示该方法**可能抛出的异常**
    ### 语法
    ```java
修饰符 返回类型 方法名(参数) throws 异常类型1, 异常类型2 {
    // 方法体
}
    ```
    ### throws声明的作用
    Java编译器规定了一些受检异常（编译时异常）：
    ```java
Throwable                    ← 异常体系的根
├── Error                    ← 严重错误，不该捕获
│   ├── OutOfMemoryError
│   ├── StackOverflowError
│   └── NoClassDefFoundError
│
└── Exception                ← "异常"主体
    ├── RuntimeException     ← 运行时异常（非受检）
    │   ├── NullPointerException
    │   ├── IndexOutOfBoundsException
    │   ├── ClassCastException
    │   └── ArithmeticException
    │
    └── 其他 Exception 子类   ← 受检异常
        ├── IOException
        ├── SQLException
        └── InterruptedException

    ```
    - ~~**编译器不允许未处理的受检异常（编译时异常）通过编译**~~
    - **编译器强制要求开发者处理受检异常（要么catch捕获，要么throws上抛），否则不能通过编译，但有些受检异常是无法规避的（如：网络未连接，文件找不到），使用throws声明代表我知道可能报错但我选择向上抛**
    - 非受检异常（运行时异常）则不强制要求处理
    # 又可以喷Java了😅
    什么叫编译器强制要求处理受检异常，但有些受检异常无法避免？啊，网络未连接，文件找不到…这种东西怎么看都是运行时异常吧，非得把语法逻辑搞的这么反直觉
    c#，Kotlin，Go人家全部都没有受检异常这一说
    本意是强制处理易恢复项，实际上纯增加工作量，因为受检异常太多了，没写几个逻辑就要处理一个受检异常，而且你不处理就得一直往上抛，上面的每一层都得写throws（方法签名污染）
    如果开发者假处理（只chtch不写逻辑），又会吞异常，非常sb
  异常捕获
    程序出现异常就会逐层上抛，直到JVM，JVM收到任何异常都会终止程序并在控制台打印栈追踪信息，如果要避免程序终止就需要捕获异常
    # 语法
    我们可以将代码编写到`try`语句块中，只要是在这个范围内发生的异常，都可以被捕获，使用`catch`关键字指定需要捕获的异常类型
    ```java
public static void main(String[] args) {

...

    try {    
      可能发生异常的语句...
       
    } catch (异常类型 对象名){   //因为异常本身也是一个对象，catch中实际上就是用一个局部变量去接收异常
				异常处理逻辑...
				
    } 
   
   
    
}
    ```
    - 因为异常本身也是一个对象，catch中实际上就是用一个局部变量去接收异常，方便我们操作
    - catch中捕获的类型只能是Throwable的子类，也就是说要么是抛出的异常，要么是错误，不能是其他的任何类型
    - printStackTrace()方法可以打印异常的栈追踪信息
    - 也可以将catch中的异常类型写成Throwable类，这样就能捕获所有异常了 
    - 异常捕获后可以继续运行后面的代码
    也可以这样（多种异常用共用一种处理）
    ```java
try {    
      可能发生异常的语句...
       
    } catch (异常类型1|异常类型2 对象名){  
				异常处理逻辑...
				
    } 
    ```
    或者是这样（**多重异常捕获**）（多个异常多种处理逻辑）
    ```java
try {    
      可能发生异常的语句...
       
    } catch (异常类型1 对象名1){  
				异常处理逻辑...
				
    } catch (异常类型2 对象名2){
		    异常处理逻辑...
		    
    } ...
    ```
    - 这种需要注意catch的顺序，会先捕获写在前面的异常（如果把父类写在前面，子类写在后面，那子类的异常就会被父类先捕获）
    还可以使用finally，无论是否捕获异常，finally都会执行
    ```java
try {
    //....
}catch (Exception e){
            
}finally {
  	System.out.println("lbwnb");   //无论是否出现异常，都会在最后执行
}
    ```
    - 可以不写catch部分，只写finally部分（发生异常程序终止，但在那之前会执行finally）
  断言表达式
    这节功能太小众了，仅做了解

    **断言**是一种调试机制，用于在开发/测试阶段**验证你对程序状态的假设**——断定某个条件“一定为真”，如果不真，说明代码有 bug，立即报错。
    # 语法
    ```java
assert 布尔表达式;
assert 布尔表达式 : 错误详情信息;  // 带提示信息的写法
    ```
    # 注意
    - **Java 断言默认不启用**，`assert` 语句会被 JVM 直接跳过，写了也不生效
    - 使用断言表达式需要修改JVM参数
    ```java
# 只开启某个类
java -ea:com.example.MyClass MyApp

# 开启所有类（最常用）
java -ea MyApp

# 关闭（默认）
java -da MyApp

    ```
[第六章：常用工具类](第六章常用工具类/index.md)

  数学工具类
    Java语法自带的加减乘除无法满足复杂运算的需求，因此，Java还提供了一些数学工具类供人使用
    # 数学工具类（Math类）
    Math类可以直接调用，不用写包名（Match类属于java.lang包，而编译器会自动【import】引入java.lang包）
    ### 基础数学运算
    | **方法** | **签名** | **说明** | **示例** |
    | --- | --- | --- | --- |
    | 绝对值 | `abs(int/long/float/double a)` | 返回绝对值 | `Math.abs(-5)` → `5` |
    | 最大值 | `max(a, b)` | 返回两数中较大值 | `Math.max(3, 7)` → `7` |
    | 最小值 | `min(a, b)` | 返回两数中较小值 | `Math.min(3, 7)` → `3` |
    | 四舍五入 | `round(double/float a)` | 四舍五入返回 long/int | `Math.round(2.6)` → `3` |
    | 向上取整 | `ceil(double a)` | 向上取整，返回 double | `Math.ceil(2.1)` → `3.0` |
    | 向下取整 | `floor(double a)` | 向下取整，返回 double | `Math.floor(2.9)` → `2.0` |
    | 截断取整 | `rint(double a)` | 取最接近的整数，返回 double | `Math.rint(2.5)` → `2.0` |
    | 符号复制 | `signum(a)` | 返回参数的符号（1.0 / -1.0 / 0） | `Math.signum(-8)` → `-1.0` |
    | 交换/相邻浮点数 | `nextUp(a)` / `nextDown(a)` | 返回相邻的浮点值 | 精度调试用 |
    ### 幂与开方
    | **方法** | **签名** | **说明** | **示例** |
    | --- | --- | --- | --- |
    | 求平方根 | `sqrt(double a)` | 平方根 | `Math.sqrt(16)` → `4.0` |
    | 求立方根 | `cbrt(double a)` | 立方根 | `Math.cbrt(27)` → `3.0` |
    | 求幂 | `pow(double a, double b)` | a 的 b 次方 | `Math.pow(2, 10)` → `1024.0` |
    | 欧几里得范数 | `hypot(x, y)` | √(x²+y²)，不会溢出 | `Math.hypot(3, 4)` → `5.0` |
    | 平方根倒数 | `sqrt(x² + y²)` 类的还有 | — | — |
    ### 指数与对数
    | **方法** | **签名** | **说明** | **示例** |
    | --- | --- | --- | --- |
    | e 的幂 | `exp(double a)` | e^a | `Math.exp(1)` → `2.718...` |
    | e 的幂减 1 | `expm1(double a)` | e^a − 1（小数精度更好） | — |
    | 自然对数 | `log(double a)` | 以 e 为底 | `Math.log(Math.E)` → `1.0` |
    | 以 10 为底对数 | `log10(double a)` | — | `Math.log10(100)` → `2.0` |
    | log(1+x) | `log1p(double x)` | ln(1+x)（小数精度更好） | — |
    ### 三角函数
    | **方法** | **说明** | **备注** |
    | --- | --- | --- |
    | `sin(a)` / `cos(a)` / `tan(a)` | 正弦、余弦、正切 | **参数是弧度**，不是角度 |
    | `asin(a)` / `acos(a)` / `atan(a)` | 反三角函数 | 返回弧度 |
    | `atan2(y, x)` | 返回点 的极角 | 常用于计算角度，避免除零问题 |
    | `toRadians(deg)` | 角度 → 弧度 | `Math.toRadians(180)` → `π` |
    | `toDegrees(rad)` | 弧度 → 角度 | `Math.toDegrees(Math.PI)` → `180.0` |
    | `sinh(x)` / `cosh(x)` / `tanh(x)` | 双曲正弦/余弦/正切 | — |
    ### 随机数
    | **方法** | **说明** | **示例** |
    | --- | --- | --- |
    | `random()` | 返回 `[0.0, 1.0)` 的随机 double | — |
    ### 常数
    | **常量** | **说明** | **值** |
    | --- | --- | --- |
    | `Math.PI` | 圆周率 π | 3.141592653589793 |
    | `Math.E` | 自然常数 e | 2.718281828459045 |
    ### 精度控制
    | **方法** | **说明** | **示例** |
    | --- | --- | --- |
    | `floorDiv(x, y)` | 向下取整的整数除法 | `Math.floorDiv(-7, 2)` → `-4`（`-7/2` 是 `-3`） |
    | `floorMod(x, y)` | 向下取整的取模（结果符号同 y） | `Math.floorMod(-7, 2)` → `1`（`-7%2` 是 `-1`） |
    | `IEEEremainder(x, y)` | IEEE 754 标准的余数 | — |
    | `copySign(magnitude, sign)` | 取第一个数的绝对值 + 第二个数的符号 | `Math.copySign(3, -1)` → `-3.0` |
    | `fma(a, b, c)` | a×b+c（一次舍入，更快更准） | JDK 9+ |
  数组工具类
    在Java中操作数组还得遍历，非常麻烦，因此Java提供了数组工具类用来便捷操作数组
    # 数组工具类（Arrays类）
    Arrays类可以直接调用，不用写包名（Arrays类属于java.util包，而编译器会自动`import java.util.*`）
    ### 打印/转字符串
    | **方法** | **说明** | **示例** |
    | --- | --- | --- |
    | `toString(arr)` | 一维数组转字符串，格式 `[1, 2, 3]` | `Arrays.toString(new int[]{1,2})` → `[1, 2]` |
    | `deepToString(arr)` | **嵌套数组**转字符串，递归处理 |  |
    PS：查看数组要么遍历，要么`toString(arr)` 不能直接println，否则会显示哈希地址
    ### 排序
    | **方法** | **说明** |
    | --- | --- |
    | `sort(arr)` | 升序排序（基本类型用**双轴快排**，对象用 **TimSort**）**oracle.com** |
    | `sort(arr, from, to)` | 只排序 `[from, to)` 范围 |
    | `sort(objArr, comparator)` | 对象数组按自定义比较器排序 |
    | `parallelSort(arr)` | **并行排序**（Fork/Join，大数组更快） |
    ### 查找
    | **方法** | **说明** | **示例** |
    | --- | --- | --- |
    | `binarySearch(arr, key)` | **二分查找**，返回下标 | — |
    | `binarySearch(arr, from, to, key)` | 指定范围内查找 | — |
    | `binarySearch(objArr, key, comparator)` | 按自定义比较器查找 |  |
    PS：
    1. **数组必须先排好序**，否则结果是垃圾值
    1. **找不到时不返回 -1**，而是返回 `(插入点) - 1`
    1. 找到多个相同值时，返回哪个下标不确定
    ### 填充
    | **方法** | **说明** | **示例** |
    | --- | --- | --- |
    | `fill(arr, val)` | 全部元素填充为 val | `Arrays.fill(a, 0)` |
    | `fill(arr, from, to, val)` | 填充 `[from, to)` 范围 |  |
    ### 拷贝
    | **方法** | **说明** | **备注** |
    | --- | --- | --- |
    | `copyOf(arr, newLen)` | 拷贝到指定长度 | 变长补默认值，变短截断 |
    | `copyOfRange(arr, from, to)` | 拷贝 `[from, to)` 范围 | 相当于字符串的 `substring` |
    | `System.arraycopy(src, srcPos, dest, destPos, len)` | 底层 native 拷贝 |  |
    ### 比较
    | **方法** | **说明** |
    | --- | --- |
    | `equals(arr1, arr2)` | 长度和每个元素都相等才返回 true |
    | `deepEquals(arr1, arr2)` | **嵌套数组**深度比较 |
    | `compare(arr1, arr2)` | 字典序比较，返回负/零/正 |
    | `mismatch(arr1, arr2)` | 返回第一个不同处的下标，全同返回 -1 |
    PS：**`==`**** 比较的是地址，****`equals`**** 才比较内容**
    ### 转list（后面介绍list）
    | **方法** | **说明** |
    | --- | --- |
    | `asList(T... a)` | 数组转 List |
    ### 其他
    | **方法** | **说明** | **版本** |
    | --- | --- | --- |
    | `hashCode(arr)` / `deepHashCode(arr)` | 计算数组哈希值 | — |
    | `stream(arr)` | 数组转 Stream，可用函数式处理 | JDK 8 |
    | `setAll(arr, generator)` | 按公式批量赋值 | JDK 8 |
    | `spliterator(arr)` | 可拆分迭代器（并行用） |  |
  日期相关工具类
    计算机中以时间戳来记录时间「自1970年1月1日00:00:00（UTC时间）起到某一时刻的毫秒数」
    时区则是从英国本初子午线开始为UTC 0+，每隔15°经度+1
    # 日期相关工具类（`Date`类）
    这里讲的是旧的日期类，现在这些方法大多数都已过时
    ### 查看当前时间
    创建一个Date类的对象即可
    ```java
Date date = new Date();
System.out.println(date);
    ```
    ### 传入一个时间戳
    将时间戳作为参数传入即可
    ```java
Date date = new Date(1000);
//变量date此时就携带了该时间戳
    ```
    或是传入年月日时分秒
    ```java
Date date = new Date(125, 7, 1, 12, 0, 0);  //直接设置年月日时分秒，其中年是相对于1900年，月份从0开始
System.out.println(date);
    ```
    或是用set方法设置时间
    ```java
Calendar instance = Calendar.getInstance();
instance.set(2025, Calendar.NOVEMBER, 1);
instance.set(2025, Calendar.NOVEMBER, 1, 20, 0, 0);  //时分秒也可以一起
    ```
    ### 其他方法
    ```java
long ts = now.getTime();      // 取毫秒时间戳（最常用）
now.setTime(ts);              // 覆盖为新的时间戳
boolean a = now.after(other);  // 时间戳now是否晚于时间戳other
boolean b = now.before(other); // 时间戳now是否早于时间戳other
boolean c = now.equals(other); // 时间戳now毫秒值是否相同与时间戳other

    ```
    # `DateFormat`类
    `DateFormat`类可以实现字符串和日期对象的相互转换。由于其定义是一个抽象类无法直接使用，其常用的子类是`SimpleDateFormat`，通过配置能实现各种各样的日期转换：
    依旧是创建对象来携带转换后的日期
    ```java
//对应的日期格式为：2025-11-11 21:12:03（区分大小写）
SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
    ```
    其中日期格式需要我们手动指定，日期格式的规则可以参考，常用格式符号：
    | 符号 | 描述 | 示例 |
    | --- | --- | --- |
    | y | 年 (年份) | `yyyy`（四位数年，如2024）
`yy`（两位数年，如24） |
    | M | 月 (月份) | `MM`（两位数月，如01）
`MMM`（简写月名，如Jan）
`MMMM`（全名，如January） |
    | d | 日 (天数) | `dd`（两位数日，如09）
`d`（无前导零） |
    | H | 24小时制小时（0-23） | `HH`（两位，如08）
`H`（无前导零） |
    | h | 12小时制小时（1-12） | `hh`（两位，如08）
`h`（无前导零） |
    | m | 分钟 | `mm`（两位，如05）
`m`（无前导零） |
    | s | 秒 | `ss`（两位，如09）
`s`（无前导零） |
    | S | 毫秒 | `SSS`（三位，如123） |
    | a | 上午/下午标志 | `AM` 或 `PM` |
    其中parse方法用于将字符串转换为时间戳对象
    format方法用于将时间戳对象转化为字符串

    ### 总的来说，旧版的日期类还是太难用了（用起来太复杂）
  新版日期类（Java8）
    Java 8 引入了一套全新的日期和时间 API，主要包括以下几个核心类，它们都位于 `java.time` 包中，旨在解决旧版 `java.util.Date` 和 `java.util.Calendar` 设计上的不足
    - **LocalDate：** 表示没有时间部分的日期（年、月、日）例如：2024-04-27
    - **LocalTime：** 表示没有日期部分的时间（时、分、秒、纳秒）例如：14:30:00
    - **LocalDateTime：** 表示日期和时间的组合（没有时区信息）例如：2024-04-27T14:30:00
    - **ZonedDateTime：** 表示带有时区的日期和时间，例如：2024-04-27T14:30:00+08:00[Asia/Shanghai]
    # LocalDate类
      只有日期、没有时间和时区
      ### 创建与解析
      | **方法** | **说明** | **示例** |
      | --- | --- | --- |
      | `now()` | 系统默认时区的当前日期 | `LocalDate.now()` |
      | `now(ZoneId)` | 指定时区的当前日期 | `LocalDate.now(ZoneId.of("Asia/Shanghai"))` |
      | `of(int y, int m, int d)` | 按年/月/日创建，月份从 1 开始 | `LocalDate.of(2025, 3, 15)` |
      | `of(int, Month, int)` | 用 `Month` 枚举，避免写错月份 | `LocalDate.of(2025, Month.MARCH, 15)` |
      | `parse(CharSequence)` | 解析 ISO 格式字符串 `yyyy-MM-dd` | `LocalDate.parse("2025-03-15")` |
      | `parse(CharSequence, DateTimeFormatter)` | 按自定义格式解析 | `LocalDate.parse("2025/03/15", fmt)` |
      | `ofYearDay(int year, int dayOfYear)` | 按年内第几天创建 | `LocalDate.ofYearDay(2025, 74)` → 3月15日 |
      | `ofEpochDay(long epochDay)` | 距 1970-01-01 的天数 | `LocalDate.ofEpochDay(0)` → 1970-01-01 |
      PS：
      1. LocalDate类不能直接new对象，而是需要调用 `now() , of() , ofYearDay() `这几个静态方法来创建对象
      1. LocalDate类创建出来的对象是不可变的，修改需要使用with方法创建副本
      ### **取值（get 系列）**
      | **方法** | **返回** | **示例结果（2025-03-15，周六）** |
      | --- | --- | --- |
      | `getYear()` | `int` | 2025 |
      | `getMonthValue()` | `int`（1–12） | 3 |
      | `getMonth()` | `Month` 枚举 | `Month.MARCH` |
      | `getDayOfMonth()` | `int`（1–31） | 15 |
      | `getDayOfWeek()` | `DayOfWeek` 枚举 | `DayOfWeek.SATURDAY` |
      | `getDayOfYear()` | `int`（1–366） | 74 |
      | `lengthOfMonth()` | `int` | 31 |
      | `lengthOfYear()` | `int` | 365 |
      | `isLeapYear()` | `boolean` | false |
      ### **加减运算（plus / minus）**
      | **方法** | **说明** |
      | --- | --- |
      | `plusDays(long)` / `minusDays(long)` | 加/减天数 |
      | `plusWeeks(long)` / `minusWeeks(long)` | 加/减周数 |
      | `plusMonths(long)` / `minusMonths(long)` | 加/减月数 |
      | `plusYears(long)` / `minusYears(long)` | 加/减年数 |
      | `plus(long, TemporalUnit)` / `minus(...)` | 按通用单位加减，如 `ChronoUnit.DECADES` |
      ### **字段调整**
      | **方法** | **说明** |
      | --- | --- |
      | `withDayOfMonth(int)` | 改为当月某天 |
      | `withDayOfYear(int)` | 改为当年第几天 |
      | `withMonth(int)` | 改月份 |
      | `withYear(int)` | 改年份 |
      | `with(TemporalAdjuster)` | 高级调整器，如"下周一" |
      ### **比较判断**
      | **方法** | **返回** | **说明** |
      | --- | --- | --- |
      | `isBefore(LocalDate)` | `boolean` | 是否早于 |
      | `isAfter(LocalDate)` | `boolean` | 是否晚于 |
      | `isEqual(LocalDate)` | `boolean` | 是否同一天 |
      | `equals(Object)` | `boolean` | 值相等（对 LocalDate 与 isEqual 等价） |
      | `compareTo(LocalDate)` | `int` | 负数早于 / 0 相等 / 正数晚于，可用于排序 |
      ### **差值计算**
      | **方法** | **返回** | **说明** |
      | --- | --- | --- |
      | `until(LocalDate)` | `Period` | 两个日期之间的"年月日"差 |
      | `until(Temporal, TemporalUnit)` | `long` | 按指定单位取差值 |
      | `toEpochDay()` | `long` | 距 1970-01-01 的天数（两值相减得天数差） |
      | `datesUntil(LocalDate)`（Java 9+） | `Stream<LocalDate>` | 遍历日期区间 |
    # LocalTime类
    `LocalTime` 与 `LocalDate` 是一对姊妹类：`LocalDate` 只管"哪一天"，`LocalTime` 只管"几点几分几秒"（如 `14:30:05.123`），同样**不可变、线程安全、无时区**
    API表和上面类似，就略了，到时候查吧
    # LocalDateTime类
    `LocalDateTime` 是前两者的合体：**日期 + 时间、无时区**（如 `2026-09-17T21:30:05.123`），是 `java.time` 中使用频率最高的类。它同样**不可变、线程安全**
    # **ZonedDateTime类**
    是最全的时间类，有时间，日期，时区，它同样**不可变、线程安全**
    # DateTimeFormatter类
    `DateTimeFormatter` 是 `java.time` 体系中负责**格式化（对象 → 字符串）和解析（字符串 → 对象）的类**
    `DateTimeFormatter` 本身不存储任何日期数据，它只是一个“翻译器”，定义了日期时间对象与字符串之间的双向映射规则：
