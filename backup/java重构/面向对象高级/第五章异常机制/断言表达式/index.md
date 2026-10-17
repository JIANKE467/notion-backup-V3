---
{
  "id": "3dd5a2dd-8276-805a-8ef2-fe3378ec21b3",
  "url": "https://app.notion.com/p/3dd5a2dd8276805a8ef2fe3378ec21b3",
  "created_time": "2026-09-16T14:43:00.000Z",
  "last_edited_time": "2026-09-16T14:46:00.000Z"
}
---

#  断言表达式

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
