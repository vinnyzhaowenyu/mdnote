---
title: Getting started with the Documentation Theme for Jekyll
keywords: sample homepage
tags: [getting_started]
sidebar: note_sidebar
permalink: note_jekyll_theme_index.html
summary:  介绍jekyll 主题的使用
---

## 构建使用主题 

通过以下的的介绍来构建使用该主题

### 1. 主题下载 

在[Github](https://github.com/tomjohnson1492/documentation-theme-jekyll)上下载或者clone这个主题.一旦你定制好了主题,最好不要使用git pull来更新他。建议在Github上点击*Clone or download*按钮，然后选择**Download ZIP**。

### 2. 安装Jekyll

如果你的机器上没有安装使用过Jekyll，一下的介绍将会安装Jekyll

* [在Mac上安装Jekyll][mydoc_install_jekyll_on_mac]
* [在Windows上安装Jekyll][mydoc_install_jekyll_on_windows]

### 3. 安装 Bundler

如果没有安装Bundler就安装他：

```
gem install bundler
```

你需要确认环境中所有的Ruby gems的[Bundler](http://bundler.io/)正常使用，Bundler依赖对应版本的gems

### 4. Option 1: 安装主题 (*without* the github-pages gem) {#option1}

如果你不打算在[Github Pages](https://pages.github.com/)上开发你的Jekyll站点，就是用下面的操作。

Bundler的Gemfile需要指定，他能管理项目的软件依赖。尽管该项目已经包含了一个Gemfile，但这个主题除了Jekylly外没有任何依赖。
这个Gemfile被用来指定开饭到Github Pages需要的gems。**如果你不打算在GitHub上开放的Jekyll项目，删除项目主目录下的这两个文件**

* Gemfile
* Gemfile.lock

如果你没有在你的机器上运行过Jekyll(可以使用`jekyll --version`),你需要安装jekyll gem:

```
gem install jekyll
```

现在运行jekyll 服务(需要跳转到项目的主目录中(`cd`)):

```
jekyll serve
```

### 4. Option 2: 安装 (*with* the github-pages gem) {#option2}

如果你在Github Pages开放你的项目，保留Gemfile和Gemfile.local文件。Gemfile告诉Jekyll使用Github-pages gem。**然而，注意你不能使用命令`jekyll server`，他依赖最新版本的Jekyll和Github Pages**(该问题已经被记录[briefly here](https://help.github.com/articles/setting-up-your-github-pages-site-locally-with-jekyll/)).

你需要使用Bundler来解决依赖，使用Bundler来安装所有的Ruby Gems依赖:

```
bundle update
```

通常使用这个命令来运行Jekyll:

```
bundle exec jekyll serve
```

如果你想使用更加精炼的命令，你可以将这个命令放在一个脚本中jekyll.sh，然后使用简单命令来运行Jekyll`. jekyll.sh`

## 在Docker中运行站点 

你可以在你的机器上使用Docker直接构建一个运行的站点。只需要在项目目录中下载repo文件和运行下面这条命令

```
docker build --no-cache -t mydocs .
```

一旦Docker Images构建完成，你可以挂载和使用整个站点:

```
docker run -v "$PWD:/src" -p 4000:4000 mydocs serve -H 0.0.0.0
```

这或许是最简单方法来构建你的站点了。

## 配置侧边导航(sidebar)

这个主题中有多个效果(products).每个效果使用不同的侧边导航.实际上是为了区分不同类型的文档使用不同的侧边导航.这个思路是由于用户阅读文档时要有一个合适侧边导航。(你可以获取更多的关于侧边导航信息在[这个Blog中](http://idratherbewriting.com/2016/03/23/release-of-documentation-theme-for-jekyll-50/).)

同样保留的顶面水平导航(navigation)，因为他运行用户快速跳转不同的产品内容。侧边导航需要适配不同的产品

由于每个产品使用不同的侧边导航，你需要设置你的站点的侧边导航。他是在 \_includes/custom 目录中 “sidebarconfigs.html”的文件。这个文件控制哪种侧边导航关联何种产品。打开这个文件查看内容

sidebarconfigs.html文件使用简单的`if elsif`逻辑设置一个变量，logic to set a variable that the sidebar.html file uses to read the sidebar data file. sidebarconfigs.html中的代码就像这样:

{% raw %}
```liquid
{% if page.sidebar == "home_sidebar" %}
{% assign sidebar = site.data.sidebars.home_sidebar.entries %}

{% elsif page.sidebar == "product1_sidebar" %}
{% assign sidebar = site.data.sidebars.product1_sidebar.entries %}

{% elsif page.sidebar == "product2_sidebar" %}
{% assign sidebar = site.data.sidebars.product2_sidebar.entries %}

{% elsif page.sidebar == "mydoc_sidebar" %}
{% assign sidebar = site.data.sidebars.mydoc_sidebar.entries %}

{% else %}
{% assign sidebar = site.data.sidebars.home_sidebar.entries %}
{% endif %}
```
{% endraw %}

In each page's frontmatter, you must specify the sidebar you want that page to use. Here's an example of the page frontmatter showing the sidebar property:
每个页面的frontmatter都需要指定一个sidbar，下面这是一个例子:

<pre>
---
title: Alerts
tags: [formatting]
keywords: notes, tips, cautions, warnings, admonitions
last_updated: July 3, 2016
summary: "You can insert notes, tips, warnings, and important alerts in your content. These notes are stored as shortcodes made available through the linksrefs.hmtl include."
<span class="red">sidebar: mydoc_sidebar</span>
permalink: mydoc_alerts
---
</pre>

这里 `sidebar: mydoc_sidebar` 会链接到 \_data/sidebars/mydoc_sidebar.yml 文件 (意思是, mydoc_sidebar.yml 文件插入到 sidebars子目录\data中).

如果在frontmatter没有指定sidebar，就会使用默认的sidebar(`else`指定的内容，即`site.data.sidebars.home_sidebar.entries`)

注意你的sidebar只能包含2层，每个product都有自己的侧边导航，这样分类深度就足够了，就像有了3层深度了。不建议有更深层次的分类嵌套

{% include note.html content="Note that each level must have at least one topic before the next level starts. You can't have a second level that contains multiple third levels without having at least one standalone topic in the second level." %}


你可以在任意页面打开或者关闭侧边导航(例如:首页).关闭页面侧边导航，就是设置页面的frontmatter tag为`hide_sidebar:true`

更多关于侧边导航的信息，查看[Sidebar navigation][mydoc_sidebar_navigation]

## 侧边导航的语法 

侧边导航的配置文件使用YAML语法,下面给出一个例子：

```yaml
entries:
- title: sidebar
  product: Jekyll Doc Theme
  version: 6.0
  folders:

  - title: Overview
    output: web, pdf
    folderitems:

    - title: Get started
      url: /index.html
      output: web, pdf

    - title: Introduction
      url: /mydoc_introduction.html
      output: web, pdf

    - title: Supported features
      url: /mydoc_supported_features.html
      output: web, pdf

    - title: About the theme author
      url: /mydoc_about.html
      output: web, pdf

    - title: Support
      url: /mydoc_support.html
      output: web, pdf

  - title: Release Notes
    output: web, pdf
    folderitems:

    - title: 6.0 Release notes
      url: /mydoc_release_notes_60.html
      output: web, pdf

    - title: 5.0 Release notes
      url: /mydoc_release_notes_50.html
      output: web, pdf

```

每个`folder`或者`subfolder`必须包含`title`和`output`所属。每个`folderitem`or`subfolderitem`必须包含`title`,`url`和`output`所属

只有`web`和`pdf`两个outputs可用.(即使你不出版成PDF,你仍然需要指明`output:web`)

YAML语法依赖空格缩进，因此确保你的pattern是属于相同的侧边导航分类。查看[YAML tutorial](mydoc_yaml_tutorial)可以了解更详细的关于YAML的配置

To accommodate the title page and table of contents in PDF outputs, each product sidebar must list these pages before any other:

```yaml
- title:
  output: pdf
  type: frontmatter
  folderitems:
  - title:
    url: /titlepage
    output: pdf
    type: frontmatter
  - title:
    url: /tocpage
    output: pdf
    type: frontmatter
```

Leave the output as `output: pdf` for these frontmatter pages so that they don't appear in the web output.

更详细在[Sidebar navigation][mydoc_sidebar_navigation]和[YAML tutorial][mydoc_yaml_tutorial]

## 相关链接和离线预览

这个主题使用相关链接来浏览，因此你可以在你的电脑上离线浏览而不需要一个主机或空间。他通常用来在内部服务器上上传一些学习文档提供浏览。由于需要在各个主机间无缝跳转，因此使用了相关链接方式访问。

## 页面格式化 

当编文章时，每个页面都需要有以下的格式内容。

```yaml
---
title: "Some title"
tags: [sample1, sample2]
keywords: keyword1, keyword2, keyword3
last_updated: Month day, year
summary: "optional summary here"
sidebar: sidebarname
permalink: filename.html
---
```

( 你必须在每个页面都指定这些值 ) 

对于`title`标题，需要使用双引号括起来。如果标题本身包含双引号，需要使用反斜杠`\`转意。

对于`keywords`中的关键词，主要用来提供SEO，便于搜索引擎分析。

对于`tags`，必须在\_data/tags.yml中定义。需要在tags目录中创建一致的tag文件，格式可以参考同目录下的其他文件。(Jekyll 不会自动创建tag文件.)

如果你不需要mini-TOC在页面上展示(例如：homepage 或landing pages)，可以增加`toc: false`在页面格式化配置

对于`permalink`值，应该和文件名相同，但需要以`.html`为后缀。

更多详细内容，查看[Pages][mydoc_pages].

## 文章保存 

可以将文章保存在模板的下的子目录中。例如：product1，product2等等，可以保存在\_pages目录的子目录中。在\_pages目录，你可以保存你的子分类，或者子子分类。当Jekyll构建站点时，会解析这些文件为permalink的URL并保存在一个web根目录中。


Note that product1, product2, and mydoc are all just sample content to demonstrate how to add multiple products into the theme. You can freely delete that content.

For more information, see [Pages][mydoc_pages] and [Posts][mydoc_posts].

## Configure the top navigation

The top navigation bar's menu items are set through the \_data/topnav.yml file. Use the top navigation bar to provide links for navigating from one product to another, or to navigate to external resources.

For external URLs, use `external_url` in the item property, as shown in the example topnav.yml file. For internal links, use `url` the same was you do in the sidebar data files.

Note that the topnav has two sections: `topnav` and `topnav_dropdowns`. The topnav section contains single links, while the `topnav_dropdowns` section contains dropdown menus. The two sections are independent of each other.

## Generating PDF

If you want to generate PDF, you'll need a license for [Prince XML](http://www.princexml.com/). You will also need to [install Prince](http://www.princexml.com/doc/installing/).  You can generate PDFs by product (but not for every product on the site combined together into one massive PDF). Prince will work even without a license, but it will imprint a small Prince image on the first page, and you're supposed to buy the license to use it.

If you're on Windows, install [Git Bash client](https://git-for-windows.github.io/) rather than using the default Windows command prompt.

Open up the css/printstyles.css file and customize the email address (`youremail@domain.com`) that is listed there. This email address appears in the bottom left footer of the PDF output. You'll also need to create a PDF configuration file following the examples shown in the pdfconfigs folder, and also customize some build scripts following the same pattern shown in the root: pdf-product1.sh

See the section on [Generating PDFs][mydoc_generating_pdfs] for more details about setting the theme up for this output.

## Blogs / News

创建markdown文件在\_posts目录中,Post file命名是以日期开头(YYYY-MM-DD-title)

news/news.html 文件
The news/news.html file displays the posts, and the news_archive.html file shows a yearly history of posts. In documentation, you might use the news to highlight product features outside of your documentation, or to provide release notes and other updates.

See [Posts][mydoc_posts] for more information.

## Markdown语法

该主题使用 [kramdown markdown](http://kramdown.gettalong.org/).kramdown 是一个简单的Github偏好的Markdown，当你使用文本列表时，列表上下需要一个空白行，然后第一个字符串是列表数字，而且在点后面接两个空格，就像这样:

```
1.  First item
2.  Second item
3.  Third item
```

当你要插入段落，标记，代码或者其他内容在列表中时，前面使用4个空格。 The four spaces will line up with the first letter of the list item (the <b>F</b>irst or <b>S</b>econd or <b>T</b>hird).

```
1.  First item

    ```
    alert("hello");
    ```

2.  Second item

    Some pig!

3.  Third item
```

See the topics under "Formatting" in the sidebar for more information.

## 自动化链接

如果想使用一个自动系统 
If you want to use an automated system for managing links, see [Automated Links][mydoc_hyperlinks.html#automatedlinks]. This approach automatically creates a list of Markdown references to simplify linking.

## Other instructions

The content here is just a getting started guide only. For other details in working with the theme, see the various sections in the sidebar.

{% include links.html %}
