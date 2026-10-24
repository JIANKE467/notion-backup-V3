---
{
  "id": "3fb5a2dd-8276-8095-8d0d-cb6ccf4c3c13",
  "url": "https://app.notion.com/p/3fb5a2dd827680958d0dcb6ccf4c3c13",
  "created_time": "2026-10-16T06:20:00.000Z",
  "last_edited_time": "2026-10-17T07:17:00.000Z"
}
---

#  文件字符流

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
