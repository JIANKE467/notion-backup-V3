---
{
  "id": "3615a2dd-8276-8041-b3d6-d847d31d843a",
  "url": "https://app.notion.com/p/3615a2dd82768041b3d6d847d31d843a",
  "created_time": "2026-05-15T07:16:00.000Z",
  "last_edited_time": "2026-05-15T08:29:00.000Z"
}
---

#  文本样式

[首行缩进](首行缩进/index.md)
  ## 属性
  text-ident：控制首行缩进
  ## 值
  可填相对大小（一个字大小）和绝对大小（像素）
[对齐方式](对齐方式/index.md)
  ## 属性
  text-align
  ## 值
  - start：如果内容方向是左至右，则等于 left，反之则为 right。
  - end：如果内容方向是左至右，则等于 right，反之则为 left。
  - left：行内内容向左侧边对齐。
  - right：行内内容向右侧边对齐。
  - center：行内内容居中。
  - justify：文字向两侧对齐，对于非等宽字体不会搞得一侧是锯齿状，对最后一行无效。
  - justify-all：和 justify 一致，但是强制使最后一行两端对齐。
  - match-parent：和 inherit 类似，区别在于 start 和 end 的值根据父元素的书写方向确定，并被替换为恰当的 left 或 right 值。
  ## PS
  **text-align属性只能添加到块级元素中，并对其中的行内元素生效**
  不能添加到行内元素中（因为行内元素占据的空间本身就是内容的宽度，没有多余的空间来让其对齐）
[文本修饰](文本修饰/index.md)
  文本修饰就是设置下划线，中划线…等
  ## 属性
  text-decoration：修饰文本
  ## 值
  可以写多个值，如：颜色，修饰类型，大小，样式…
  修饰类型：
  - none：取消原有的划线
  - underline：下划线
  - line-through：中划线
  - overline：上划线
  线条样式：
  - 实线solid
  - 波浪线wavy
  - 小点dotted
  - 双实线double
  - 虚线dashed
  颜色：
  预设值或rgb色
  宽度：
  相对宽度或绝对宽度
[文本大小写](文本大小写/index.md)
  ## 属性
  text-transform：控制文本大小写
  ## 值
  - uppercase：大写
  - lowercase：小写
  - capitalize：首字母大写
[行高](行高/index.md)
  ## 属性
  line-height：控制行高
  ## 值
  直接写倍数(默认相对大小)
  or
  相对大小
  or
  绝对大小（不建议）
[文本间距](文本间距/index.md)
  字与字之间间距
  ## 属性
  letter-spacing：控制字间距
  word-spacin：单词间距
  ## 值
  - normal：默认值（浏览器决定）
  - 绝对大小or相当大小
  ## PS
  不建议调这个属性，调不好很乱
[文本换行](文本换行/index.md)
  ## 属性
  word-break：控制文本换行策略
  overflow-wrap：控制长度超过一行的单词是否被拆分换行（该属性要与word-break属性配合使用）
  text-wrap：新版控制文本换行策略（部分浏览器未支持）
  ## 值
  word-break属性↓
  - normal – 使用默认换行规则，禁止出现单词分割。
  - break-all – 只要到达本行末尾，就强制对单词进行拆分。

  overflow-wrap属性↓
  - break-word

  text-wrap属性↓
  - wrap：自动换行
  - nowrap：禁止换行
  - balance – 平衡每行的字符数，让每一行看起来都舒适。
  - pretty – 和默认换行相同，只是用户代理将使用较慢的算法，该算法更倾向于更好的布局而不是速度。
  - stable – 和默认换行相同，只是当用户编辑内容时，他们正在编辑的行之前的行保持不变，这对于文本框来说很实用。
[文本空白处理](文本空白处理/index.md)
  本节介绍了对于代码中的空格和换行该如何处理
  默认忽略空格和换行
  ## 属性
  white-space：声明代码中的空格和换行该如何处理
  ## 值
  - pre ：保留源码空格和换行 ，其他情况一律不换行（除了<br>标签）
  - pre-wrap ： 同上，但超出宽度换行
  - pre-line ：不保留源码空格序列，只保留源码换行
  - nowrap ：完全禁止换行
