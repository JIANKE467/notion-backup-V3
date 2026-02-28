---
{
  "id": "3005a2dd-8276-81c9-9a34-c8aafa97b6f5",
  "url": "https://www.notion.so/3005a2dd827681c99a34c8aafa97b6f5",
  "created_time": "2026-02-07T09:52:00.000Z",
  "last_edited_time": "2026-02-07T09:52:00.000Z"
}
---

#  转义字符

‍
| **转义字符** | **含义** |
| --- | --- |
| n | 换行符（Newline） |
| t | 水平制表符（Tab） |
| \ | 反斜杠 \ |
| ' | 单引号 ' |
| " | 双引号 " |
| 0 | 空字符（字符串结束标志） |
| r | 回车符（Carriage Return） |
| b | 退格符（Backspace） |
| a | 响铃符（Alert/Bell） |
| f | 换页符（Form Feed） |
| v | 垂直制表符（Vertical Tab） |
**常用说明：**
- `\n` 是最常用的转义字符，用于换行输出
- `\t` 常用于格式化输出，产生一个Tab的间距
- `\\` 用于输出反斜杠本身
- `\'` 和 `\"` 用于在字符/字符串中包含引号
- `\0` 是字符串的结束标志，C语言字符串以此结尾
**示例代码：**
```c
#include <stdio.h>

int main() {
    printf("Hello\nWorld\n");  // 换行
    printf("Name:\tSSBN\n");   // 制表符
    printf("Path: C:\\Users\\\n");  // 反斜杠
    printf("He said: \"Hello\"\n");  // 双引号
    return 0;
}
```
