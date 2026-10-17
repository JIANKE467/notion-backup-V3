---
{
  "id": "3f95a2dd-8276-80c8-a4a6-cc3cafc21cd8",
  "url": "https://app.notion.com/p/Java-IO-3f95a2dd827680c8a4a6cc3cafc21cd8",
  "created_time": "2026-10-14T08:09:00.000Z",
  "last_edited_time": "2026-10-17T07:00:00.000Z"
}
---

#  Java IO

本章节讲Java I/O框架，我们知道，读写硬盘等IO操作需要使用系统调用，而不同操作系统的调用方式不同，而Java则通过Java IO框架屏蔽了这种差异，实现了：一套代码到处运行
**JavaIO框架核心是通过流来操作IO数据的**
注意⚠️：前面学的Stream流不隶属于`java.io`包，且特性/方法也是不一样的
[文件字节流](文件字节流/index.md)
  本节的核心是FileInputStream类及**FileOutputStream类**，下面围绕该类进行展开
  # FileInputStream类（文件字节输入流）
  来历：FileInputStream是`InputStream` 的具体实现类，位于 `java.io` 包中
  作用：用于获取文件的字节流（把硬盘上的一个文件，以**字节**为单位读取到程序内存中）（输入文件到流）
  ### 常用方法
  构造方法（创建FileInputStream类的对象时支持的传入参数）：
  ```java
FileInputStream(File file)          
// 通过 File 对象创建
FileInputStream(String name)        
// 通过文件路径名创建
FileInputStream(FileDescriptor fdObj) 
// 通过文件描述符创建
  ```
  读取方法：
  | 方法 | 功能 | 传入 | 返回 |
  | --- | --- | --- | --- |
  | **read()** | 一次读取一个字节，下次调用读取下一个，读到末尾返回-1 | 空参调用 | 读到的那个字节值，读到末尾返回-1 |
  | **read(byte[] b)** | 一次读多个字节，将读到的值放入传入的数组中，每次读都从数组的0下标覆盖写入 | 传入一个数组 | 读到的字节数，读到的值放到了数组中，读到末尾返回-1 |
  | **int read(byte[] b, int off, int len)** | 依旧将数据存到数组中，不过可以控制存放位置、读取量 | 数组（存放读到的数据），起始下标，读取字节 | 读到的字节数，读到的值放到了数组中，读到末尾返回-1 |
  | 方法 | 功能 | 传入 | 返回 |
  | --- | --- | --- | --- |
  | **skip(n)** | 跳过并丢弃 n 个字节的数据 | 跳过字节数 | 字节流 |
  | **available()** | 返回剩余可读取（不受阻塞）的字节估计数 | 空 | 字节数 |
  | **Descriptor getFD()** | 获取文件描述符对象。 | 空 | 对象 |
  | 方法 | 功能 | 传入 | 返回 |
  | --- | --- | --- | --- |
  | **close()** | 关闭流并释放系统资源（**使用完必须调用）** | 空 | 无 |
  ### 使用方法
  需要导入`java.io`包
  1. 创建FileInputStream类的对象以创建流
  ```java
FileInputStream fis = new FileInputStream("路径");
//将文件路径作为参数传入以明确要读取哪个文件
  ```
  1. 调用read() 方法读取流（以**int read(byte[] b, int off, int len)**签名的方法为例）
  ```java
byte[] buffer = new byte[1024];
int len = fis.read(buffer, 0, 512); // 最多读512字节存入buffer
  ```
  1. 关闭流并释放系统资源
  ```java
fis.close();
  ```
  ### 注意
  IO操作可能受很多因素影响导致抛异常（文件被占用，硬盘正忙），因此需要捕获异常（使用try catch捕获异常）
  可以空处理/打印堆栈/稍后重试
  ```java
public static void main(String[] args) {
    try {   
		    //注意，IO相关操作会有很多影响因素，有可能出现异常，所以需要明确进行处理
        FileInputStream inputStream = new FileInputStream("路径");
        //路径支持相对路径和绝对路径
    } catch (FileNotFoundException e) {
		    //打印异常堆栈
        e.printStackTrace();
    }
}
  ```
  # **FileOutputStream类（文件字节输出流）**
  来历：FileOutputStream是`OutputStream`的具体实现类，位于`java.io`包中
  作用：用于将程序中的字节写入文件（把内存中的数据，以**字节**为单位写入硬盘上的文件）（从流中输出）
  ### 常用方法
  构造方法（创建FileOutputStream类的对象时支持的传入参数）：
  ```java
FileOutputStream(File file)
// 通过 File 对象创建，默认覆盖文件原有内容
FileOutputStream(String name)
// 通过文件路径名创建，默认覆盖文件原有内容
FileOutputStream(File file, boolean append)
// 通过 File 对象创建，可指定是否追加写入
FileOutputStream(String name, boolean append)
// 通过文件路径名创建，可指定是否追加写入
FileOutputStream(FileDescriptor fdObj)
// 通过文件描述符创建
  ```
  写入方法：（跟字节输入流差不多）
  | 方法 | 功能 | 传入 | 返回 |
  | --- | --- | --- | --- |
  | **write(int b)** | 写入一个字节（一次只写入参数的前 8 位，超出部分会被忽略） | 字符/数字/十六进制 | 无 |
  | **write(byte[] b)** | 将数组中的所有字节写入文件 | 一个字节数组 | 无 |
  | **write(byte[] b, int off, int len)** | 将数组中从 `off` 开始的 `len` 个字节写入文件 | 字节数组、起始下标、写入字节数 | 无 |
  | **flush()** | 刷新输出流，使待写数据提交到底层输出目标 | 空 | 无 |
  | **close()** | 关闭流并释放系统资源（使用完必须调用） | 空 | 无 |
  ### 使用方法
  需要导入`java.io`包
  1. 创建FileOutputStream类的对象以创建流
  ```java
FileOutputStream fos = new FileOutputStream("路径");
// 将文件路径作为参数传入，以明确要写入哪个文件
  ```
  1. 调用write()方法写入字节（以`write(byte[] b)`为例）
  ```java
byte[] data = {65, 66, 67};
fos.write(data); // 将数组中的字节写入文件
  ```
  1. 关闭流并释放系统资源
  ```java
fos.close();
  ```
  ### 注意
  IO操作可能受很多因素影响导致抛异常（路径不存在、文件无法创建、磁盘正忙等），因此需要捕获异常（使用try catch捕获异常）
  异常可以空处理/打印堆栈/稍后重试；
  默认创建FileOutputStream时，如果目标文件已经存在，会先清空原有内容再写入；如果需要保留原内容并在末尾追加，应使用带`append`参数的构造方法，并将其设为`true`
  FileOutputStream写入的是字节，不是字符；写入文本时需要先按指定字符集将字符串转换为字节
  ```java
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.charset.StandardCharsets;

public static void main(String[] args) {
    try (FileOutputStream outputStream = new FileOutputStream("路径")) {
        // 路径支持相对路径和绝对路径
        byte[] data = "示例文本".getBytes(StandardCharsets.UTF_8);
        outputStream.write(data);
    } catch (IOException e) {
        // 打印异常堆栈
        e.printStackTrace();
    }
}
  ```
