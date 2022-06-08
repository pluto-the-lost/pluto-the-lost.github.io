---
title: 使用markdown
date: 2022-06-03 18:18:00 +0800
categories: blogs
tags: [markdown, vs-code]
---

Markdown是用文档形式编写简易html网页的语言，可以节省一些排版操作。

<!-- more -->

基本语法就不再提了，网上都能搜到，看[官方教程](https://markdown.com.cn/basic-syntax/)就好，非常简单。

## 在vscode中使用markdown

我在vscode写markdown最多的是两个情景，一是github repo的readme.md文件，二是写博客。推荐安装vscode的几个插件：

* [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one) 提供了markdown的快捷键，以及公式编辑等功能
* [Markdown Preview Enhanced](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced) 提供了markdown的即时预览工具，并且可以切换多种主题，包括github主题，可以随时导出pdf, html等格式的文件

安装后打开.md文件，按`ctrl+k v`就可以在侧边打开预览了

## 折叠部分内容

```markdown
<details>
  <summary>Click to view hide content!</summary>

this is something hidden in the void.

</details>
```

<details>
  <summary>Click to view hide content!</summary>

this is something hidden in the void.

</details>

## 全角符号分隔符

vs-code分词是用`editor.wordSeparators`作为分隔符，里面只包括了英文半角符号，这导致在写中文markdown的时候，`ctrl+shift+方向键`，会一下子选中一大片，加入中文全角符号可以显著改善这一现象。

在vscode中，按`ctrl+shift+P`，输入Preference: Settings(UI)，找到`editor.wordSeparators`，在后面加上

    ，。？：“”、《》（）

就可以了