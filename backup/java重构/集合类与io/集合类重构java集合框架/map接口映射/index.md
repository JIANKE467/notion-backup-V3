---
{
  "id": "3e85a2dd-8276-8023-b274-d25755c8d906",
  "url": "https://app.notion.com/p/Map-3e85a2dd82768023b274d25755c8d906",
  "created_time": "2026-09-27T09:00:00.000Z",
  "last_edited_time": "2026-09-27T09:46:00.000Z"
}
---

#  Map接口（映射）

# Map接口
作用：Map接口定义了“映射”这种逻辑，元素两两对应，也就是“键值对”
继承关系：和迭代器一样，Map不继承自集合根接口，但Map仍属于Java集合框架，下面引用Oracle官方的说法↓
> Java Collections Framework 的核心接口由两棵**并列的、相互独立的**接口树构成：**Collection 分支，Map 分支**
实现类：Map接口的实现类分为 ”一个抽象骨架”（AbstractMap） 和骨架下 “六个具体实现类”（HashMap，LinkedHashMap，Hashtable，WeakHashMap，IdentityHashMap，EnumMap），还有一堆不在抽象骨架下的类
# Map接口定义的方法
```java
//Map并不是Collection体系下的接口，而是单独的一个体系，因为操作特殊
//这里需要填写两个泛型参数，其中K就是键的类型，V就是值的类型，比如上面的学生信息，ID一般是int，那么键就是Integer类型的，而值就是学生信息，所以说值是学生对象类型的
public interface Map<K,V> {
    //-------- 查询相关操作 --------
  
  	//获取当前存储的键值对数量
    int size();

    //是否为空
    boolean isEmpty();

    //查看Map中是否包含指定的键
    boolean containsKey(Object key);

    //查看Map中是否包含指定的值
    boolean containsValue(Object value);

    //通过给定的键，返回其映射的值
    V get(Object key);

    //-------- 修改相关操作 --------

    //向Map中添加新的映射关系，也就是新的键值对
    V put(K key, V value);

    //根据给定的键，移除其映射关系，也就是移除对应的键值对
    V remove(Object key);


    //-------- 批量操作 --------

    //将另一个Map中的所有键值对添加到当前Map中
    void putAll(Map<? extends K, ? extends V> m);

    //清空整个Map
    void clear();


    //-------- 其他视图操作 --------

    //返回Map中存放的所有键，以Set形式返回
    Set<K> keySet();

    //返回Map中存放的所有值
    Collection<V> values();

    //返回所有的键值对，这里用的是内部类Entry在表示
    Set<Map.Entry<K, V>> entrySet();

    //这个是内部接口Entry，表示一个键值对
    interface Entry<K,V> {
        //获取键值对的键
        K getKey();

        //获取键值对的值
        V getValue();

        //修改键值对的值
        V setValue(V value);

        //判断两个键值对是否相等
        boolean equals(Object o);

        //返回当前键值对的哈希值
        int hashCode();

        ...
    }

    ...
}
```
非常多,没全列出来
# Map接口的实现类（以HashMap为例）
### 创建，插入，读取
```java
public static void main(String[] args) {
		
		//创建哈希映射
    Map<Integer, String> map = new HashMap<>();
    
    //使用put方法添加键值对
    map.put(1, "小明");   
    map.put(2, "小红");
    
    //使用get方法根据键获取对应的值
    System.out.println(map.get(2)); 
}
```
PS：映射（Map）无法添加相同的键，即使值不同。如果出现键相同的情况，那么会覆盖掉旧的，可以使用Java8新方法putIfAbsent()安全插入
### 默认返回值
```java
public static void main(String[] args) {
    Map<Integer, String> map = new HashMap<>();
    map.put(1, "小明");
    
    //get方法，找不到键值对默认返回null
    System.out.println(map.get(3));
    
    //getOrDefault方法，找不到键值对可以返回自定义的值
    System.out.println(map.getOrDefault(3, "备胎"));   //Java8新增操作，当不存在对应的键值对时，返回备选方案
}
```