[文件字符流](文件字符流/index.md)
  这个跟上一节差不多
  文件字符流主要由两个类构成：**FileReader（文件字符输入流）**、**FileWriter（文件字符输出流）**。下面围绕这两个类展开。
  # FileReader 类（文件字符输入流）
  继承关系：继承自 `InputStreamReader`，位于 `java.io` 包中；它会把文件中的字节按指定字符集解码为字符。
  作用：获取文件的字符流（把硬盘上的文件，以字符为单位读取到程序内存中）。适合读取文本文件；读取图片、音频等二进制文件应使用字节流（输入文件到流）
  ### 常用方法
  构造方法（创建 `FileReader` 对象时支持的传入参数）：
  ```java
FileReader(File file)
// 通过 File 对象创建，使用平台默认字符集
FileReader(String fileName)
// 通过文件路径名创建，使用平台默认字符集
FileReader(FileDescriptor fd)
// 通过文件描述符创建
FileReader(File file, Charset charset)
// 通过 File 对象创建，并指定字符集（Java 11+）
FileReader(String fileName, Charset charset)
// 通过文件路径名创建，并指定字符集（Java 11+）
  ```
  读取方法：
  | 方法 | 功能 | 传入 | 返回 |
  | --- | --- | --- | --- |
  | **read()** | 一次读取一个字符；读到末尾返回 `-1` | 空参调用 | 读到的字符值（`int`），末尾返回 `-1` |
  | **read(char[] cbuf)** | 将字符读入字符数组，从数组下标 `0` 开始覆盖写入 | 字符数组 | 实际读取的字符数，末尾返回 `-1` |
  | **read(char[] cbuf, int off, int len)** | 将字符读入数组，可指定存放位置和最多读取的字符数 | 字符数组、起始下标、最多读取长度 | 实际读取的字符数，末尾返回 `-1` |
  其他常用方法：
  | 方法 | 功能 | 传入 | 返回 |
  | --- | --- | --- | --- |
  | **skip(long n)** | 跳过并丢弃 `n` 个字符 | 要跳过的字符数 | 实际跳过的字符数 |
  | **ready()** | 判断下一次读取是否可以保证不阻塞 | 空 | `true` 或 `false` |
  | **getEncoding()** | 获取当前使用的字符编码名称 | 空 | 编码名称；若流已关闭则可能为 `null` |
  | **close()** | 关闭流并释放系统资源（使用完必须调用） | 空 | 无 |
  ### 使用方法
  需要导入 `java.io` 包。读取文本时，建议明确指定字符集，避免文件编码与平台默认字符集不一致而出现乱码。
  1. 创建 `FileReader` 对象以创建流
  ```java
FileReader reader = new FileReader("路径", StandardCharsets.UTF_8);
// 将文件路径和字符集作为参数传入
  ```
  1. 调用 `read()` 方法读取字符（以字符数组批量读取为例）
  ```java
char[] buffer = new char[1024];
int len = reader.read(buffer, 0, buffer.length); // 最多读取 1024 个字符
  ```
  1. 关闭流并释放系统资源
  ```java
reader.close();
  ```
  ### 注意
  IO 操作可能受文件不存在、文件被占用、磁盘异常等因素影响而抛出异常，因此需要处理 `IOException`。推荐使用 `try-with-resources`，让流在代码块结束时自动关闭。
  ```java
import java.io.FileReader;
import java.io.IOException;
import java.nio.charset.StandardCharsets;

public static void main(String[] args) {
    try (FileReader reader = new FileReader("路径", StandardCharsets.UTF_8)) {
        char[] buffer = new char[1024];
        int len;
        while ((len = reader.read(buffer)) != -1) {
            System.out.print(new String(buffer, 0, len));
        }
    } catch (IOException e) {
        e.printStackTrace();
    }
}
  ```
  `read()` 的返回类型是 `int`，这样可以用 `-1` 表示文件末尾；读到字符时返回其字符值。Java 的 `char` 表示 UTF-16 代码单元，因此一个补充字符可能由两个 `char` 组成。
  # FileWriter 类（文件字符输出流）
  继承关系：继承自 `OutputStreamWriter`，位于 `java.io` 包中；它会把程序中的字符按指定字符集编码为字节，再写入文件。
  作用：用于将程序中的字符写入文本文件（把内存中的字符数据写入硬盘上的文件）（从流中输出文件）
  ### 常用方法
  构造方法（创建 `FileWriter` 对象时支持的传入参数）：
  ```java
FileWriter(File file)
// 通过 File 对象创建，使用平台默认字符集；默认覆盖原内容
FileWriter(String fileName)
// 通过文件路径名创建，使用平台默认字符集；默认覆盖原内容
FileWriter(File file, boolean append)
// 通过 File 对象创建，可指定是否追加；使用平台默认字符集
FileWriter(String fileName, boolean append)
// 通过文件路径名创建，可指定是否追加；使用平台默认字符集
FileWriter(FileDescriptor fd)
// 通过文件描述符创建
FileWriter(File file, Charset charset)
// 指定字符集（Java 11+）
FileWriter(File file, Charset charset, boolean append)
// 指定字符集和是否追加（Java 11+）
FileWriter(String fileName, Charset charset)
// 指定字符集（Java 11+）
FileWriter(String fileName, Charset charset, boolean append)
// 指定字符集和是否追加（Java 11+）
  ```
  写入方法：
  | 方法 | 功能 | 传入 | 返回 |
  | --- | --- | --- | --- |
  | **write(int c)** | 写入一个字符 | 字符值（`int`） | 无 |
  | **write(char[] cbuf)** | 将字符数组中的全部字符写入文件 | 字符数组 | 无 |
  | **write(char[] cbuf, int off, int len)** | 将数组中从 `off` 开始的 `len` 个字符写入文件 | 字符数组、起始下标、字符数 | 无 |
  | **write(String str)** | 将字符串写入文件 | 字符串 | 无 |
  | **write(String str, int off, int len)** | 将字符串中指定范围的字符写入文件 | 字符串、起始下标、字符数 | 无 |
  | **flush()** | 刷新输出流，使缓冲中的数据提交到底层输出目标 | 空 | 无 |
  | **close()** | 关闭流并释放系统资源（使用完必须调用） | 空 | 无 |
  ### 使用方法
  需要导入 `java.io` 包。指定字符集时，需使用 Java 11+ 提供的 `Charset` 构造方法。
  1. 创建 `FileWriter` 对象以创建流
  ```java
FileWriter writer = new FileWriter("路径", StandardCharsets.UTF_8);
// 默认覆盖目标文件原有内容
  ```
  1. 调用 `write()` 方法写入字符
  ```java
writer.write("示例文本");
writer.write("追加到程序缓冲区的字符");
  ```
  1. 刷新并关闭流
  ```java
writer.flush();
writer.close();
  ```
  ### 注意
  IO 操作可能因为路径不存在、文件无法创建、磁盘异常等原因抛出 `IOException`，需要进行异常处理。推荐使用 `try-with-resources`：
  ```java
import java.io.FileWriter;
import java.io.IOException;
import java.nio.charset.StandardCharsets;

public static void main(String[] args) {
    try (FileWriter writer = new FileWriter("路径", StandardCharsets.UTF_8)) {
        writer.write("示例文本");
    } catch (IOException e) {
        e.printStackTrace();
    }
}
  ```
  `FileWriter` 默认使用平台默认字符集；为保证不同环境下文本编码一致，建议显式指定字符集，例如 `StandardCharsets.UTF_8`。Java 18 及之后版本的默认字符集通常为 UTF-8，但显式指定仍更清晰、可靠。
  默认创建 `FileWriter` 时，如果目标文件已存在，会先清空原有内容再写入；若要保留原内容并在末尾追加，应使用带 `append` 参数的构造方法，并将其设为 `true`：
  ```java
try (FileWriter writer = new FileWriter("路径", StandardCharsets.UTF_8, true)) {
    writer.write("追加内容");
}
  ```
  `FileWriter` 写入的是字符，字符会根据所选字符集编码后保存为文件字节；读取时应使用相同字符集，避免乱码。
