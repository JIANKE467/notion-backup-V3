---
{
  "id": "3d75a2dd-8276-80a2-913b-cd0ae906fb5e",
  "url": "https://app.notion.com/p/Java15-3d75a2dd827680a2913bcd0ae906fb5e",
  "created_time": "2026-09-10T08:32:00.000Z",
  "last_edited_time": "2026-09-10T08:41:00.000Z"
}
---

#  文本块（Java15）

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
