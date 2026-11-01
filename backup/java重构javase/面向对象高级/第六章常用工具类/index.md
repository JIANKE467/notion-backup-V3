---
{
  "id": "3de5a2dd-8276-805f-8339-d7e4eff90df7",
  "url": "https://app.notion.com/p/3de5a2dd8276805f8339d7e4eff90df7",
  "created_time": "2026-09-17T11:25:00.000Z",
  "last_edited_time": "2026-09-17T12:58:00.000Z"
}
---

#  第六章：常用工具类


[数学工具类](数学工具类/index.md)
  Java语法自带的加减乘除无法满足复杂运算的需求，因此，Java还提供了一些数学工具类供人使用
  # 数学工具类（Math类）
  Math类可以直接调用，不用写包名（Match类属于java.lang包，而编译器会自动【import】引入java.lang包）
  ### 基础数学运算
  | **方法** | **签名** | **说明** | **示例** |
  | --- | --- | --- | --- |
  | 绝对值 | `abs(int/long/float/double a)` | 返回绝对值 | `Math.abs(-5)` → `5` |
  | 最大值 | `max(a, b)` | 返回两数中较大值 | `Math.max(3, 7)` → `7` |
  | 最小值 | `min(a, b)` | 返回两数中较小值 | `Math.min(3, 7)` → `3` |
  | 四舍五入 | `round(double/float a)` | 四舍五入返回 long/int | `Math.round(2.6)` → `3` |
  | 向上取整 | `ceil(double a)` | 向上取整，返回 double | `Math.ceil(2.1)` → `3.0` |
  | 向下取整 | `floor(double a)` | 向下取整，返回 double | `Math.floor(2.9)` → `2.0` |
  | 截断取整 | `rint(double a)` | 取最接近的整数，返回 double | `Math.rint(2.5)` → `2.0` |
  | 符号复制 | `signum(a)` | 返回参数的符号（1.0 / -1.0 / 0） | `Math.signum(-8)` → `-1.0` |
  | 交换/相邻浮点数 | `nextUp(a)` / `nextDown(a)` | 返回相邻的浮点值 | 精度调试用 |
  ### 幂与开方
  | **方法** | **签名** | **说明** | **示例** |
  | --- | --- | --- | --- |
  | 求平方根 | `sqrt(double a)` | 平方根 | `Math.sqrt(16)` → `4.0` |
  | 求立方根 | `cbrt(double a)` | 立方根 | `Math.cbrt(27)` → `3.0` |
  | 求幂 | `pow(double a, double b)` | a 的 b 次方 | `Math.pow(2, 10)` → `1024.0` |
  | 欧几里得范数 | `hypot(x, y)` | √(x²+y²)，不会溢出 | `Math.hypot(3, 4)` → `5.0` |
  | 平方根倒数 | `sqrt(x² + y²)` 类的还有 | — | — |
  ### 指数与对数
  | **方法** | **签名** | **说明** | **示例** |
  | --- | --- | --- | --- |
  | e 的幂 | `exp(double a)` | e^a | `Math.exp(1)` → `2.718...` |
  | e 的幂减 1 | `expm1(double a)` | e^a − 1（小数精度更好） | — |
  | 自然对数 | `log(double a)` | 以 e 为底 | `Math.log(Math.E)` → `1.0` |
  | 以 10 为底对数 | `log10(double a)` | — | `Math.log10(100)` → `2.0` |
  | log(1+x) | `log1p(double x)` | ln(1+x)（小数精度更好） | — |
  ### 三角函数
  | **方法** | **说明** | **备注** |
  | --- | --- | --- |
  | `sin(a)` / `cos(a)` / `tan(a)` | 正弦、余弦、正切 | **参数是弧度**，不是角度 |
  | `asin(a)` / `acos(a)` / `atan(a)` | 反三角函数 | 返回弧度 |
  | `atan2(y, x)` | 返回点 的极角 | 常用于计算角度，避免除零问题 |
  | `toRadians(deg)` | 角度 → 弧度 | `Math.toRadians(180)` → `π` |
  | `toDegrees(rad)` | 弧度 → 角度 | `Math.toDegrees(Math.PI)` → `180.0` |
  | `sinh(x)` / `cosh(x)` / `tanh(x)` | 双曲正弦/余弦/正切 | — |
  ### 随机数
  | **方法** | **说明** | **示例** |
  | --- | --- | --- |
  | `random()` | 返回 `[0.0, 1.0)` 的随机 double | — |
  ### 常数
  | **常量** | **说明** | **值** |
  | --- | --- | --- |
  | `Math.PI` | 圆周率 π | 3.141592653589793 |
  | `Math.E` | 自然常数 e | 2.718281828459045 |
  ### 精度控制
  | **方法** | **说明** | **示例** |
  | --- | --- | --- |
  | `floorDiv(x, y)` | 向下取整的整数除法 | `Math.floorDiv(-7, 2)` → `-4`（`-7/2` 是 `-3`） |
  | `floorMod(x, y)` | 向下取整的取模（结果符号同 y） | `Math.floorMod(-7, 2)` → `1`（`-7%2` 是 `-1`） |
  | `IEEEremainder(x, y)` | IEEE 754 标准的余数 | — |
  | `copySign(magnitude, sign)` | 取第一个数的绝对值 + 第二个数的符号 | `Math.copySign(3, -1)` → `-3.0` |
  | `fma(a, b, c)` | a×b+c（一次舍入，更快更准） | JDK 9+ |
