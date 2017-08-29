---
title: Git SSH免密码push
keywords: git 
last_updated: August 28, 2017
tags: [ssh,git,github]
summary: a
sidebar: note_sidebar
permalink: note_git_ssh.html
folder: note 
---

## 创建SSH秘钥

参考 : [http://www.zhaowenyu.com/note_ssh_rsa.html](http://www.zhaowenyu.com/note_ssh_rsa.html)

## 复制到Github

## git clone

下载使用支持SSH协议的git路径，不能使用https协议。

例如：

```
git clone git@github.com:vinnyzhaowenyu/mdnote.git
```

## 测试

```
git add .
git commit -m "update"
git push
```

{% include links.html %}
