---
{
  "id": "3d45a2dd-8276-8051-a38c-fe4a1bb55953",
  "url": "https://app.notion.com/p/3d45a2dd82768051a38cfe4a1bb55953",
  "created_time": "2026-09-07T08:59:00.000Z",
  "last_edited_time": "2026-09-10T08:50:00.000Z"
}
---

#  第三章：字符串

字符串类型与char（字符类型）不同，
字符串类型可以保存多个字符，字符类型只能保存一个字符，
而且，
字符串是一种类，而字符类型是基本数据类型

[String类](string类/index.md)
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
[StringBuilder类](stringbuilder类/index.md)
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
[正则表达式](正则表达式/index.md)
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
[字符串类增强（Java11）](字符串类增强java11/index.md)
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
[文本块（Java15）](文本块java15/index.md)
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
[Switch模式匹配（Java21/22/25）](switch模式匹配java212225/index.md)
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
