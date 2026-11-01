---
{
  "id": "3fc5a2dd-8276-8035-8d8b-c10848c7f192",
  "url": "https://app.notion.com/p/3fc5a2dd827680358d8bc10848c7f192",
  "created_time": "2026-10-17T07:00:00.000Z",
  "last_edited_time": "2026-10-18T08:46:00.000Z"
}
---

#  打印流

打印流也是文件字节/字符流的工具类
分两种类
# 打印流是干啥的
我们知道，可以使用文件输出字节/字符流的方法从流中输出内容到文件中，但这会带来一个问题：文件是按字符写入的，而字节输出流是按字节写入的，如果不使用转换流将字节转换成字符，就会出现字节流输出97，写进文件中变成a了（因为 97 是 a 的 ASCII 码）
因此使用普通输出流输出内容到文件就需要考虑格式转换
而打印流则提供了方便的输出方法，无需考虑格式转换，必要时会自动转换
# Q&A
Q：a存储的是97，97存储的也是97，怎么确保没有歧义的？
A：对于一般的数据结构，使用数据类型来标记到底是字符还是数字，但如果操作的是流的话，则需要手动处理一下
Q：打印流只能打印到控制台上吗？
A：并非，只是叫打印流这个名字，打印到哪里取决于构造时传入的参数（传入文件路径就打印到文件中，传入System.out就打印到控制台）
# 关于System.out
我们天天用System.out.println() 那你知道是什么意思吗？
- System是个类：**Java 给你准备的“系统级工具箱”，提供与运行环境打交道的一堆现成工具。**
- out是：一个静态变量，JVM启动时会将一个对象引用给它，这个对象就是控制台的输出流
- 所以，System.out实际是控制台输出流对象，System.out.println() 就是调用这个对象的printlnln()方法
- System.out是*PrintStream类型的对象*
# **PrintStream类（字节打印流）**
继承关系：继承自FilterOutputStream类  文件字节输出流（从流中输出）
作用：提供简便的打印方法（省去类型转换的步骤）
构造方法：（决定打印到哪里）（创建流）
```java
// 接收文件路径字符串（打印到文件）
PrintStream ps1 = new PrintStream("test.txt");

// 接收 File 对象（打印到文件）
PrintStream ps2 = new PrintStream(new File("test.txt"));

// 接收输出流，可开启自动刷新（打印到输出流/作为输出流的输入）
PrintStream ps3 = new PrintStream(
        new FileOutputStream("test.txt"), true);
```
```java
//或者直接给**PrintStream类型的变量赋值
//System.out是**控制台输出流对象
//只有System.out可以直接赋值给PrintStream，因为System.out是*PrintStream类型的对象*
PrintStream ps1 = **System.out；**
```
常用方法：
println()方法
作用：换行打印，打印位置取决于构造方法
重载：有多种重载，这确保了它什么数据类型都能打印

print()方法
作用：不换行打印，打印位置取决于构造方法
重载：有多种重载，这确保了它什么数据类型都能打印
### 使用方法
```java
public static void main(String[] args) {
		//创建对象以获取流
    try(PrintStream stream = new PrintStream("文件路径")){
        // 向文件打印lbwnb
        stream.println("lbwnb");  
    }catch (IOException e){
        
    }
}
```
# **PrintWriter类（字符打印流）**
继承关系：FilterWriter文件字符输出流（从流中输出）
和上面一模一样，不写了
