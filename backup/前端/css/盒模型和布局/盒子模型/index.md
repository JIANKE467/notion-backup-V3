---
{
  "id": "3615a2dd-8276-80a9-a0b3-df97f2790786",
  "url": "https://app.notion.com/p/3615a2dd827680a9a0b3df97f2790786",
  "created_time": "2026-05-15T08:29:00.000Z",
  "last_edited_time": "2026-05-17T09:06:00.000Z"
}
---

#  盒子模型


[盒子模型的概念](盒子模型的概念/index.md)
  在盒子模型的概念中，为了方便浏览器布局，我们将每个组件都视为一个矩形盒子（无论是<p>标签还是<div>）
  ## 盒子的组成部分
  一个盒子有四个部分
  - 内容区（content）
  - 内边距（padding）
  - 边框（border）
  - 外边距（margin）
  **其中盒子大小默认是内容区大小**

  这种标准很反直觉，不如IE当年的标准：“盒子大小就是所有区域总大小”
  但IE标准寄了，所以现在很多项目会多做一步设置
  ```css
* {  
box-sizing: border-box;
}
/*将所有的盒子大小改为边框大小*/
  ```
  **注意⚠️：**
  **外边距不被算作盒子大小**
  ## 属性
  box-sizing：控制盒子大小计算方式
  ## 值
  - content-box： 只包含内容区
  - border-box：连边距边框一起计算
[内容区域](内容区域/index.md)
  ## 宽高属性
  可以通过width和height属性修改某盒子内容区域大小
  **PS：盒子大小默认是指内容区域大小，所以设置某个元素的宽高实际上是设置盒子大小**
  **例外**⚠️：
  **行内元素盒子无法设置宽高**
  （虽然行内元素也是盒子）
  **行内块/块级元素可以设置宽高**
  ## 值
  - 默认值是auto：把尺寸决定权交给 layout algorithm（布局算法）
  - fit-content：尽量包住内容，但不要超过可用空间
  - max-content：元素内容在完全不换行、不压缩的情况下，需要的最大尺寸
  - min-content：最小尺寸
  - 百分比：占外部盒子的百分比（可以超过100%）
  - 绝对大小（像素）
  - 相对大小
  ## 注意
  一般来说内容区域没有东西，盒子不会被撑开（除非手动设置盒子宽高）
[背景设置](背景设置/index.md)
  ## 属性
  background-color：背景颜色
  background-image：背景图片
  background-size：背景大小（搭配背景图片使用）
  background-repeat：是否重复显示（搭配背景大小使用）
  background-position：控制背景图片在盒子中的位置（搭配背景图片使用）
  background-attachment：背景图片是否随着页面滚动
  ## 值
  背景颜色
  - 预设值：red，blue…
  - rgb值

  背景图片
  - url(”地址”)

  背景大小
  - auto：默认，按图片固有尺寸显示，如果图片没有固有尺寸，则根据容器尺寸来显示。
  - cover ：缩放背景图，保持比例，使其完全覆盖（优先窄边缩放）
  - contain ：缩放背景图，保持比例，使其完全覆盖（优先宽边缩放，可能出现重复展示）
  - 10px 10px：像素，破坏了原有比例
  - 100% 100%：占父盒子百分比

  是否重复显示
  - no-repeat：不重复
  - repeat：重复
  - repeat x：重复x方向
  - repeat y：重复y方向

  图片位置
  | 水平关键字 (X) | 垂直关键字 (Y) | 描述 |
  | --- | --- | --- |
  | left | top | 将图片左上角对齐容器的左上角。 |
  | center | center | 将图片中心点对齐容器的中心点。 |
  | right | bottom | 将图片右下角对齐容器的右下角。 |
  例： `background-position: left center; `

  - 也可以用百分比定义图片的中心相对于盒子的中心的偏移量
  例：`background-position: 50% 50%`;
  background-attachment：
  - scroll：默认，背景跟着元素滚动

  - fixed：背景固定，不跟页面滚动

  - local：背景会跟随元素内部内容滚动
  ## 注意⚠️
  background是前5个属性的简写属性，
  background下的属性可以写到一起
  （适当部分要加`/`分割避免歧义）
  ```css
.test {
  background: red no-repeat url("https://img2.baidu.com/it/u=4082245214,2139971588&fm=253&fmt=auto&app=120&f=JPEG?w=889&h=500") 10px 20px / contain;
  }
  ```
  等于
  ```css
.test {  
background-color: red;	
background-image: url("https://img2.baidu.com/it/u=4082245214,2139971588&fm=253&fmt=auto&app=120&f=JPEG?w=889&h=500");	
background-repeat: no-repeat;	
background-position: 10px 20px;	
background-size: contain;}
  ```
[盒子边框](盒子边框/index.md)
  # 总设置
  ## 边框属性
  border-width：控制边框的宽度
  border-style：控制边框的样式
  border-color：设置边框颜色
  border-radius：设置边框圆角
  ## 值
  边框宽度
  - 像素

  边框样式
  - none - 无样式，默认值
  - solid - 实线样式，一根普通的边框线，也是用的最多的一种
  - dashed - 虚线形式dotted - 点线形式，一堆小点点围绕盒子
  - double - 双实线形式，两条实线围绕盒子（边框宽度至少需要2-3px才能正确显示）
  - ridge/groove - 相框形式，比较古老的样式，不符合现代审美

  边框颜色
  - rgb
  - 预设值

  边框圆角
  - 像素：设置的圆角半径
  - 百分比：圆角百分比，设置出来就是圆角被削了一部分（真丑）
  # 单独设置四个边
  ## 属性
  border-top：上边样式
  border-bottom：下边样式
  border-left：左边样式
  border-right：右边样式
  ## 值
  同总设置

  # 注意⚠️
  - `boder`是`border-width`，`border-style`，`border-color`（宽度，颜色，风格）的简写属性，可以在boder属性下写到一起
  - 如果同时使用了边框总设置和单边设置，此时会按照声明的顺序进行覆盖
  - `border-top`是`border-top-color`，`border-top-width`，`border-top-style`的简写（其他三个边一样是简写）
  - 对于圆角的设置可以只设置某个角圆角：`border-top-left-radius：50px`
