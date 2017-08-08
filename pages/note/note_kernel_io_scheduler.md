---
title:  IO调度算法
keywords: aa 
last_updated: June 1, 2017
tags: [getting_started]
summary: aa 
sidebar: note_sidebar
permalink: note_io.html
folder: note 
---

```
1.dmesg | grep -i scheduler //查看当前系统支持的IO调度算法
2.cat /sys/block/sda/queue/scheduler //查看当前系统的IO调度算法
3.echo noop > /sys/block/sda/queue/scheduler //临地更改I/O调度方法:
```

http://alanwu.blog.51cto.com/3652632/1393068/
https://gitsea.com/2013/05/03/linux-io-%E8%B0%83%E5%BA%A6%E6%96%B9%E6%B3%95/

{% include links.html %}