[(Java 7/8/11) 文件工具类](java-7811-文件工具类/index.md)
  Java原生的文件工具类有File，Files，RandomAccessFile
  这里我们只介绍Files类
  # Files类
  归属：依旧是在`java.io`包下
  作用：操作文件的工具类（创建/删除/移动/重命名…）
  注意⚠️：Files类下的所有方法均为静态方法，无需创建对象即可使用（典型的工具类） 
  ### 常用方法
  - 判断方法
  | **方法** | **功能** | **传入参数** | **返回值** |
  | --- | --- | --- | --- |
  | `exists(Path)` | 判断文件或目录是否存在 | `Path`：文件路径 | `boolean`：布尔值 |
  | `notExists(Path)` | 判断文件或目录是否不存在 | `Path`：文件路径 | `boolean`：布尔值 |
  | `isDirectory(Path)` | 判断路径是否为目录 | `Path`：路径 | `boolean`：布尔值 |
  | `isRegularFile(Path)` | 判断路径是否为普通文件 | `Path`：路径 | `boolean`：布尔值 |
  | `isReadable(Path)` | 判断文件是否可读 | `Path`：路径 | `boolean`：布尔值 |
  | `isWritable(Path)` | 判断文件是否可写 | `Path`：路径 | `boolean`：布尔值 |
  | `isExecutable(Path)` | 判断文件是否可执行 | `Path`：路径 | `boolean`：布尔值 |
  | `isHidden(Path)` | 判断文件是否为隐藏文件 | `Path`：路径 | `boolean`：布尔值 |
  | `isSymbolicLink(Path)` | 判断路径是否为符号链接 | `Path`：路径 | `boolean`：布尔值 |
  | `isSameFile(Path, Path)` | 判断两个路径是否指向同一文件 | 两个 `Path` | `boolean`：布尔值 |
  - 创建方法
  | **方法** | **功能** | **传入参数** | **返回值** |
  | --- | --- | --- | --- |
  | `createFile(Path)` | 创建一个新的空文件（父目录必须已存在） | `Path`：新文件路径 | `Path`：创建的文件路径 |
  | `createDirectory(Path)` | 创建单级目录（父目录必须已存在） | `Path`：目录路径 | `Path`：创建的目录路径 |
  | `createDirectories(Path)` | 递归创建多级目录（父目录不存在时自动创建） | `Path`：目录路径 | `Path`：创建的目录路径 |
  | `createTempFile(String, String)` | 在系统临时目录创建临时文件 | 前缀（文件名）、后缀（扩展名） | `Path`：临时文件路径 |
  | `createTempFile(Path, String, String)` | 在指定目录创建临时文件 | 目录、前缀（文件名）、后缀（扩展名） | `Path`：临时文件路径 |
  | `createTempDirectory(String)` | 在系统临时目录创建临时目录 | 文件夹名 | `Path`：临时目录路径 |
  注意⚠️：系统临时目录关机即删
  Windows临时目录路径：C:\Users\用户名\AppData\Local\Temp
  Linux临时目录路径：/tmp
  - 删除方法
  | **方法** | **功能** | **传入参数** | **返回值** |
  | --- | --- | --- | --- |
  | `delete(Path)` | 删除文件或空目录（不存在时抛异常） | `Path`：待删除路径 | `void`（无返回值） |
  | `deleteIfExists(Path)` | 删除文件或空目录（不存在时静默跳过，不抛异常） | `Path`：待删除路径 | `boolean`：布尔值 |
  - 复制/移动方法
  | **方法** | **功能** | **传入参数** | **返回值** |
  | --- | --- | --- | --- |
  | `copy(Path, Path, CopyOption...)` | 复制文件或目录到目标位置 | 源路径、目标路径、选项（如 `REPLACE_EXISTING` 覆盖） | `Path`：目标路径 |
  | `copy(InputStream, Path, CopyOption...)` | 把输入流的内容写入文件（常用于下载保存） | 输入流对象、目标路径、选项 | `long`：复制的字节数 |
  | `copy(Path, OutputStream)` | 把文件内容读出写入输出流 | 源路径、输出流 | `long`：复制的字节数 |
  | `move(Path, Path, CopyOption...)` | 移动文件或重命名 | 源路径、目标路径、选项（如 `ATOMIC_MOVE` 原子移动） | `Path`：目标路径 |
  - 读取方法
  | **方法** | **功能** | **传入参数** | **返回值** |
  | --- | --- | --- | --- |
  | `readAllBytes(Path)` | 一次性读取整个文件的所有字节（仅适合小文件） | `Path`：文件路径 | `byte[]`：全部字节内容 |
  | `readAllLines(Path)` | 一次性读取整个文件的所有行（仅适合小文件） | `Path`：文件路径（默认 UTF-8） | `List<String>`：所有行的列表 |
  | `readAllLines(Path, Charset)` | 一次性读取所有行，并指定编码 | 路径、字符集 | `List<String>`：所有行的列表 |
  | `readString(Path)`（JDK 11+） | 一次性读取整个文本文件为字符串（仅适合小文件） | `Path`：文件路径 | `String`：整个文件内容 |
  | `lines(Path)` | 惰性逐行读取文件（按需加载，适合大文件） | `Path`：文件路径 | `Stream<String>`：行内容流 |
  | `newBufferedReader(Path)` | 打开带缓冲的字符读取流（适合逐行处理大文件） | `Path`：文件路径 | `BufferedReader`：缓冲读取流 |
  | `newInputStream(Path, OpenOption...)` | 打开文件字节输入流 | 路径、打开选项 | `InputStream`：字节输入流 |
  - 写入类
  | **方法** | **功能** | **传入参数** | **返回值** |
  | --- | --- | --- | --- |
  | `write(Path, byte[], OpenOption...)` | 把字节数组写入文件（默认覆盖，可加 `APPEND` 追加） | 路径、字节数组、选项 | `Path`：写入的文件路径 |
  | `write(Path, Iterable<CharSequence>, Charset, OpenOption...)` | 按行把字符串集合写入文件 | 路径、行集合、字符集、选项 | `Path`：写入的文件路径 |
  | `writeString(Path, CharSequence, OpenOption...)`（JDK 11+） | 把字符串写入文件 | 路径、字符串、选项 | `Path`：写入的文件路径 |
  | `newBufferedWriter(Path, OpenOption...)` | 打开带缓冲的字符写入流（适合逐行写出） | 路径、打开选项（如 `APPEND`） | `BufferedWriter`：缓冲写入流 |
  | `newOutputStream(Path, OpenOption...)` | 打开文件字节输出流 | 路径、打开选项 | `OutputStream`：字节输出流 |
  - 遍历方法
  | **方法** | **功能** | **传入参数** | **返回值** |
  | --- | --- | --- | --- |
  | `list(Path)` | 列出目录下的**直接子项**（不递归） | `Path`：目录路径 | `Stream<Path>`：子项流 |
  | `walk(Path)` | 递归遍历整个目录树的所有层级 | `Path`：起始目录 | `Stream<Path>`：所有条目流 |
  | `walk(Path, int)` | 递归遍历目录树，但限制最大深度 | 路径、最大深度 | `Stream<Path>`：限定深度的条目流 |
  | `find(Path, int, BiPredicate)` | 递归查找目录树中满足条件的条目 | 路径、深度、过滤条件（路径+属性 → boolean） | `Stream<Path>`：符合条件的条目流 |
  | `newDirectoryStream(Path)` | 打开目录流，可迭代遍历目录内容 | `Path`：目录路径 | `DirectoryStream<Path>`：可迭代的目录流 |
  - 获取属性方法
  | **方法** | **功能** | **传入参数** | **返回值** |
  | --- | --- | --- | --- |
  | `size(Path)` | 获取文件大小 | `Path`：文件路径 | `long`：文件大小（字节） |
  | `getLastModifiedTime(Path)` | 获取文件最后修改时间 | `Path`：文件路径 | `FileTime`：修改时间对象 |
  | `setLastModifiedTime(Path, FileTime)` | 设置文件最后修改时间 | 路径、时间对象 | `Path`：文件路径 |
  | `getOwner(Path)` | 获取文件所有者 | `Path`：文件路径 | `UserPrincipal`：所有者对象 |
  | `readAttributes(Path, Class<T>)` | 一次性读取文件的完整属性（大小、时间、类型等） | 路径、属性类型（如 `BasicFileAttributes.class`） | `T`：属性对象 |
  | `setAttribute(Path, String, Object)` | 设置文件的某个属性（如只读、权限） | 路径、属性名、属性值 | `Path`：文件路径 |
  # Q&A
  Q：前面的章节“文件字节/字符流”不是已经实现了输入/输出的方法了吗？为什么这里又实现一遍？
  A：这里并不是重复实现，这里的输入/输出方法本质还是调用的文件字节/字符流的方法，这里只是为了整合更完善的功能（支持直接编辑而不是先创建流）而做的包装
