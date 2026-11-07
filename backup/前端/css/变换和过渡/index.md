---
{
  "id": "36e5a2dd-8276-80c2-abb9-f6cfd7f667ff",
  "url": "https://app.notion.com/p/36e5a2dd827680c2abb9f6cfd7f667ff",
  "created_time": "2026-05-28T02:43:00.000Z",
  "last_edited_time": "2026-05-28T02:49:00.000Z"
}
---

#  变换和过渡


[盒子模型进阶](盒子模型进阶/index.md)

  最大宽度和最小宽度
    css除了绝对宽高width和height外，还有最大和最小宽高
    这在响应式布局中很有用，可以防止元素变得过窄或过宽
    ## 属性
    - `max-width`: 设置元素的最大宽度
    - `min-width`: 设置元素的最小宽度
    - `max-height`: 设置元素的最大高度。
    - `min-height`: 设置元素的最小高度。
    ## 值
    - 像素
    - 百分比（占父元素的百分比）
  盒子轮廓
    轮廓（outline）是绘制在元素`border`（边框）之外的一条线，用于突出元素。它与边框非常相似，但有几个关键区别：
    1. **不占据空间**：轮廓在元素之上绘制的，不影响元素尺寸或布局，它不是盒子模型的一部分
    1. **在盒子的边框外进行绘制**：轮廓在盒子的边框外进行绘制，可能造成遮挡
    ## 属性
    outline：控制盒子的轮廓（简写属性）
    outline-style: 轮廓样式
    outline-width: 轮廓宽度
    outline-color：轮廓颜色
    outline-offset：轮廓到边框的距离
    ## 值
    outline-style:
    - [none](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Reference/Properties/outline-style#none)无轮廓 
    - [dotted](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Reference/Properties/outline-style#dotted)轮廓为一系列点
    更多略
    轮廓宽度/轮廓到边框的距离：
    - 像素
    轮廓颜色：
    - rgb值
    - 16进制
    ## PS
    轮廓不是边框
  盒子阴影
    ## 属性
    `text-shadow`属性，实现文字的阴影效果（和盒子阴影用法一致，不再赘述）
    `box-shadow` ：控制盒子阴影（简写属性）
    **~offset-x** - 水平方向的偏移，默认情况下阴影在盒子的正下方。
    **~offset-y** - 垂直方向的偏移，默认情况下阴影在盒子的正下方。
    **~(可选) blur-radius** - 模糊半径，默认阴影是纯色的，该属性改成了渐变
    **~(可选) spread-radius** - 扩展半径，默认阴影和盒子一样大，该属性可以缩放阴影大小
    **~color** - 阴影的颜色。
    注意⚠️：~代表前面是`box-shadow`
    ## 值
    **~offset-x/~offset-y：**
    - 像素
    **~color：**
    - rgb
    - 16进制
    **~(可选) blur-radius：**
    - 像素

    还有`box-shadow`属性的直属值`inset`表示这是内阴影

    ## 还能同时编写多个阴影
    ```css
 box-shadow:   /* 多个阴影可以逐行编写，但是注意需要用逗号分割 */
      0 -4px 3px rgba(0, 42, 255, 0.12),
      0 4px 8px rgba(255, 0, 0, 0.2);
    ```
    ## PS
    - 阴影也是在盒子上层绘制的，不影响布局，但可能会被父盒子截断
    - 阴影和轮廓一样，形状随盒子形状变化
    - 由于 DPI / 缩放不同，1px不一定是屏幕上 1 个像素
  行内纵向对齐
    ## 属性
    vertical-align：控制行内元素的纵向对齐方式
    ## 值
    - baseline：与文字基线对齐
    - top ：与文字顶线对齐
    - bottom ：与文字底线对齐
    - middle ：与文字中线对齐
    ![](assets/3725a2dd-8276-80de-9caf-ce6a455b088e.png)
    ## PS
    一般是给行内块设置vertical-align属性，让他和文字对齐
  精灵图
    精灵图（也称“雪碧图”）是一种网页图片应用处理方式。它将一个页面涉及到的所有零星图片都包含到一张大图中，然后利用 CSS 的 `background-image`、`background-position` 和 `width`、`height` 属性来显示大图中的特定部分。
    > 优点：通过将多个图片合并成一张，减少了HTTP请求的数量，从而加快了页面加载速度。
    ```css
.vip-icon {
  display: inline-block;
  width: 40px;
  height: 40px;
  background-position: -57px 0;
  background-image: url("/img/sprites.png");
}
    ```
    属性都是学过的，详见 [背景设置](https://app.notion.com/p/3625a2dd82768087a010eb4a876d0c08)
  颜色渐变
    # 属性
    background-image：设置背景渐变
    # 值
    ### 线性渐变函数：
    颜色沿着一条直线过渡
    **语法**
    `linear-gradient(方向，颜色1 百分比, 颜色2 百分比，...)`
    **最少参数写法：**
    `linear-gradient(颜色1 , 颜色2 )`
    例：
    ```css
.container {
  width: 300px;
  height: 50px;
  background-image: linear-gradient(to right, red, yellow);
}
    ```
    **方向参数：**
    | to bottom | 上 → 下（默认） |
    | --- | --- |
    | to top | 下 → 上 |
    | to right | 左 → 右 |
    | to left | 右 → 左 |
    | to right bottom | 左上 → 右下 |
    **还可以使用图片渐变：**
    ```css
background:
  linear-gradient(rgba(0,0,0,.4), rgba(0,0,0,.4)),
  url(bg.jpg);
    ```

    - 径向渐变 函数：颜色从一个中心点向外辐射过渡
