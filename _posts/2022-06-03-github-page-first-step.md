---
title: 学习Github page写博客
date: 2022-06-03 15:20:00 +0800
categories: blogs
tags: [Github, jekyll]
---

Github可以建立个人静态网页，虽然只能写写博客，但省去了搭服务器、申请公网ip、买域名等复杂的步骤。

<!-- more -->

# Github page和Jekyll介绍

#### Github page建立个人主页

操作也很简单，[官方教程](https://pages.github.com/)说得很清楚

1. 创建一个**公库**，叫做`USERNAME.github.io`，这里的`USERNAME`是你的github账户名
2. 在库的setting里选择一个theme，也可以用其它的Jekyll theme，我这里用的就是一个叫[NexT](https://github.com/Simpleyyt/jekyll-theme-next)的第三方主题
3. 按照主题教程修改`_config.yml`和`index.md`两个文件即可编辑网页风格和主页内容
4. 已经可以了，在浏览器中输入`USERNAME.github.io`，就能打开你的主页了，每次修改后大概要等1-2分钟才会完成网页同步

#### 每个仓库可以有一个Github page



#### Jekyll

这是一个从markdown等文本文件生成静态网页的网页编译器，是基于ruby语言的，可以在本机装一个Jekyll，然后编译网页，host一个自己的服务器。但我没装，Github会自动编译`USERNAME.github.io`里面的


# 撰写博客

最详细的教程当然是[Jekyll官方文档](http://jekyllcn.com/docs/posts/)，这里只记录一些很重要的，以及文档里没有的知识点。

## 博客文章规范

文章用markdown写，也支持一些其它格式，文件要放在`_post`文件夹下，命名要符合下面的规范

```
年-月-日-标题.md
如 2011-12-31-new-years-eve-is-awesome.md
```

md文件开头要有一段yml信息，对于博客文章而言大概是这样

    ---
    title: 学习Github page写博客
    date: 2022-06-03 15:20:00 +0800
    categories: blogs
    tags: [Github, jekyll]
    ---

date的+0800表示时区在东八区，不能省略，如果时间设定成未来时间，Jekyll在编译时会跳过这篇文章，详情见[使用Jekyll时遇到的时区问题](https://changwh.github.io/2019/03/17/timezone-issue-in-jekyll/#:~:text=%E5%9B%A0%E6%AD%A4%EF%BC%8Cjekyll%E9%BB%98%E8%AE%A4%E4%BD%BF%E7%94%A8UTC%E6%97%B6%E9%97%B4%E3%80%82)。

头文件后，用markdown语言编写即可，markdown的编辑器有很多，推荐使用vscode，[详细教程]()

## 缩略展示

1. 在_config.yml文件里，设置`excerpt_separator: <!-- more -->`
2. 在文章中想要截断的地方加上`<!-- more -->`，则从主页看到的文章会显示这段之前的文字，展开阅读下文


## 代码高亮

markdown的代码是用\`键，即`~`下面的那个，把代码框起来，多行的话则是用三个\`前后框住，在前面三个撇之后声明使用的语言就可以按照该语言的格式高亮。

[支持语言和对应声明方式一览](https://blog.csdn.net/u012102104/article/details/78950290)


    ```ruby
    def show
      @widget = Widget(params[:id])
      respond_to do |format|
        format.html # show.html.erb
        format.json { render json: @widget }
      end
    end
    ```

（btw，上面这段是通过在每行代码前面加上四个空格打出来的，在markdown里这叫做“代码围栏”）
显示效果如下

```ruby
def show
  @widget = Widget(params[:id])
  respond_to do |format|
    format.html # show.html.erb
    format.json { render json: @widget }
  end
end
```

Jekyll支持另一种高亮方法，在正常的markdown预览器中无法显示，但编译成网页后显示正常，而且**可以切换高亮风格**(不过我觉得原生的很够用了)

    {% highlight ruby %} def foo puts 'foo' end {% endhighlight %}

    {% highlight ruby linenos %} def foo puts 'foo' end {% endhighlight %}

{% highlight ruby %} def foo puts 'foo' end {% endhighlight %}

{% highlight ruby linenos %} def foo puts 'foo' end {% endhighlight %}

## 插入图片

和markdown一样，Jekyll是可以插入网络图片的

    ![图片名](图片链接)
    如 ![img](https://markdown.com.cn/assets/img/philly-magic-garden.9c0b4415.jpg)

![img](https://markdown.com.cn/assets/img/philly-magic-garden.9c0b4415.jpg) 

如果要插入自己的图片，就把图片上传到博客repo根目录的`/assets`文件夹里，再用相对目录索引

    ![img](/assets/20220603/shiprock.c3b9a023.jpg)

![img](/assets/20220603/shiprock.c3b9a023.jpg)