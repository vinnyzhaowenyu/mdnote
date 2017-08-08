---
title: Chrome多实例运行
keywords: chrome 
last_updated: June 2, 2017
tags: [chrome]
summary: "Chrome可以在同一台机器上运行多个实例，配置和缓存都相互独立"
sidebar: note_sidebar
permalink: note_chrome_mult_instance.html
folder: note 
---

在日常工作中通常需要多个用户登录到同一个系统中(例如公用跳板机)，但是在同一个Google Chrome实例中不能登录多个用户，因为同一个Google Chrome实例中，后登录的用户的Cookie等信息会覆盖前一登录用户的信息。或者在不同的登录界面不能再次打开Chrome，导致其他用户不能使用Chrome。

同一个Chrome程序运行多个实例就可以解决多用户公用Chrome的问题。

Google Chrome默认的working directory是里面记录了session，cookie等诸多信息，通过创建和配置不同的配置文件可以开启多个相互独立的实例。

Windows、Linux、Mac等操作系统上Chrome可以使用`--user-data-dir=`来配置。

右键Chrome图标，查看快捷方式的属性。

例如Windows平台：在快捷方式属性中可以查看二进制程序的运行路径和程序运行的默认配置目录

```
C:\Users\wenyu\AppData\Local\Google\Chrome\Application\chrome.exe   
C:\Users\wenyu\AppData\Local\Google\Chrome\Application
```

创建新的配置文件存放目录`C:\Users\wenyu\AppData\Local\Google\Chrome\APP1`，然后将新的快捷方式属性中的程序后添加配置路径

```
C:\Users\wenyu\AppData\Local\Google\Chrome\Application\chrome.exe  --user-data-dir="C:\Users\wenyu\AppData\Local\Google\Chrome\APP1"
```

通过创建多个快捷方式启动Chrome，就可以同时运行了

![chrome图片](http://wenyu-mdnote.oss-cn-shanghai.aliyuncs.com/chrome_welcome.png)

{% include links.html %}
