---
{
  "id": "3615a2dd-8276-80d9-86fa-eb5236fa3d21",
  "url": "https://app.notion.com/p/3615a2dd827680d986faeb5236fa3d21",
  "created_time": "2026-05-15T08:29:00.000Z",
  "last_edited_time": "2026-05-23T09:12:00.000Z"
}
---

#  盒模型和布局

[盒子模型](盒子模型/index.md)

  盒子模型的概念
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
  内容区域
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
  背景设置
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
  盒子边框
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
  内边距
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
  外边距
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
  用户代理样式（浏览器默认样式）
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
  滚动区域
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
  UI设计1，2
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
[布局](布局/index.md)
  定位布局
    浏览器默认使用的是普通文档流布局（static）
    ## 属性
    position：选择布局方式
    ## 值
    - relative（相对定位）
    - absolute（绝对定位）
    - fixed（固定定位）
    - sticky（粘滞定位）
    - static（流式定位）（默认）
    相对定位
      相对定位：相对于父盒子的内容区上下左右偏移
      ## 属性（需要先将position属性设置为相对定位）
      left：离父盒子左侧距离
      right：离父盒子右侧距离
      top：离父盒子上方距离
      bottom：离父盒子下方距离
      **子盒子定位是从父盒子边框内径，内边距外径处开始计算的**
      ## 值
      - 5px：像素
      ## 注意
      **相对定位只是视觉效果上发生了位移，盒子所占据的大小和位置还是停留在原地**
    绝对定位
      绝对定位让盒子完全脱离文档流
      **绝对定位将于最近的设置了定位布局的层中布局**
      **人话：如果父元素没有设置position属性的值，则继续往上一层，直到找到设置了position属性的层，并认该层为父层**
      **如果一直没有，那就认<html>或<body>标签为父层**
      PS：改变父层这个行为并不实际存在，只是为了解释绝对定位会以哪层为参考定位的惯性思维（专业叫法：包含块 [包含块](https://app.notion.com/p/3645a2dd82768091bb55ea4e049ed150) ）
      ## 属性（需要先将position属性设置为绝对定位）
      left：离父盒子左侧距离
right：离父盒子右侧距离
top：离父盒子上方距离
bottom：离父盒子下方距离
      **子盒子定位是从父盒子边框内径，内边距外径处开始计算的**
      ## 值
      - 5px：像素
      ## 注意
      **与相对布局不同，绝对布局不只是在视觉上移动了盒子，而是真的把盒子移动了**
      **如果absolute没有定位祖先，当body或html存在滚动条时，盒子将会跟随滚动条一起向上滚动**
      这种将盒子从页面常规排列中抽离出来，不再占据原本应有的位置，就是“脱离文档流”
    固定定位
      固定定位不受滚动条影响，始终固定在窗口某个位置（回顶部按钮的实现原理）
      ## 属性（需要先将position属性设置为固定定位）
      left：离父盒子左侧距离
      right：离父盒子右侧距离
      top：离父盒子上方距离
      bottom：离父盒子下方距离
      **子盒子定位是从父盒子边框内径，内边距外径处开始计算的**
      ## 值
      - 5px：像素
    粘滞定位
      粘滞定位可以让元素在页面滚动时，先像相对定位一样，当滚到特定位置时，就像固定定位一样
      ## 属性（需要先将position属性设置为粘滞定位）
      left：离父盒子左侧距离多远转换成固定定位
      right：离父盒子右侧距离多远转换成固定定位
      top：离父盒子上方距离多远转换成固定定位
      bottom：离父盒子下方距离多远转换成固定定位
      **子盒子定位是从父盒子边框内径，内边距外径处开始计算的**
      ## 值
      - 5px：像素
      ## 注意
      粘滞布局虽然表现得像脱离文档流，但是盒子本身所占据的区域依然存在（所以不是脱离文本流）
    包含块
      css的部分属性计算不基于父盒子，而是基于“包含块”
      ## 有哪些属性？
      - 尺寸（Size）：当元素的 width, height, padding, margin 设置为百分比（%）时，这些值是相对于包含块计算的。
      - 定位（Position）：当元素使用绝对定位（absolute）或固定定位（fixed）时，它的偏移属性（top, right, bottom, left）是相对于包含块的边缘进行
      ## 如何确定包含块？
      1. 静态与相对定位 ：父元素就是包含块
      1. 绝对定位：找最近的position 值不为 static 的祖先元素的内边距区域，如果所有祖先元素都没有设置定位，这个初始包含块通常就是浏览器窗口
      1. 固定定位 :它的包含块始终是视口
    z轴顺序
      当多个元素发生重叠时，z轴顺序决定，谁在上面，谁被挡住
      默认情况下，DOM顺序（标签顺序）靠后的会覆盖靠前的
      ## 属性
      z-index：设置z轴优先级（数大的在上面）
      ## 值
      - 只能是整数
      ## 注意⚠️
      z轴顺序不会对普通文档流元素生效，只对设置了定位方式的元素生效
    层级上下文
      ## 什么是层级上下文
      浏览器不是简单按 z-index 全局排序。
而是：
      > 每个“堆叠上下文”内部独立排序。
      可以理解成：
      - 页面被分成多个“图层世界”
      - 每个世界内部比 z-index
      - 不同世界之间整体排序
      ## 谁会创建堆叠上下文
      - 盒子存在非static定位，且使用了z-index属性（即使是z-index: 0）此时盒子会创建一个新的层级上下文盒子
      - 使用了fixed定位（即使没有z-index），会直接创建一个新的层级上下文盒子
      - 使用了sticky定位且处于粘滞状态时，会创建一个新的层级上下文
      - 盒子使用了filter、perspective、clip-path、isolation: isolate和will-change属性时。
      - 盒子使用了transform进行了三维变换（下一章介绍）
      - 盒子使用了opacity属性改变了盒子的透明度
      ## 所以
      **即便子层级的z-index超级大，但父层级的z-index较小，子元素仍会被压在下面**
  网格布局
    ## 属性
    display：用于控制盒子的展示效果（块级？行内？网格？）
    ## 值
    - grid：网格
    - inline：行内
    - block：块级
    基础设置
      网格中添加的每一个直接子元素会被自动放入到划分出来的网格中，我们一般称其为网格项
      ## 网格属性（需先将该盒子display属性设置成grid）
      grid-template-columns ：控制行属性
      grid-template-rows：控制列属性
      gap：控制网格间隙
      ## 值
      grid-template-columns/grid-template-rows属性：
      - 100px 100px 100px：表示创建3个100px的行/列
      - 1fr 1fr 1fr：表示将该容器横/纵向分3部分，每部分占比为1/3（网格占满容器）
      - repeat()函数：下面讲

      gap属性：
      - 10px：间隙大小

      ## repeat（）函数：
      语法
      ```css
repeat(行｜列数,尺寸)
      ```
      行/列数可传入参数：
      - auto-fill：自动，在不换行的情况下，尽可能多地往一行里塞入行/列
      - 数字：指定行/列数
      尺寸可传入参数：
      - 像素数（单位：px）
      - 1fr：分数比例（单位：fr）
      - minmax(200px, 1fr)：minmax()函数，定义最小尺寸和行/列数
      ## PS
      gap属性会牺牲一部分格子的大小来为格子之间留出空间，从而实现间距效果
    显式网格和隐式网格
      网格结构有两种创建策略，显示网格和隐式网格
      ## 显式网格
      显式网格就是你在容器中明确定义了几行几列，浏览器直接按你声明的行列创建
      ## 隐式网格
      没在容器中明确定义行列，或容器内元素超出原定的行列数时，浏览器的默认网格创建策略
      ## 逻辑
      当你的子元素超过了你定义的显式网格范围或没定义，CSS 会自动帮你“补网格”，这部分就是隐式网格。
      ## 属性
      - grid-auto-rows ：控制自动生成的行（隐式行）有多高
      - grid-auto-columns ：控制自动生成的列（隐式列）有多宽
      - grid-auto-flow：修改填充顺序（横向/纵向）和隐式行扩展方向（横向/纵向）
      ## 值
      grid-auto-rows ：
      - 像素
      grid-auto-columns ：
      - 像素
      grid-auto-flow：
      - row：横向排列，纵向扩展
      - column：纵向排列，横向扩展
      ## ps
      grid-auto-rows 和grid-auto-columns 属性只定义扩展行列的尺寸，不能改变原有显示网格的尺寸
    元素的定位与合并
      # 指定元素位置
      可以通过网格线（Grid Lines）的编号来指定元素的位置。
      ### 属性
      - grid-column-start:指定列开始网格线
      - grid-column-end: 指定列结束网格线
      - grid-row-start:  指定行开始网格线
      - grid-row-end: 指定行结束网格线
      或使用简写属性↓
      - grid-column: 列开始线 和 结束线
      - grid-row: 行开始线 和 结束线
      ### 值
      grid-column-start/grid-column-end/grid-row-start/grid-row-end：
      - 网格线序号（从左往右数，从1开始）
      grid-column/grid-row:
      - 序号/序号
      # 合并单元格
      Grid （网格布局）可以让一个元素跨越多个格子（合并单元格）
      **合并单元格需要在内部嵌套的盒子中设置属性↓**
      ### 属性
      grid-column：声明从哪合并到哪
      ### 值
      - `网格线序号/网格线序号`
      - `span 数字`：从当前位置跨几个格子
      ps：网格线序号可以是负数，负数是倒着数
    网格对齐
      按层级分，有三大类对齐方式
      # *-content
        *-content管网格在父元素中的对齐方式
        ### 属性
        justify-content：网格在父元素行轴（横轴）上的对齐方式
        align-content：网格在父元素块轴（纵轴）上的对齐方式
        ### 值
        - stretch (默认值): 如未设置格子具体宽度，网格将拉伸以填满空间
        - start: 行轴起点（左上角）
        - end: 行轴的终点（右上角）
        - center: 行轴中心位置
        - space-between: 拉伸格子间隙，铺满行轴
        - space-around: 保证每个格子两侧的间隔相等（左右）
        - space-evenly: 保证每个格子之间的间隔一致（上下左右）
      # *-self
        *-self管网格内子元素单个的对齐方式，需要在子元素中设置
        ### 属性
        justify-self：子元素行轴（横轴）对齐方式
        align-self：子元素块轴（纵轴）对齐方式
        ### 值
        - stretch（默认值）：如未设置格子具体宽高，子元素将拉伸填满网格区域
        - start：对齐到起点（左上角）
        - end：对齐到终点（右下角）
        - center：居中对齐
      # *-items
        *-items管网格内所有子元素整体的对齐方式，需要在父元素中设置
        ### 属性
        justify-items：所有子元素行轴（横轴）对齐方式
        align-items：所有子元素块轴（纵轴）对齐方式
        ### 值
        - stretch（默认值）：子元素拉伸填满各自的网格区域
        - start：对齐到起点
        - end：对齐到终点
        - center：居中对齐
    网格区域
      我们可以直接利用网格快捷直观的布局，而不是用传统方法填充
      ## 传统网格填充方式：
      1. 按顺序自动填充
      1. 指定单元格的起始网格线和结束网格线（合并单元格的方法）
      1. 用span指定跨几格（合并单元格的方法）
      PS：说这么多其实底层只有一种填充方法：自动填充（因为第2，3种都是基于自动填充的单元格合并）
      ## 使用grid-template-areas属性快速填充：
      ```html
<div class="grid-box">
  <div class="grid-item header">1</div>
  <div class="grid-item nav">2</div>
  <div class="grid-item content">3</div>
  <div class="grid-item footer">4</div>
</div>
      ```

      ```css
.grid-box {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: 40px 140px 40px;

  grid-template-areas:
    "header header header"   /* 从上往下从左往右，编写每个格子分别属于哪个盒子，连续的两个或多个格子会自动相连 */
    "nav    content content"
    "nav    footer footer";
}
      ```
      可以发现，该属性直接将布局较直观的表示了出来，并且省去了繁琐的合并单元格过成
      **注意⚠️**
      **grid-template-areas属性使用元素别名来布局，需要先给相应元素设置别名**
      **使用****`grid-area`****属性**
      ```css
.grid-item { background-color: gray; }
.header  { grid-area: header; }
.aside { grid-area: nav; }
.main    { grid-area: content; }
.footer  { grid-area: footer; }
      ```
      **如果某个格子想留空，可以使用点号 (.) 来表示一个空的网格单元**
  弹性布局
    Flex布局是目前Web开发中使用最广泛、最流行的布局方式，使用弹性布局，需要先将父容器的display属性的值设置为flex
    > 采用弹性布局，盒子会呈线性排列，无论是块级还是行内元素，并且即使是块级元素，也会直接无视其排斥特性。
    - 弹性布局默认会将所有元素挤到同一行（不换行）
    - 当一行元素过多，放不下时，子元素宽度会被强行压缩
    - 可以使用flex-wrap属性来控制当展示不下时是否自动换行（避免了强行压缩）
    ## 属性
    display：用于控制盒子的展示效果（块级？行内？网格？）
    flex-wrap：是否自动换行
    ## 值
    display：
    - grid：网格（块级样式）
    - inline-grid：网格（行内样式）
    - inline：行内
    - block：块级
    - flex：弹性布局（块级样式）
    - inline-flex：弹性布局（行内样式）

    flex-wrap：
    - wrap：换行
    - nowrap（默认）：不换行
    - wrap-reverse：换行，但交叉轴方向相反
    对齐方式
      Flexbox 的核心在于它引入了两个非常重要的概念：主轴（Main Axis） 和 交叉轴（Cross Axis）
      - **主轴（Main Axis）**：Flex项目排列的主要方向，默认是水平从左到右。
      - **交叉轴（Cross Axis）**：与主轴垂直的方向，如果主轴是水平的，交叉轴就是垂直的。
      ## 属性
      `flex-direction`属性：改变主轴方向
      **`justify-content`** ：控制 **主轴 (Main Axis)** 上的对齐。
      **`align-content`**：控制 **交叉轴 (Cross Axis)** 上的对齐。
      ## 值
      flex-direction：
      - `row` (默认值): 主轴为水平方向，起点在左端。
      - `row-reverse`: 主轴为水平方向，起点在右端。（项目从右向左排）
      - `column`: 主轴为垂直方向，起点在上沿。
      - `column-reverse`: 主轴为垂直方向，起点在下沿。（项目从下向上排）

      justify/align-content：
      - `flex-start/start` (默认值): 从主轴起点开始对齐。
      - `flex-end/end`: 从主轴终点开始对齐。
      - `center`: 在主轴上居中对齐。
      - `space-between`: 优先两端对齐，项目之间的间隔都相等。第一个项目贴近起点，最后一个项目贴近终点。
      - `space-around`: 每个项目两侧的间隔相等。所以，项目之间的间隔比项目与边框的间隔大一倍。
      - `space-evenly`: 所有项目之间的间隔，以及项目与边框的间隔，都完全相等。

      ## PS
      主轴上只有`justify-content`属性
      交叉轴上有`align-content`，`align-items`，`align-self`三种属性
      类似于： [网格对齐](https://app.notion.com/p/3665a2dd827680e18b32fe179afbe6d4) 
      align-content要配合换行（flex-wrap属性）使用
    空间分配
      这节介绍在页面空间改变时，盒子的缩放逻辑
      ## 属性
      flex-shrink属性：制盒子缩小倍数
      flex-grow属性：控制盒子放大倍数
      flex-basis属性：统一控制元素在主轴上占据的空间大小
      flex属性：是前面三个属性的简写
      ## 值
      flex-shrink：
      - 数字：代表盒子缩小倍数，默认1，0代表不缩小
      flex-grow：
      - 数字：代表盒子放大比例，默认0，0代表不放大
      - 如果所有盒子的 flex-grow 都为 1，它们将平分剩余空间。
      - 如果一个盒子的 flex-grow 为 2，其他盒子都为 1，那么它将获得比其他盒子多一倍的剩余空间，以此类推。
      flex-basis：
      - 默认值是 auto，表示盒子的大小由其内容或 width/height 属性决定。
      - 也可以设置一个具体的长度值，如 100px，那么盒子在主轴上的尺寸也会自动调整为100px
      flex：
      ```css
.flex-item {
  flex: 1 0 auto;
}
      ```
      等价于
      ```css
.flex-item {
  flex-grow: 1;
  flex-shrink: 0;
  flex-basis: auto;
}
      ```
  布局行内展示
    我们已经知道，通过设置 display: flex，一个容器就变成了“Flex容器”，它的直接子元素就成了“Flex项目”。不过，这种容器依然是一个块级元素（block-level element）
    CSS支持将这些常用的布局设置为行内形式，让其变为行内特性
    将flex属性和替换成inline-flex属性或inline-grid属性即可
  块级格式化上下文BFC
    ## 什么是BFC容器？
    BFC容器内部元素不会影响外部布局（如：不会margin折叠）
    BFC可以包含浮动元素
    （如：浮动元素不会导致高度塌陷）
    ## 如何开启BFC？
    - **将容器的overflow的属性为hidden（最简单）**
    还有其他开启方法↓
    - 根元素 `<html>`
    - 浮动元素 (元素的 `float` 属性不为 `none`)
    - 绝对定位元素 (元素的 `position` 值为 `absolute` 或 `fixed`)
    - `display` 值为 `inline-block`, `table-cell`, `table-caption`, `flex`, `inline-flex`, `grid` 或 `inline-grid` 的元素
    - `overflow` 值不为 `visible` 的块级元素（如 `hidden`, `auto`, `scroll`)
    ## 效果
    如：margin折叠问题
    我们只需要给两个盒子都开启BFC就不会发生margin折叠
    ## 注意⚠️
    最好是在子盒子外面套一个开启了BFC的盒子，而不是直接在子盒子打开BFC（有可能会裁切）
    overflow属性：内容超出盒子后做何处理
  UI设计：顶部导航栏
    使用定位布局-固定定位，固定导航栏
    将离左右边框距离设为0即可占满顶部

    写内容部分时注意调整上内边距，不要被导航栏遮住了

    至于图标，网上有很多图标库可用
    icinfont.com
    https://fontawesome.com/
    https://iconpark.oceanengine.com/official
[选择器进阶](选择器进阶/index.md)

  伪类选择器
    伪类选择器用于选择特定状态的元素，如：点击过的链接，鼠标悬停的元素….
    用于实现更多功能
    ## 语法
    回顾一下css语法
    ```css
选择器 {  
属性: 值;
}
    ```
    伪类选择器：以`：`开头
    ## 链接/输入框相关
    - **`:link`** 和 **`:visited`**: 分别用于设置链接未被访问和已被访问时的样式。
    - **`:hover`**: 用于设置鼠标悬停在元素上时的样式。这是最常用的伪类之一，可以用于任何元素，不仅仅是链接。
    - **`:active`**: 用于设置元素被激活时的样式（例如，鼠标在元素上按下但还未释放）。
    - **`:focus`**: 用于设置元素获得焦点时的样式，通常用于表单输入框、按钮等可交互元素。
    **注意：** 当这几个伪类一起使用时，为了保证它们都生效，需要遵循 **LVHA** 顺序：`:link` — `:visited` — `:hover` — `:active`
    例：
    ```html
<a href="#">这是一个链接</a>
    ```
    ```css
a:link {
  color: green; /* 未访问的链接为绿色 */
}
a:visited {
  color: red; /* 已访问的链接为红色 */
}
a:hover {
  color: purple; /* 鼠标悬停时变为紫色 */
  text-decoration: none;  /* 鼠标悬停时移除下划线 */
}
a:active {
  color: orange; /* 点击时变为橙色 */
}
    ```
    ## 结构类伪类
    它们会根据元素在文档树（就是HTML代码）中的位置来选取元素：
    - **`:first-child`**: 选取其父元素下的第一个子元素。
    - **`:last-child`**: 选取其父元素下的最后一个子元素。
    - **`:nth-child(n)`**: 选取其父元素下的第 `n` 个子元素。`n` 可以是：
      - 数字：如 `li:nth-child(3)` 选取第3个 `li`。
      - 关键字：`even` (偶数) 或 `odd` (奇数)。
      - 公式：`an+b` 的形式，如 `2n+1` 表示所有奇数项。
    - **`:only-child`**: 选取父元素中唯一的子元素。
    - **`:nth-of-type(n)`**: 与 `:nth-child(n)` 类似，但它只在同类型的兄弟元素中计数。例如，`p:nth-of-type(2)` 会选取父元素下的第二个 `<p>` 元素，而不管它前面有多少个其他类型的兄弟元素。
    ## 附加伪类选择器
    语法
    ```css
：附加伪类选择器（条件）
    ```
    - 使用`:not`伪类，来实现反向判断的效果
    - 使用`:where`来实现多选效果（满足）
    - `:where`表示判断只要是其中几个选择器的其中一个满足条件即可
    - `:has`伪类用于判定某个元素是否存在满足条件的子元素或是兄弟元素
    例：
    ```css
div:has(> a:first-child) {
  background-color: green;
}
    ```
  伪元素选择器
    伪元素选择器是 CSS 里用来“选中元素的一部分内容”或“在元素前后插入虚拟内容”的选择器。
    它和普通选择器最大的区别是：
    - 普通选择器：选中“整个元素”
    - 伪元素：选中“元素内部的一部分”
    - 伪元素选择器可以选择普通选择器无法选中的
    ## 语法
    常见写法使用 :: 开头，例如：
    ```css
p::first-line
/*表示选中 <p> 标签的第一行文字。*/
    ```
    # 常见伪元素
    生成型伪元素
    1. ::before
    在元素内容之前插入内容
    1. ::after
    在元素内容之后插入内容
    1. ::first-line
    选中文本第一行
    1. ::first-letter
    选中文本第一个字母
    1. ::selection
    选中文本时的样式

    非生成型伪元素
    1. ::placeholder
    选择输入框中的提示文本
    1. ::marker
    选中列表项前面的标记
    ## 属性
    content属性：配合生成型伪元素使用（否则生成型伪元素无法显示）
  嵌套选择器
    嵌套选择器就是让css支持嵌套写法（没想到吧，这东西24年前还不支持）
    直接上例子：
    ```css
.card {
  background-color: white;
}

.card p { line-height: 1.6; }
.card a { color: blue; }
    ```
    等价于
    ```css
.card {
  background-color: white;
  
  p { line-height: 1.6; }
  a { color: blue; }
}
    ```
    ## 注意⚠️
    在嵌套选择器中，使用伪选择器和类选择器仍然要声明伪选择器和类选择器的父选择器
    这时，我们可以使用`&`符号代表父选择器
    ```css
.card::before { content: "xxxx"; }
    ```
    等价于
    ```css
.card {
  ::before { content: "xxxx"; }
}
    ```