[数组工具类](数组工具类/index.md)
  在Java中操作数组还得遍历，非常麻烦，因此Java提供了数组工具类用来便捷操作数组
  # 数组工具类（Arrays类）
  Arrays类可以直接调用，不用写包名（Arrays类属于java.util包，而编译器会自动`import java.util.*`）
  ### 打印/转字符串
  | **方法** | **说明** | **示例** |
  | --- | --- | --- |
  | `toString(arr)` | 一维数组转字符串，格式 `[1, 2, 3]` | `Arrays.toString(new int[]{1,2})` → `[1, 2]` |
  | `deepToString(arr)` | **嵌套数组**转字符串，递归处理 |  |
  PS：查看数组要么遍历，要么`toString(arr)` 不能直接println，否则会显示哈希地址
  ### 排序
  | **方法** | **说明** |
  | --- | --- |
  | `sort(arr)` | 升序排序（基本类型用**双轴快排**，对象用 **TimSort**）**oracle.com** |
  | `sort(arr, from, to)` | 只排序 `[from, to)` 范围 |
  | `sort(objArr, comparator)` | 对象数组按自定义比较器排序 |
  | `parallelSort(arr)` | **并行排序**（Fork/Join，大数组更快） |
  ### 查找
  | **方法** | **说明** | **示例** |
  | --- | --- | --- |
  | `binarySearch(arr, key)` | **二分查找**，返回下标 | — |
  | `binarySearch(arr, from, to, key)` | 指定范围内查找 | — |
  | `binarySearch(objArr, key, comparator)` | 按自定义比较器查找 |  |
  PS：
  1. **数组必须先排好序**，否则结果是垃圾值
  1. **找不到时不返回 -1**，而是返回 `(插入点) - 1`
  1. 找到多个相同值时，返回哪个下标不确定
  ### 填充
  | **方法** | **说明** | **示例** |
  | --- | --- | --- |
  | `fill(arr, val)` | 全部元素填充为 val | `Arrays.fill(a, 0)` |
  | `fill(arr, from, to, val)` | 填充 `[from, to)` 范围 |  |
  ### 拷贝
  | **方法** | **说明** | **备注** |
  | --- | --- | --- |
  | `copyOf(arr, newLen)` | 拷贝到指定长度 | 变长补默认值，变短截断 |
  | `copyOfRange(arr, from, to)` | 拷贝 `[from, to)` 范围 | 相当于字符串的 `substring` |
  | `System.arraycopy(src, srcPos, dest, destPos, len)` | 底层 native 拷贝 |  |
  ### 比较
  | **方法** | **说明** |
  | --- | --- |
  | `equals(arr1, arr2)` | 长度和每个元素都相等才返回 true |
  | `deepEquals(arr1, arr2)` | **嵌套数组**深度比较 |
  | `compare(arr1, arr2)` | 字典序比较，返回负/零/正 |
  | `mismatch(arr1, arr2)` | 返回第一个不同处的下标，全同返回 -1 |
  PS：**`==`**** 比较的是地址，****`equals`**** 才比较内容**
  ### 转list（后面介绍list）
  | **方法** | **说明** |
  | --- | --- |
  | `asList(T... a)` | 数组转 List |
  ### 其他
  | **方法** | **说明** | **版本** |
  | --- | --- | --- |
  | `hashCode(arr)` / `deepHashCode(arr)` | 计算数组哈希值 | — |
  | `stream(arr)` | 数组转 Stream，可用函数式处理 | JDK 8 |
  | `setAll(arr, generator)` | 按公式批量赋值 | JDK 8 |
  | `spliterator(arr)` | 可拆分迭代器（并行用） |  |
