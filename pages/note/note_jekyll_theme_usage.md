---
title: 使用Jekyll主题 
keywords: documentation theme, jekyll, technical writers, help authoring tools, hat replacements
last_updated: June 1, 2017
tags: [getting_started]
summary: "安装运行Jekyll Theme主题后，如果使用呢？"
sidebar: note_sidebar
permalink: note_jekyll_theme_usage.html
folder: note 
---


## 创建新top分类

### 创建新目录树文件
top分类可以配置一个目录索引，新目录索引配置文件可以从其他文件复制一份修改

```
_data/sidebars/note_sidebar.yml
```

### 修改目录索引配置
新建立的侧边导航必须要配置这个

```
_includes/custom/sidebarconfigs.html
```

添加新的分类

```
\{\% elsif page.sidebar == "note_sidebar" \%\}
\{\% assign sidebar = site.data.sidebars.note_sidebar.entries \%\}

\{\% if site.product == "note" \%\}
\{\% assign sidebar_pdf = site.data.sidebars.note_sidebar.entries \%\}
\{\% endif \%\}
```

### 增加top导航链接

```
_data/topnav.yml
```

```
- title: Topnav
  items:
    - title: 技术笔记 
      url: /note_index.html
```

### 创建该分类的目录的md文件


```
pages/note/note_how_to_use_jekyll_theme.md
```


## 构建Web代码

```
cd /mdnote && bundle exec jekyll build
```







--------------------



## 添加一篇新文章

### 配置导航连接

在侧边导航配置文件中创建一个目录，或者使用已有的目录创建一篇文章导航

这里的目录和文章只是侧边导航中的一个连接，通过这个连接可以打开相应的文件

### 创作文章

在pages目录中创建一个一个目录或者在一个已经存在的目录中创建md文件

```
pages/note/note_linux_ntpd.md
```

这里pages下note目录创建后需要在`_includes/custom/sidebarconfigs.html`文件中声明


## 配置Github地址

指定Github项目的位置

```
github_editme_path: vinnyzhaowenyu/mdnote/tree/master/mdnote/
```


## 添加一个分类 

配置一个侧边导航
_data/sidebars/note_sidebar.yml


配置顶部导航
_data/topnav.yml

创建一个目录note，将md文件放置在该目录中
pages/note/note_how_to_use_jekyll_theme.md

## 注意细节

在顶部的配置内容部分`: ` 后面一定要添加一个空格，否则md解析无法通过

{% include links.html %}
