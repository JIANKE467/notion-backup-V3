---
{
  "id": "3f75a2dd-8276-80bc-91ae-cfd079a2a38c",
  "url": "https://app.notion.com/p/Java-8-Stream-3f75a2dd827680bc91aecfd079a2a38c",
  "created_time": "2026-10-12T08:08:00.000Z",
  "last_edited_time": "2026-10-16T09:33:00.000Z"
}
---

#  **(Java 8) Stream流**

# 说在最前面
**本节围绕“流水线”这一核心思想展开**，`Stream`也是为了引入“流水线”这一概念诞生的
注意⚠️：Stream流不隶属于`java.io`包，而是在`java.utli`包下
# 流水线是什么
在Java集合框架中，想操作集合中的元素，传统的办法是：遍历所有元素后操作。如果有多步操作则需要进行多次遍历（每一步都遍历集合中所有元素）（整个集合为单位跑一遍流程）
![](assets/3f75a2dd-8276-8066-a675-ff0bc75ba735.webp)
```java
public static void main(String[] args) {
  	//定义一个集合
    List<String> list = new ArrayList<>();
    list.add("A");
    list.add("B");
    list.add("C");
  
  	//移除为B的元素（第一步）
  	Iterator<String> iterator = list.iterator();
    while (iterator.hasNext()){
        if(iterator.next().equals("B")) iterator.remove();
    }
  
  	//移除为A的元素（第二步）
   iterator = list.iterator();
    while (iterator.hasNext()){
        if(iterator.next().equals("A")) iterator.remove();
    }
    
  
	  //打印结果
	  System.out.println(list);
}
```
而流水线思想是：每个元素单独跑一遍流程（中途淘汰的元素，后面的步骤不再遍历）
```java
                 ┌──────────────────────────────────────────────┐
   Source        │   1    2    3    4    5    6    7    8       │   List<Integer>
                 └──────────────────────┬───────────────────────┘
                                        │
                                        v
                 ┌──────────────────────────────────────────────┐
  Creation       │                 .stream()                    │   Stream<Integer>
                 └─┬────┬────┬────┬────┬────┬────┬────┬────────┘
                   │1   │2   │3   │4   │5   │6   │7   │8
                   v    v    v    v    v    v    v    v
                 ┌──────────────────────────────────────────────┐
Intermediate     │        .filter(n -> n % 2 == 0)              │   Stream<Integer>
                 └─────┬─────────┬─────────┬─────────┬──────────┘
                       │2        │4        │6        │8
                       v         v         v         v
                 ┌──────────────────────────────────────────────┐
Intermediate     │        .map(n -> n * n)                      │   Stream<Integer>
                 └─────┬─────────┬─────────┬─────────┬──────────┘
                       │4        │16       │36       │64
                       v         v         v         v
                 ┌──────────────────────────────────────────────┐
Intermediate     │        .sorted()                             │   Stream<Integer>
 (stateful)      └──────────────────────┬───────────────────────┘
                                        │4    16    36    64
                                        v
                 ┌──────────────────────────────────────────────┐
Intermediate     │        .skip(1)                              │   Stream<Integer>
 (stateful)      └──────────────────────┬───────────────────────┘
                                        │16   36    64
                                        v
                 ┌──────────────────────────────────────────────┐
  Terminal       │        .forEach(System.out::println)         │   void
                 │        打印: 16  36  64                       │
                 └──────────────────────────────────────────────┘

```
```java
public static void main(String[] args) {
  	//定义一个集合
    List<String> list = new ArrayList<>();
    list.add("A");
    list.add("B");
    list.add("C");
  
  	//使用流水线处理
    list = list     
            .stream()    //获取流
            .filter(e -> !e.equals("B"))   //只允许所有不是B的元素通过流水线
	            .filter(e -> !e.equals("A")) //只允许所有不是A的元素通过流水线
            .collect(Collectors.toList());   //将流水线中的元素重新收集起来，变回List
    System.out.println(list);
}
```
# **Stream接口**
`java.util.stream.Stream` 是一个**接口**
实现类：各集合的实现类均实现了该接口
作用：为Java引入流水线能力，该接口还定义了多种集合操作方法
### 关键方法：
获取流**「写在链式调用的最前面」**
- **`stream()`****方法：获取流**
- parallelStream()方法：获取并行流「写在链式调用的最前面」
终止流**「写在链式调用的最后」（触发执行）**
- **`collect()`****方法：终止操作**
- …
中间操作
- **`filter()`**方法：过滤掉指定元素
- ** ****`map()`**方法：转换元素类型
- **`sorted()`**方法：对元素排序
- **`distinct()`**方法：去除重复元素
- ….
### 使用方法
将链式调用的结果赋值给原对象：先调用**`stream()`**方法获取流，接着调用中间操作方法操作集合，最后调用**`collect()`**方法终止流并触发执行
例子：
```java
public static void main(String[] args) {
  	//定义一个集合
    List<String> list = new ArrayList<>();
    list.add("A");
    list.add("B");
    list.add("C");
  
  	//使用流水线处理
    list = list     
            .stream()    //获取流
            .filter(e -> !e.equals("B"))   //只允许所有不是B的元素通过流水线
	          .filter(e -> !e.equals("A")) //只允许所有不是A的元素通过流水线
            .collect(Collectors.toList());   //将流水线中的元素重新收集起来，变回List
    System.out.println(list);
}
```
# 注意
- 中间操作的方法允许传入Lambda表达式
- 流水线是惰性执行，只有读到终止流的方法才会触发执行
- 使用流水线相比于普通迭代器遍历在大量数据时更加节省内存（省去了重复遍历的内存开销）
- 对于多线程的意义[https://www.icloud.com.cn/freeform/0b2aRciYqgZ7dF1xdfbels1Dg](https://www.icloud.com.cn/freeform/0b2aRciYqgZ7dF1xdfbels1Dg)
