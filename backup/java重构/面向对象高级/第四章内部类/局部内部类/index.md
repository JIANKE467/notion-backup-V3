---
{
  "id": "3db5a2dd-8276-8055-acbc-ef2d769e3915",
  "url": "https://app.notion.com/p/3db5a2dd82768055acbcef2d769e3915",
  "created_time": "2026-09-14T08:49:00.000Z",
  "last_edited_time": "2026-09-20T09:29:00.000Z"
}
---

#  局部内部类

局部内部类是**在方法中定义的类**
```java
public class Outer {
    public void hello(){
        class Inner {    //直接在方法中创建局部内部类
            
        }
    }
}
```
### 注意⚠️
- 局部内部类的作用域为该方法
