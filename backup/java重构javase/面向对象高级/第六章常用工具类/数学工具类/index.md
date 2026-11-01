---
{
  "id": "3de5a2dd-8276-805b-a58c-f6ea5c00ed87",
  "url": "https://app.notion.com/p/3de5a2dd8276805ba58cf6ea5c00ed87",
  "created_time": "2026-09-17T11:28:00.000Z",
  "last_edited_time": "2026-09-17T11:50:00.000Z"
}
---

#  数学工具类

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
