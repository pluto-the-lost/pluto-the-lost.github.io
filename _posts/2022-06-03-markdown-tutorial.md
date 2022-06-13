---
title: 使用 markdown
date: 2022-06-03 18:18:00 +0800
categories: blogs
tags: [markdown, vs-code]
---

Markdown 是用文档形式编写简易 html 网页的语言，可以节省一些排版操作。

<!-- more -->

基本语法就不再提了，网上都能搜到，看 [官方教程](https://markdown.com.cn/basic-syntax/) 就好，非常简单。

## 在 vscode 中使用 markdown

我在 vscode 写 markdown 最多的是两个情景，一是 github repo 的 readme.md 文件，二是写博客。推荐安装 vscode 的几个插件：

* [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one) 提供了 markdown 的快捷键，以及公式编辑等功能
* [Markdown Preview Enhanced](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced) 提供了 markdown 的即时预览工具，并且可以切换多种主题，包括 github 主题，可以随时导出 pdf, html 等格式的文件

安装后打开.md 文件，按 `ctrl+k v` 就可以在侧边打开预览了

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

vs-code 分词是用 `editor.wordSeparators` 作为分隔符，里面只包括了英文半角符号，这导致在写中文 markdown 的时候，`ctrl+shift + 方向键`，会一下子选中一大片，加入中文全角符号可以显著改善这一现象。

在 vscode 中，按 `ctrl+shift+P`，输入 `Preference: Settings (UI)`，找到 `editor.wordSeparators`，在后面加上

    ，。？：“”、《》（）

就可以了

## 直接插入图片

markdown 的插入图片是用如下格式

    ![image name](/image/path)

也就是要把图片存在一个路径，然后用文本去指向那个路径。如果我们写文章的时候，每张图片都手动去存再去链接，非常的麻烦，所以可以用 vscode 的 [Paste Image 插件](https://marketplace.visualstudio.com/items?itemName=mushan.vscode-paste-image)。

安装以后，打开 settings.json，加上下面几行

    "pasteImage.basePath": "${projectRoot}",
    "pasteImage.path": "${projectRoot}/assets/images/${currentFileName}",
    "pasteImage.prefix": "/"

保存设置，以后就可以在编辑时，复制图片或截图后，按 `Ctrl+Alt+v`，自动插入剪切板里的图片了

![](/assets/images/2022-06-03-markdown-tutorial.md/2022-06-13-15-57-17.png)

图片会保存到 `/assets/images/` 路径下，文件名是精确到秒的时间，不用担心覆盖掉其它图片。markdown 文件里会自动多出一行引用图片文件的语句。

    ![](/assets/images/2022-06-03-markdown-tutorial.md/2022-06-13-15-57-17.png)

## 设置自定义的代码补全

vsvode 里，代码自动补全功能叫做 snippets，可以用一小段代码索引出来一大段。当你经常输入一大段固定格式的代码，这个功能就很有用。对于 markdown 写博客来说，对补全功能需求最高的莫过于插入 html 语言了，两种语言之间的切换是真的烦。比如输入如下代码可以插入一个 html 文件或 pdf 文件

```html
<div style="position: relative; padding: 30% 45%;">
<iframe style="position: absolute; width: 100%; height: 100%; left: 0; top: 0;" src="/path/to/file" frameborder="no" scrolling="no" allowfullscreen="true"></iframe>
</div>
```

但谁记得住这么长串啊！不要紧，可以设置 snippets，按 `ctrl+shift+p`，打 snippets，进入 `Configure User Snippets`，选择 `markdown` 语言，就会打开一个 `markdown.json` 文件。在里面插入

```json
  "inserthtml":{
  "prefix": "iframe",
  "body": [
    "<div style=\"position: relative; padding: 30% 45%;\">",
    "<iframe style=\"position: absolute; width: 100%; height: 100%; left: 0; top: 0;\"src=\"$1\"frameborder=\"no\"scrolling=\"no\"allowfullscreen=\"true\"></iframe>",
    "</div>"],
  "description": "insert an html or a pdf"
  }
```

保存，再打开 `setting.json`，加入

```json
  "[markdown]": {
      "editor.quickSuggestions": {
          "strings": "on"
      }
  }
```

保存，这样在.md 文件里输入 `iframe`，会有类似写代码的时候的自动补全选项跳出来，按回车，上面的一大段代码就自动插入了

![](/assets/images/2022-06-03-markdown-tutorial.md/2022-06-13-17-17-10.png)

类似的方法可以用在插入 youtube 或 bilibili 视频上，当然写其它语言的代码的时候也非常方便。

我自己用的 `markdown.json` 文件也放到 [这里了](/assets/images/2022-06-03-markdown-tutorial.md/markdown.json){:target="_blank"}，里面实现了

| Snippets             | prefix     |
| :------------------- | :--------- |
| insert html iframe   | `iframe`   |
| yml title            | `title`    |
| insert bilibili      | `bilibili` |
| bold red text        | `redtext`  |
| auto-fold content    | `detail`   |
| assets path          | `assets`   |
| link open at new tab | `link`     |

