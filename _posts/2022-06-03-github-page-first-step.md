---
title: 学习Github page写博客
date: 2022-06-03 15:20:00
categories: blogs
tags: [Github, jekyll]
---

# Github page和Jekyll介绍

#### Github page建立个人主页

Github可以建立个人静态网页，虽然只能写写博客，但省去了搭服务器、申请公网ip、买域名等复杂的步骤。操作也很简单，[官方教程](https://pages.github.com/)说得很清楚

1. 创建一个**公库**，叫做`USERNAME.github.io`，这里的`USERNAME`是你的github账户名
2. 在库的setting里选择一个theme，也可以用其它的Jekyll theme，我这里用的就是一个叫[NexT](https://github.com/Simpleyyt/jekyll-theme-next)的第三方主题
3. 按照主题教程修改`_config.yml`和`index.md`两个文件即可编辑网页风格和主页内容
4. 已经可以了，在浏览器中输入`USERNAME.github.io`，就能打开你的主页了，每次修改后大概要等1-2分钟才会完成网页同步

#### 每个仓库可以有一个Github page


#### Jekyll

这是一个从markdown等文本文件生成静态网页的网页编译器，是基于ruby语言的，可以在本机装一个Jekyll，然后编译网页，host一个自己的服务器。但我没装，Github会自动编译`USERNAME.github.io`里面的


# 编写博客

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

Jekyll支持另一种高亮方法，在正常的markdown预览器中无法显示，但编译成网页后显示正常，而且可以切换高亮风格

    {% highlight ruby %} def foo puts 'foo' end {% endhighlight %}

    {% highlight ruby linenos %} def foo puts 'foo' end {% endhighlight %}

{% highlight ruby %} def foo puts 'foo' end {% endhighlight %}

{% highlight ruby linenos %} def foo puts 'foo' end {% endhighlight %}



## 插入视频

[插入bilibili视频](https://www.cnblogs.com/wkfvawl/p/12268980.html)

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