---
{
  "id": "3fc5a2dd-8276-8035-8d8b-c10848c7f192",
  "url": "https://app.notion.com/p/3fc5a2dd827680358d8bc10848c7f192",
  "created_time": "2026-10-17T07:00:00.000Z",
  "last_edited_time": "2026-10-17T07:19:00.000Z"
}
---

#  打印流

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
