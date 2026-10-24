---
{
  "id": "3de5a2dd-8276-8082-a1fe-ec9c01554acb",
  "url": "https://app.notion.com/p/3de5a2dd82768082a1feec9c01554acb",
  "created_time": "2026-09-17T12:19:00.000Z",
  "last_edited_time": "2026-09-17T12:59:00.000Z"
}
---

#  日期相关工具类

计算机中以时间戳来记录时间「自1970年1月1日00:00:00（UTC时间）起到某一时刻的毫秒数」
时区则是从英国本初子午线开始为UTC 0+，每隔15°经度+1
# 日期相关工具类（`Date`类）
这里讲的是旧的日期类，现在这些方法大多数都已过时
### 查看当前时间
创建一个Date类的对象即可
```java
Date date = new Date();
System.out.println(date);
```
### 传入一个时间戳
将时间戳作为参数传入即可
```java
Date date = new Date(1000);
//变量date此时就携带了该时间戳
```
或是传入年月日时分秒
```java
Date date = new Date(125, 7, 1, 12, 0, 0);  //直接设置年月日时分秒，其中年是相对于1900年，月份从0开始
System.out.println(date);
```
或是用set方法设置时间
```java
Calendar instance = Calendar.getInstance();
instance.set(2025, Calendar.NOVEMBER, 1);
instance.set(2025, Calendar.NOVEMBER, 1, 20, 0, 0);  //时分秒也可以一起
```
### 其他方法
```java
long ts = now.getTime();      // 取毫秒时间戳（最常用）
now.setTime(ts);              // 覆盖为新的时间戳
boolean a = now.after(other);  // 时间戳now是否晚于时间戳other
boolean b = now.before(other); // 时间戳now是否早于时间戳other
boolean c = now.equals(other); // 时间戳now毫秒值是否相同与时间戳other

```
# `DateFormat`类
`DateFormat`类可以实现字符串和日期对象的相互转换。由于其定义是一个抽象类无法直接使用，其常用的子类是`SimpleDateFormat`，通过配置能实现各种各样的日期转换：
依旧是创建对象来携带转换后的日期
```java
//对应的日期格式为：2025-11-11 21:12:03（区分大小写）
SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
```
其中日期格式需要我们手动指定，日期格式的规则可以参考，常用格式符号：
| 符号 | 描述 | 示例 |
| --- | --- | --- |
| y | 年 (年份) | `yyyy`（四位数年，如2024）
`yy`（两位数年，如24） |
| M | 月 (月份) | `MM`（两位数月，如01）
`MMM`（简写月名，如Jan）
`MMMM`（全名，如January） |
| d | 日 (天数) | `dd`（两位数日，如09）
`d`（无前导零） |
| H | 24小时制小时（0-23） | `HH`（两位，如08）
`H`（无前导零） |
| h | 12小时制小时（1-12） | `hh`（两位，如08）
`h`（无前导零） |
| m | 分钟 | `mm`（两位，如05）
`m`（无前导零） |
| s | 秒 | `ss`（两位，如09）
`s`（无前导零） |
| S | 毫秒 | `SSS`（三位，如123） |
| a | 上午/下午标志 | `AM` 或 `PM` |
其中parse方法用于将字符串转换为时间戳对象
format方法用于将时间戳对象转化为字符串

### 总的来说，旧版的日期类还是太难用了（用起来太复杂）
