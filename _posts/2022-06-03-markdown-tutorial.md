---
title: 使用markdown
date: 2022-06-03 18:18:00 +0800
categories: blogs
tags: [markdown]
---

Markdown是用文档形式编写简易html网页的语言，可以节省一些排版操作。

<!-- more -->

基本语法就不再提了，网上都能搜到，看[官方教程](https://markdown.com.cn/basic-syntax/)就好

## 在vscode中使用markdown

我在vscode写markdown最多的是两个情景，一是github repo的readme.md文件，二是写博客。推荐安装vscode的几个插件，

* [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one) 提供了markdown的快捷键
* [Markdown Preview Enhanced](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced) 提供了markdown的即时预览工具，并且可以切换多种主题，包括github主题，可以随时导出pdf, html等格式的文件

安装后打开.md文件，按`ctrl+k v`就可以在侧边打开预览了

## 插入视频

[插入bilibili视频教程](https://www.cnblogs.com/wkfvawl/p/12268980.html)

先获取视频的cid和aid，在下面的代码中修改这两项，再把修改后的html代码加到md文件中想要视频出现的地方即可

```html
<div style="position: relative; padding: 30% 45%;">
<iframe style="position: absolute; width: 100%; height: 100%; left: 0; top: 0;" src="https://player.bilibili.com/player.html?cid=145147963&aid=84267566&page=1&as_wide=1&high_quality=1&danmaku=1" frameborder="no" scrolling="no"></iframe>
</div>
```

<!-- <div style="position: relative; padding: 30% 45%;">
<iframe style="position: absolute; width: 100%; height: 100%; left: 0; top: 0;" src="https://player.bilibili.com/player.html?cid=145147963&aid=84267566&page=1&as_wide=1&high_quality=1&danmaku=1" frameborder="no" scrolling="no"></iframe>
</div> -->

插入youtube视频

直接在youtube页面点击分享 -> 嵌入，复制那段`<iframe`开头的html代码，放到md文件里就行