---
{
  "id": "3a85a2dd-8276-8012-be42-c437caf05226",
  "url": "https://app.notion.com/p/3a85a2dd82768012be42c437caf05226",
  "created_time": "2026-07-25T07:32:00.000Z",
  "last_edited_time": "2026-07-27T13:41:00.000Z"
}
---

#  第四章：流程控制

[代码块与作用域](代码块与作用域/index.md)
  除了类，方法等需要用花括号包裹内容外，也可以随意创建代码块，如
  ```java
public static void main(String[] args) {
    int a = 10;   //此时变量在最外层定义
     {
     System.out.println(a);   //处于其作用域内部的代码块可以使用
     }
    System.out.println(a);   //这里肯定也可以使用
}
  ```
  - 创建代码块不会改变执行顺序(仍然按先后顺序执行）
  - 代码块会改变其中变量的作用域（在代码块中定义的变量作用域只能在代码块中）
[选择结构 （分支语句）](选择结构-分支语句/index.md)
  # 语法
  条件成立，执行单行内容：
  ```java
if (条件判断) 判断成功执行的代码;
  ```
  条件成立，执行多行内容：
  ```java
if (条件判断) {
判断成功执行的代码;
}
  ```
  条件成立执行某语句，条件不成立执行另外一些语句：if-else语句
  ```java
if (条件判断) {
语句1;
}else{
语句2;
}
  ```
  - 如果没有else，条件不成立将直接跳过分支语句
  if-else语句支持嵌套，以实现多层选择
  ```java
if (条件1) {
语句1;
}else if(条件2){
语句2;
}else if(条件3){
语句3;
}else{
语句4;
}
  ```
  同样的，if语句也支持嵌套
  ```java
if (条件) {
  if (条件) {
  语句;
  }
}
  ```
[多分支语句](多分支语句/index.md)
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
[循环](循环/index.md)
  # for循环（前置条件循环）
  ### 语法
  ```java
for (初始化语句;循环条件;调整条件) {
循环体;
}
  ```
  - 初始化语句,循环条件,调整条件可以省略
  - 可以通过Continue来跳过本次循环，用break来结束循环（当有多层嵌套时，他们只作用于当前代码块中的循环）
  - for循环是前置条件循环
  ```java
for (int i = 0; i < 3; i++) {
        if(i == 1) continue;   
        if(i == 5) break; 
 }
  ```
  如果你非要在内层结束外层循环
  可以在循环前面打上标记↓（不推荐）
  ```java
outer: for (int i = 1; i < 4; ++i) {   //在循环语句前，添加 标签: 来进行标记
    inner: for (int j = 1; j < 4; ++j) {
        if(i == j) break outer;    //break后紧跟要结束的循环标记，当i == j时终止外层循环
        System.out.println(i+", "+j);
    }
}
  ```
  # while循环（前置条件循环）
  ### 语法
  ```java
while(循环条件) {
循环体;
}
  ```
  - whilie是前置条件循环
  - 同样可以使用continue和break
  # do-while循环（后置条件循环）
  ### 语法
  ```java
do{
循环体;
}while(循环条件);
  ```
  - 同样可以使用continue和break
  - do-while是后置条件循环
[交互式编程](交互式编程/index.md)
  Java与Python一样支持交互式编程（即可以直接在命令行中编写Java代码）
  - 交互式编程方便了开发者快速验证方案和学习（没感觉到）
  - 交互式编程需要Java9+
