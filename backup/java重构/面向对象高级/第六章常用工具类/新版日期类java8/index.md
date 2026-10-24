---
{
  "id": "3de5a2dd-8276-802d-bb13-ebbb099db2f2",
  "url": "https://app.notion.com/p/Java8-3de5a2dd8276802dbb13ebbb099db2f2",
  "created_time": "2026-09-17T12:58:00.000Z",
  "last_edited_time": "2026-09-17T13:26:00.000Z"
}
---

#  新版日期类（Java8）

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
