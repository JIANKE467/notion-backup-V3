---
{
  "id": "3fb5a2dd-8276-80c3-9365-d9ac00219e5d",
  "url": "https://app.notion.com/p/Java-7-8-11-3fb5a2dd827680c39365d9ac00219e5d",
  "created_time": "2026-10-16T07:15:00.000Z",
  "last_edited_time": "2026-10-16T08:20:00.000Z"
}
---

#  **(Java 7/8/11) 文件工具类**

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