[内边距](内边距/index.md)
  # 总设置
  ## 属性
  padding：设置边距大小

  ## 值
  边距大小
  - 像素
  - 百分比：相对父元素宽度大小（宽高都按父元素宽度计算😓）
  # 四边分别设置
  ## 属性
  `padding-top`， `padding-right`，`padding-bottom`，`padding-left`
  ## 值
  值同总设置
  ## 简写
  ```css
.test {  
padding: 10px;             /* 四边都是10px */  
padding: 10px 20px;        /* 上下10px，左右20px */  
padding: 10px 20px 30px;   /* 上10px，左右20px，下30px */  
padding: 10px 20px 30px 40px; /* 上10px，右20px，下30px，左40px */}
  ```
  # 注意⚠️
  给行内元素设置内边距，盒模型不参与垂直方向上的布局计算
  人话：给行内元素设置内边距，外部左右的元素会被挤开，但上下的元素不会被挤开，但盒子却实实在在的被撑大了（背景变大）
[外边距](外边距/index.md)
  外边距不被算作盒子大小
  ## 属性
  margin：控制外边距
  ## 值
  - `20px`：四个方向上的外边距
  - `20px 10px`：上下和左右外边距
  - `20px 15px 10px 5px` ：上下左右外边距
  - 百分比：父元素宽度（长宽都基于父元素宽度）
  - auto：水平居中块级元素（对纵向没有效果）
  ## 注意⚠️
  嵌套在内部的盒子，外边距从父元素的内容区域开始计算
  行内元素设置外边距，只有左右生效（纵向由行高和文本决定）
  ## margin折叠
  1. 块级兄弟盒子，纵向上会出现margin折叠（两个盒子的外边距不会叠加），横向不会折叠
  1. 在父子元素中，在内层盒子中使用margin-top属性时，它会直接连带父盒子一起产生边距效果（仅限margin-top会出现这种情况）
  父子盒子margin折叠解决方案：
  - 父元素有 padding-top（哪怕是 1px）
  - 父元素有 border-top（哪怕是透明边框）
  - 父元素形成新的块格式化上下文（BFC，后续会介绍，比如设置overflow属性）
  1. 空的块级元素: 如果一个块级元素没有内容、padding（内边距）、border（边框），并且 height 为 auto，那么它自己的 margin-top（上外边距） 和 margin-bottom （下外边距）会发生折叠。
  ## 提示
  margin折叠是早期css作为排版系统的特性，但现在用起来非常SB，在实际开发中应避免使用margin属性
[用户代理样式（浏览器默认样式）](用户代理样式浏览器默认样式/index.md)
  用户代理样式就是浏览器的默认样式
  我们之前学过三种样式引入方法：
  1. 内联样式
  1. 内部样式
  1. 外部样式
  现在还有一种样式
  1. 用户代理样式

  这种样式的优先级最低，它的作用是给没有写css的页面一个兜底样式（由浏览器提供）
  不过有的浏览器有这东西，有的没有
  **所以建议使用外部样式确保多端统一**
[滚动区域](滚动区域/index.md)
  而当内容超出容器但我们又希望保持布局整洁、不让内容溢出到外面时，就需要使用 滚动区域
  ## 属性
  overflow：滚动条属性
  overflow-x：单独设置x滚动条
  overflow-y：单独设置y滚动条
  ## 值
  - auto：自动，超出后出现滚动条
  - scroll：滚动条常驻
  - hidden：隐藏超出部分（可被js强制滚动）（创建了滚动容器）
  - clip：裁切超出部分（无法被js强制滚动）（没创建滚动容器）
  ## PS
  滚动条不占内容区/内边距/边框区域，它是独立的一层，滚动条被包裹在边框内，拖动滚动条padding（内边距）和内容区一起滚动
  同样的<html>标签也有overflow属性，可以控制窗口的滚动
[UI设计1，2](ui设计12/index.md)
  ## 卡片背景和边框
  - 卡片背景与网页背景要有区别
  - 卡片背景与卡片文字要有对比度
  - 可以使用盒子阴影增加质感
  ## 卡片边距
  - 卡片不能没有内边距，否则非常拥挤
  - 边距推荐是4的倍数
  ## 卡片圆角
  - 卡片要加一定圆角，否则太生硬
  - 圆角越大，内边距就得越大
  ## 页面颜色
  页面颜色要贴近主题
  - 蓝色：科技、可信赖、冷静
  - 红色：警告、禁止、热情
  - 绿色：安全、通过、自然、清新
  - 黄色：提醒、高能注意
  颜色建议
  - 主色（Primary） —— 品牌、主按钮、重点视觉
  - 辅色（Secondary）—— 辅助内容、背景分区，一般不会和主色调差别过大
  - 强调色（Accent） —— 强调、提醒、交互反馈，建议采用主色调的反色或相差较大的颜色
  注意
  时刻注意对比度，别太大（难看），别太小（看不清）
