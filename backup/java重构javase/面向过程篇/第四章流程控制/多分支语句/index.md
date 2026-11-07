---
{
  "id": "3a85a2dd-8276-8046-91e4-da1e5c1d1de7",
  "url": "https://app.notion.com/p/3a85a2dd8276804691e4da1e5c1d1de7",
  "created_time": "2026-07-25T08:02:00.000Z",
  "last_edited_time": "2026-07-25T08:36:00.000Z"
}
---

#  多分支语句

# 语法
```java
    switch (输入选项) {  
        case '选项A':    
            语句A;
            break;   
        case '选项B':
            语句B;
            break;
        case '选项C':
            语句C;
            break;
    }
}
```
- switch语句只能处理switch语句中定义好的准确选项，无法按数值范围处理（**`switch`****可以精准匹配某个值，但是它不能进行范围判断**）
- **每个独立选项必须用break结束，否则会被视为与下个选项合并执行**
- 可以用default来表示未定义的选项如何处理
# java14（switch语法修改）
分支结果直接作为返回值：
```java
int score = 9;
//直接让grade接受switch的结果
char grade = switch (score) {
    case 10, 9 -> 'A';   //case后面直接使用->来指定返回结果
    case 8 -> 'B';
    case 6, 7 -> 'C';  //当存在多个匹配条件时，使用逗号分隔
    default -> 'D';
};  //别忘了这种写法相当于赋值，最后需要加分号
System.out.println("学生等级为: " + grade);
```
分支存在其他操作：
```java
char grade = switch (score) {
    case 9 -> 'A';
    case 8 -> 'B';
    case 6, 7 -> {
        System.out.println("我是额外操作");   //存在前置操作，无法直接指定结果
        yield 'C';   //在最后使用yield关键字来指定结果
    }
    default -> 'D';
};
```
- 新版switch语句支持分支结果直接作为返回值给到前面的变量（使用->来指定返回结果）
- 新版switch语句不需要break来结束，他是自动结束的
- 分之存在其他操作，需要手动使用yield来指定返回值
