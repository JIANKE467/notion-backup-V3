---
{
  "id": "3af5a2dd-8276-803f-97ab-e5b379f84812",
  "url": "https://app.notion.com/p/3af5a2dd8276803f97abe5b379f84812",
  "created_time": "2026-08-01T02:06:00.000Z",
  "last_edited_time": "2026-08-01T02:28:00.000Z"
}
---

#  内存装入顺序

# 类加载时机
Java的类是懒加载策略，只有被使用到才会被加载（有如下情况）
- 使用子类时会先加载父类
- 创建该类的对象
- 访问该类的静态变量
- 调用该类静态方法
# 类加载顺序
Java以整个.class文件（类文件）为单位进行加载，大致经历以下阶段
```java
加载（Loading）:载入类基本信息
   ↓
验证（Verification）
   ↓
准备（Preparation）:static变量分配空间，赋默认值
   ↓
解析（Resolution）
   ↓
初始化（Initialization）:执行static赋值和static代码块
   ↓
使用.     :创建对象...
   ↓
卸载（Unloading）
```
