---
{
  "id": "3a85a2dd-8276-8003-99a7-e25b23c4bbd9",
  "url": "https://app.notion.com/p/3a85a2dd8276800399a7e25b23c4bbd9",
  "created_time": "2026-07-25T08:37:00.000Z",
  "last_edited_time": "2026-07-27T13:40:00.000Z"
}
---

#  循环

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
