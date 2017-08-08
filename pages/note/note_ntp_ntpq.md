---
title: ntpq命令 
keywords: ntpq 
last_updated: June 6, 2017
tags: [getting_started]
summary: ntp命令介绍 
sidebar: note_sidebar
permalink: note_ntp_ntpq.html
folder: note 
---

## 语法

```
ntpq [-46dinp] [-c command] [host] [...]
```

## 介绍

`ntpq`命令可以用来监控NTP进程`ntpd`的运行状况和确定性能。
他使用标准的NTPv3文档RFC1305的附录B中的信息格式(mode 6)。
NTPv4也是使用这个格式，不过被被修改了名称并新增加了一个。
这里介绍的是NTPv4版本的。

ntpq程序可以运行在交互模式，或者命令行参数模式。

ntpq向多个服务端发送请求，获取并打印出一个列表。

执行ntpq时，如果指定了一个或多个请求参数，每个请求都将发往NTP Server，localhost是默认的NTP Server。
如果没有指定参数，ntpq将进入一个命令行。
如果标准输出示终端设备，ntpq将立即输出。

ntpq使用NTP mode 6数据包和NTP Server通信，今后能够在任何允许的网络服务器上，使用兼容的方式进行查询。
以前部分使用UDP协议的NTP可能无法使用，特别是那些有着巨大的网络拓补的环境。
如果远程主机很难快速响应，ntpq尝试选择一台来转发请求。

需要注意使用主机名的情况，指定`-4`是要求DNS解析成IPv4，指定`-6`则要解析成IPv6

在命令行指定`-i`或者`-n`将会立即发送请求，否则ntpq会进入标准输入。

## ntpq选项

* -4

强制DNS将主机名解析成IPv4

* -6

强制DNS将主机名解析成IPv6

* -c

后面的参数解析成交互格式，同时增加到列表中，在指定的机器上执行。 可以指定多`-c`。

* -d

运行在debuggine模式

* -i

强制ntpq使用交互模式。提示信息将从标准输入读，并写入到标准输出，

* -n

显示IP地址而不是主机名

* -p

将多个对等的服务状态显示成一个列表，这相当于交互命令。


## ntpq命令

``` 
ntpq -np
```

```
     remote           refid      st t when poll reach   delay   offset  jitter
==============================================================================
 61.216.153.105  .INIT.          16 u    -   64    0    0.000    0.000   0.000
x45.76.98.188    10.84.87.146     2 u   10   64    1  114.294  -25.941   0.943
 163.172.177.158 .INIT.          16 u    -   64    0    0.000    0.000   0.000
*202.118.1.130   202.118.1.47     2 u    8   64    1   51.441    0.500   0.410
```

* [字段含义](http://doc.ntp.org/4.2.8/ntpq.html)

| 参数 | 描述 |
|:---:|--|
|remote| 它指的就是本地机器所连接的远程NTP服务器。|
|refid| 它指的是给远程服务器提供时间同步的服务器|
|st| 远程服务器的层级别（stratum）. 由于NTP是层型结构,有顶端的服务器,多层的Relay Server再到客户端. 所以服务器从高到低级别可以设定为1-16. 为了减缓负荷和网络堵塞,原则上应该避免直接连接到级别为1的服务器的|
|t| u: unicast or manycast client, b: broadcast or multicast client, l: local (reference clock), s: symmetric (peer), A: manycast server, B: broadcast server, M: multicast server |
|when|距离上次同步已经过去的秒数| 
|poll| 本地机和远程服务器多少时间进行一次同步(单位为秒). 在一开始运行NTP的时候这个poll值会比较小,那样和服务器同步的频率也就增加了,可以尽快调整到正确的时间范围.之后poll值会逐渐增大,同步的频率也就会相应减小. (log2 s)|
|reach| 这是一个八进制值,用来测试能否和服务器连接.每成功连接一次它的值就会增加|
|delay| 从本地机发送同步要求到服务器的round trip time|
|offset| 这是个最关键的值, 它告诉了我们本地机和服务器之间的时间差别. offset越接近于0,我们就和服务器的时间越接近|
|jitter| 这是一个用来做统计的值. 它统计了在特定个连续的连接数里offset的分布情况. 简单地说这个数值的绝对值越小我们和服务器的时间就越精确|


* [remote 标记种类](http://doc.ntp.org/4.2.8/decode.html#peer)

|标记|描述|
|:--:|---|
|(空格)| discarded as not valid (TEST10-TEST13) |
|X|该ntp server不可用|
|.|discarded by table overflow (not used)|
|-|远程服务器被clustering algorithm认为是不合格的NTP Server|
|+|它将作为辅助的NTP Server和带有*号的服务器一起为我们提供同步服务. 当*号服务器不可用时它就可以接管|
|#|backup (more than tos maxclock sources)|
|*|当前正在使用的ntp server|
|o|PPS peer (when the prefer peer is valid)|


## Links
[http://doc.ntp.org/4.2.8/ntpq.html](http://doc.ntp.org/4.2.8/ntpq.html)

{% include links.html %}