[缓冲流](缓冲流/index.md)
  经过前面章节的学习，我们知道文件字节/字符流可以对文件进行读取或写入操作，但不论是文件字符流还是文件字节流，它们都是从直接从硬盘中读取（忽略系统优化）
  缓冲流则是一个~~预读取~~（实际上不是预读取，）操作，它可以提前将文件读取到内存中，这样等获取数据时就无需再从硬盘中读取了
  依旧分为字节缓冲流和字符缓冲流
  # 字节缓冲流
    来源：都在`java.io`包中，且字节缓冲流类都继承自相应的文件字节流类
    ### **BufferedInputStream（缓冲字节输入流）**
    作用：以字节为单位读取文件到内存中
    **构造方法：**
    | 构造方法签名 | 作用 | 传入 |
    | --- | --- | --- |
    | BufferedInputStream(InputStream in) | 创建字节缓冲流对象（默认大小） | 文件字节流对象 |
    | BufferedInputStream(InputStream in, int size)  | 创建字节缓冲流对象（自定义大小） | 文件字节流对象，缓存区大小（单位：字节） |
    ```java
BufferedInputStream(InputStream in)              
// 单参数，默认缓冲区大小 8192 字节，传入文件字节流对象
BufferedInputStream(InputStream in, int size)    
// 2参数，自定义缓冲区大小，传入文件字节流和缓存区大小
    ```
    **常用方法：**
    - 由于字节缓冲流类都继承自相应的文件字节流类，所以继承了文件字节流有的所有方法
    **使用方法：**
    1. 调用构造方法创建缓冲流
    1. 执行文件字节流操作或调用文件工具类
    1. 关闭缓冲流
    ### **BufferedOutputStream（缓冲字节输出流）**
    来历：位于 `java.io` 包中，接收一个 `OutputStream` 作为底层输出流，常用于包装文件字节输出流。
    作用：先将程序中的字节写入内存缓冲区，缓冲区满或调用刷新、关闭操作时，再批量写入底层输出流，以减少直接写入次数。
    **构造方法：**
    | 构造方法签名 | 作用 | 传入 |
    | --- | --- | --- |
    | `BufferedOutputStream(OutputStream out)` | 创建字节缓冲输出流（默认缓冲区大小） | 底层输出流 |
    | `BufferedOutputStream(OutputStream out, int size)` | 创建指定缓冲区大小的字节缓冲输出流 | 底层输出流、缓冲区大小（单位：字节） |
    ```java
BufferedOutputStream(OutputStream out)
// 使用默认大小的缓冲区
BufferedOutputStream(OutputStream out, int size)
// 自定义缓冲区大小，size 单位为字节
    ```
    **常用方法：**
    | 方法 | 功能 | 传入 | 返回 |
    | --- | --- | --- | --- |
    | `write(int b)` | 将一个字节写入缓冲区；缓冲区满时会写入底层输出流 | 一个字节值 | 无 |
    | `write(byte[] b, int off, int len)` | 将字节数组中指定范围的数据写入缓冲区 | 字节数组、起始下标、写入长度 | 无 |
    | `flush()` | 将缓冲区中尚未写出的数据刷新到底层输出流 | 空 | 无 |
    | `close()` | 刷新并关闭流，同时释放系统资源 | 空 | 无 |
    由于它继承了输出流的写入方法，也可以直接调用 `write(byte[] b)` 写入整个字节数组。
    **使用方法：**
    1. 创建底层文件字节输出流，并用缓冲流包装
    1. 调用 `write()` 写入字节
    1. 使用完关闭缓冲流（会自动刷新，并关闭底层流）
    ```java
byte[] data = {65, 66, 67};
try (BufferedOutputStream output = new BufferedOutputStream(
        new FileOutputStream("路径"))) {
    output.write(data);
    // 需要在关闭前确保数据写出时，可调用 output.flush()
} catch (IOException e) {
    e.printStackTrace();
}
    ```
  # 字符缓冲流
    ### **BufferedReader（缓冲字符输入流）**
    来历：位于 `java.io` 包中，接收一个 `Reader` 作为底层字符流，常用于包装 `FileReader`。
    作用：以字符为单位缓冲读取文本内容，并提供按行读取的功能。
    **构造方法：**
    | 构造方法签名 | 作用 | 传入 |
    | --- | --- | --- |
    | `BufferedReader(Reader in)` | 创建字符缓冲输入流（默认缓冲区大小） | 底层字符输入流 |
    | `BufferedReader(Reader in, int size)` | 创建指定缓冲区大小的字符缓冲输入流 | 底层字符输入流、缓冲区大小（单位：字符） |
    ```java
BufferedReader(Reader in)
// 使用默认大小的缓冲区
BufferedReader(Reader in, int size)
// 自定义缓冲区大小，size 表示字符数
    ```
    **常用方法：**
    | 方法 | 功能 | 传入 | 返回 |
    | --- | --- | --- | --- |
    | `read()` | 读取一个字符，读到末尾返回 `-1` | 空参调用 | 字符值（`int`），末尾返回 `-1` |
    | `read(char[] cbuf, int off, int len)` | 将字符读入数组，可指定存放位置和最多读取的字符数 | 字符数组、起始下标、最多读取长度 | 实际读取的字符数，末尾返回 `-1` |
    | `readLine()` | 读取一行文本，不包含行结束符 | 空参调用 | 行内容；读到末尾且没有更多内容时返回 `null` |
    | `ready()` | 判断下一次读取是否可以保证不阻塞 | 空 | `true` 或 `false` |
    | `close()` | 关闭流并释放系统资源 | 空 | 无 |
    **使用方法：**
    需要导入 `java.io` 包。读取文本时应注意字符集；下面示例使用 Java 11+ 的 `FileReader` 字符集构造方法。
    1. 创建 `FileReader`，并用 `BufferedReader` 包装
    1. 调用 `readLine()` 逐行读取，返回 `null` 时表示读完
    1. 使用完关闭缓冲流（底层流也会随之关闭）
    ```java
try (BufferedReader reader = new BufferedReader(
        new FileReader("路径", StandardCharsets.UTF_8))) {
    String line;
    while ((line = reader.readLine()) != null) {
        System.out.println(line);
    }
} catch (IOException e) {
    e.printStackTrace();
}
    ```
    **注意：**
    `readLine()` 会去掉行结束符；如果需要保留换行，应在处理每一行时自行添加。文件字符集应与读取时指定的字符集一致，避免乱码。
    ### **BufferedWriter（缓冲字符输出流）**
    来历：位于 `java.io` 包中，接收一个 `Writer` 作为底层字符流，常用于包装 `FileWriter`。
    作用：先将程序中的字符写入内存缓冲区，再批量写入底层字符输出流；还提供了写入平台适用换行符的方法。
    **构造方法：**
    | 构造方法签名 | 作用 | 传入 |
    | --- | --- | --- |
    | `BufferedWriter(Writer out)` | 创建字符缓冲输出流（默认缓冲区大小） | 底层字符输出流 |
    | `BufferedWriter(Writer out, int size)` | 创建指定缓冲区大小的字符缓冲输出流 | 底层字符输出流、缓冲区大小（单位：字符） |
    ```java
BufferedWriter(Writer out)
// 使用默认大小的缓冲区
BufferedWriter(Writer out, int size)
// 自定义缓冲区大小，size 表示字符数
    ```
    **常用方法：**
    | 方法 | 功能 | 传入 | 返回 |
    | --- | --- | --- | --- |
    | `write(int c)` | 写入一个字符到缓冲区 | 字符值（`int`） | 无 |
    | `write(char[] cbuf, int off, int len)` | 写入字符数组中的指定范围 | 字符数组、起始下标、字符数 | 无 |
    | `write(String str)` | 写入字符串 | 字符串 | 无 |
    | `newLine()` | 写入当前系统适用的换行符 | 空 | 无 |
    | `flush()` | 将缓冲区中的字符刷新到底层输出流 | 空 | 无 |
    | `close()` | 刷新并关闭流，同时释放系统资源 | 空 | 无 |
    **使用方法：**
    1. 创建底层字符输出流，并用缓冲流包装
    1. 调用 `write()` 写入字符或字符串；需要换行时调用 `newLine()`
    1. 使用完关闭缓冲流（会自动刷新，并关闭底层流）
    ```java
try (BufferedWriter writer = new BufferedWriter(
        new FileWriter("路径", StandardCharsets.UTF_8))) {
    writer.write("第一行");
    writer.newLine();
    writer.write("第二行");
} catch (IOException e) {
    e.printStackTrace();
}
    ```
    **注意：**
    `BufferedWriter` 的 `flush()` 可以在流关闭前提交缓冲区中的字符；关闭流时也会先刷新。若要在原文件末尾追加内容，应让底层 `FileWriter` 使用追加模式；默认构造方式会覆盖原有内容。写入文本时应明确并保持字符集一致。
  # 注意
  - 需要澄清一点事实：缓冲流仅优化了多次访问，它仍是读取到缓冲流这行才会运行的，并没有优先运行的能力
  - 字符缓冲流和普通流一样，关闭流内存就释放了（释放缓冲区），它只是提供了一个缓冲能力
