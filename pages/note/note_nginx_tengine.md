---
title: Tengine介绍
keywords: tengine 
last_updated: June 12, 2017
tags: [getting_started]
summary: aa 
sidebar: note_sidebar
permalink: note_nginx_tengine.html
folder: note 
---

Tengine是由淘宝网发起的Web服务器项目。它在Nginx的基础上，针对大访问量网站的需求，添加了很多高级功能和特性。Tengine的性能和稳定性已经在大型的网站如淘宝网，天猫商城等得到了很好的检验。它的最终目标是打造一个高效、稳定、安全、易用的Web平台。


## Tengine 编译安装

如果不需要其他任何模块，可一直按照以下步骤。如果需要添加其他模块可以查看参考下文的shell脚本内容

```
./config
make
make install
```


## Tengine 离线一键安装包

[一键安装包下载地址](http://wenyu-mdnote.oss-cn-shanghai.aliyuncs.com/tengine-install-tools-v8.tar.gz)

使用方法:

执行`install-tools.sh`会自动将软件安装到`/usr/local/tengine`目录中。服务脚本tengine可以像管理普通服务一样启动和停止。

* `install-tools.sh`脚本内容

```
#!/bin/bash

if [ -f 'tengine-2.2.0.tar.gz' -a -f 'zlib-1.2.11.tar.gz' -a -f  'pcre-8.39.tar.gz' -a -f 'openssl-1.0.2.tar.gz' ]; then
    mkdir /usr/local/tengine
    tar xf zlib-1.2.11.tar.gz   -C /usr/local/
    tar xf pcre-8.39.tar.gz     -C /usr/local/
    tar xf openssl-1.0.2.tar.gz -C /usr/local/
    tar xf tengine-2.2.0.tar.gz 
fi

cd tengine-2.2.0 && ./configure  \
--prefix=/usr/local/tengine  \
--with-zlib=/usr/local/zlib-1.2.11 \
--with-pcre=/usr/local/pcre-8.39 \
--with-openssl=/usr/local/openssl-1.0.2

make && make install

cp ../tengine /etc/init.d/ && chmod +x /etc/init.d/tengine

#chkconfig tengine on

#service tengine start
```

## Tengine配置

可以参考Nginx的配置，对于Tengine独有的配置可以参考Tengine的官网


## Tengine链接

* Tengine官网

[http://tengine.taobao.org/](http://tengine.taobao.org/)

* Tegine Github地址

[https://github.com/alibaba/tengine](https://github.com/alibaba/tengine)

* Tengine/Nginx开发中文手册

[http://tengine.taobao.org/book/](http://tengine.taobao.org/book/)

{% include links.html %}