[日期相关工具类](日期相关工具类/index.md)
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
[新版日期类（Java8）](新版日期类java8/index.md)
  Java 8 引入了一套全新的日期和时间 API，主要包括以下几个核心类，它们都位于 `java.time` 包中，旨在解决旧版 `java.util.Date` 和 `java.util.Calendar` 设计上的不足
  - **LocalDate：** 表示没有时间部分的日期（年、月、日）例如：2024-04-27
  - **LocalTime：** 表示没有日期部分的时间（时、分、秒、纳秒）例如：14:30:00
  - **LocalDateTime：** 表示日期和时间的组合（没有时区信息）例如：2024-04-27T14:30:00
  - **ZonedDateTime：** 表示带有时区的日期和时间，例如：2024-04-27T14:30:00+08:00[Asia/Shanghai]
  # LocalDate类
    只有日期、没有时间和时区
    ### 创建与解析
    | **方法** | **说明** | **示例** |
    | --- | --- | --- |
    | `now()` | 系统默认时区的当前日期 | `LocalDate.now()` |
    | `now(ZoneId)` | 指定时区的当前日期 | `LocalDate.now(ZoneId.of("Asia/Shanghai"))` |
    | `of(int y, int m, int d)` | 按年/月/日创建，月份从 1 开始 | `LocalDate.of(2025, 3, 15)` |
    | `of(int, Month, int)` | 用 `Month` 枚举，避免写错月份 | `LocalDate.of(2025, Month.MARCH, 15)` |
    | `parse(CharSequence)` | 解析 ISO 格式字符串 `yyyy-MM-dd` | `LocalDate.parse("2025-03-15")` |
    | `parse(CharSequence, DateTimeFormatter)` | 按自定义格式解析 | `LocalDate.parse("2025/03/15", fmt)` |
    | `ofYearDay(int year, int dayOfYear)` | 按年内第几天创建 | `LocalDate.ofYearDay(2025, 74)` → 3月15日 |
    | `ofEpochDay(long epochDay)` | 距 1970-01-01 的天数 | `LocalDate.ofEpochDay(0)` → 1970-01-01 |
    PS：
    1. LocalDate类不能直接new对象，而是需要调用 `now() , of() , ofYearDay() `这几个静态方法来创建对象
    1. LocalDate类创建出来的对象是不可变的，修改需要使用with方法创建副本
    ### **取值（get 系列）**
    | **方法** | **返回** | **示例结果（2025-03-15，周六）** |
    | --- | --- | --- |
    | `getYear()` | `int` | 2025 |
    | `getMonthValue()` | `int`（1–12） | 3 |
    | `getMonth()` | `Month` 枚举 | `Month.MARCH` |
    | `getDayOfMonth()` | `int`（1–31） | 15 |
    | `getDayOfWeek()` | `DayOfWeek` 枚举 | `DayOfWeek.SATURDAY` |
    | `getDayOfYear()` | `int`（1–366） | 74 |
    | `lengthOfMonth()` | `int` | 31 |
    | `lengthOfYear()` | `int` | 365 |
    | `isLeapYear()` | `boolean` | false |
    ### **加减运算（plus / minus）**
    | **方法** | **说明** |
    | --- | --- |
    | `plusDays(long)` / `minusDays(long)` | 加/减天数 |
    | `plusWeeks(long)` / `minusWeeks(long)` | 加/减周数 |
    | `plusMonths(long)` / `minusMonths(long)` | 加/减月数 |
    | `plusYears(long)` / `minusYears(long)` | 加/减年数 |
    | `plus(long, TemporalUnit)` / `minus(...)` | 按通用单位加减，如 `ChronoUnit.DECADES` |
    ### **字段调整**
    | **方法** | **说明** |
    | --- | --- |
    | `withDayOfMonth(int)` | 改为当月某天 |
    | `withDayOfYear(int)` | 改为当年第几天 |
    | `withMonth(int)` | 改月份 |
    | `withYear(int)` | 改年份 |
    | `with(TemporalAdjuster)` | 高级调整器，如"下周一" |
    ### **比较判断**
    | **方法** | **返回** | **说明** |
    | --- | --- | --- |
    | `isBefore(LocalDate)` | `boolean` | 是否早于 |
    | `isAfter(LocalDate)` | `boolean` | 是否晚于 |
    | `isEqual(LocalDate)` | `boolean` | 是否同一天 |
    | `equals(Object)` | `boolean` | 值相等（对 LocalDate 与 isEqual 等价） |
    | `compareTo(LocalDate)` | `int` | 负数早于 / 0 相等 / 正数晚于，可用于排序 |
    ### **差值计算**
    | **方法** | **返回** | **说明** |
    | --- | --- | --- |
    | `until(LocalDate)` | `Period` | 两个日期之间的"年月日"差 |
    | `until(Temporal, TemporalUnit)` | `long` | 按指定单位取差值 |
    | `toEpochDay()` | `long` | 距 1970-01-01 的天数（两值相减得天数差） |
    | `datesUntil(LocalDate)`（Java 9+） | `Stream<LocalDate>` | 遍历日期区间 |
  # LocalTime类
  `LocalTime` 与 `LocalDate` 是一对姊妹类：`LocalDate` 只管"哪一天"，`LocalTime` 只管"几点几分几秒"（如 `14:30:05.123`），同样**不可变、线程安全、无时区**
  API表和上面类似，就略了，到时候查吧
  # LocalDateTime类
  `LocalDateTime` 是前两者的合体：**日期 + 时间、无时区**（如 `2026-09-17T21:30:05.123`），是 `java.time` 中使用频率最高的类。它同样**不可变、线程安全**
  # **ZonedDateTime类**
  是最全的时间类，有时间，日期，时区，它同样**不可变、线程安全**
  # DateTimeFormatter类
  `DateTimeFormatter` 是 `java.time` 体系中负责**格式化（对象 → 字符串）和解析（字符串 → 对象）的类**
  `DateTimeFormatter` 本身不存储任何日期数据，它只是一个“翻译器”，定义了日期时间对象与字符串之间的双向映射规则：