[转换流](转换流/index.md)
  转换流相当于文件字节/字符流的一个工具类
  如果想将一个类型的流传入另一个类型的流，传统的做法是遍历内容后写入另一个流
  那有老铁问了：我记得前面讲过转换流类型的方法呀
  这其实是个重大误区：前面有转换流流类型方法的类叫Stream[(Java 8) Stream流](https://app.notion.com/p/3f75a2dd827680bc91aecfd079a2a38c) ，它不隶属于java.io包，而是集合框架的东西，特性和方法完全不同（虽然都是流）
  转换流就是专门用于**字节流和字符流之间相互转换**的
  **（转换流转换的不是元素类型而是流类型）**
  # InputStreamReader类（字节流➡️字符流）
  作用：将字节流转换成字符流
  构造方法：
  ```java
// 1. 使用平台默认字符集
InputStreamReader(InputStream in)

// 2. 使用指定字符集名称（最常用）
InputStreamReader(InputStream in, String charsetName)
    // charsetName 如 "UTF-8"、"GBK"，无效时抛 UnsupportedEncodingException
  ```
  工作原理：传入字节流对象，返回字符流对象，这个类光调用构造方法就够用
  # OutputStreamWriter类（字符流➡️字节流）
  作用：将字符流转换成字节流
  构造方法：
  ```java
// 1. 使用平台默认字符集
OutputStreamWriter(OutputStream out)

// 2. 使用指定字符集名称（最常用）
OutputStreamWriter(OutputStream out, String charsetName)
    // charsetName 如 "UTF-8"、"GBK"，无效时抛 UnsupportedEncodingException

  ```
  工作原理：传入字符流对象，返回字节流对象，这个类光调用构造方法就够用
[打印流](打印流/index.md)
  打印流也是文件字节/字符流的工具类
  分两种类
  # **PrintStream类（字节打印流）**
  继承关系：FilterOutputStream文件字节输出流（从流中输出）
  构造方法：
  ```java
// 接收文件路径字符串
PrintStream ps1 = new PrintStream("test.txt");

// 接收 File 对象
PrintStream ps2 = new PrintStream(new File("test.txt"));

// 接收输出流，可开启自动刷新
PrintStream ps3 = new PrintStream(
        new FileOutputStream("test.txt"), true);
  ```

  # **PrintWriter类（字符打印流）**
  继承关系：FilterWriter文件字符输出流（从流中输出）
