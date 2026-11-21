---
{
  "id": "3695a2dd-8276-80dd-8177-e2baa500bcc5",
  "url": "https://app.notion.com/p/3695a2dd827680dd8177e2baa500bcc5",
  "created_time": "2026-05-23T09:10:00.000Z",
  "last_edited_time": "2026-05-23T09:12:00.000Z"
}
---

#  布局

[定位布局](定位布局/index.md)
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
[网格布局](网格布局/index.md)
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
[弹性布局](弹性布局/index.md)
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
[布局行内展示](布局行内展示/index.md)
  我们已经知道，通过设置 display: flex，一个容器就变成了“Flex容器”，它的直接子元素就成了“Flex项目”。不过，这种容器依然是一个块级元素（block-level element）
  CSS支持将这些常用的布局设置为行内形式，让其变为行内特性
  将flex属性和替换成inline-flex属性或inline-grid属性即可
[块级格式化上下文BFC](块级格式化上下文bfc/index.md)
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
[UI设计：顶部导航栏](ui设计顶部导航栏/index.md)
  使用定位布局-固定定位，固定导航栏
  将离左右边框距离设为0即可占满顶部

  写内容部分时注意调整上内边距，不要被导航栏遮住了

  至于图标，网上有很多图标库可用
  icinfont.com
  https://fontawesome.com/
  https://iconpark.oceanengine.com/official
