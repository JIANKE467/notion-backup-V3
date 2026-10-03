---
{
  "id": "3655a2dd-8276-80cd-a845-e619cd24372d",
  "url": "https://app.notion.com/p/3655a2dd827680cda845e619cd24372d",
  "created_time": "2026-05-19T09:37:00.000Z",
  "last_edited_time": "2026-05-23T09:11:00.000Z"
}
---

#  网格布局

## 属性
display：用于控制盒子的展示效果（块级？行内？网格？）
## 值
- grid：网格
- inline：行内
- block：块级
[基础设置](基础设置/index.md)
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
[显式网格和隐式网格](显式网格和隐式网格/index.md)
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
[元素的定位与合并](元素的定位与合并/index.md)
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
[网格对齐](网格对齐/index.md)
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
[网格区域](网格区域/index.md)
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
