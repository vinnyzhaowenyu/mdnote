---
title: SSH代理转发
keywords: aa 
last_updated: August 22, 2017
tags: [ssh]
summary: SSH Proxy 
sidebar: note_sidebar
permalink: note_ssh_proxy.html
folder: note 
---

## SSH本地端口转发(L)

-L port:host:hostport #建立本地SSH隧道(本地客户端建立监听端口)
将本地机(客户机)的某个端口转发到远端指定机器的指定端口. 

## SSH远程端口转发(R)

-R port:host:hostport #建立远程SSH隧道(隧道服务端建立监听端口)
将远程主机(服务器)的某个端口转发到本地端指定机器的指定端口. 
# 有本地映射肯定有远程映射，就是把-L换成-R，这样我们访问远程主机的端口就相当于访问本地的端口，但感觉作用不大。


## SSH动态端口转发(D)

-D port 
指定一个本地机器 “动态的’’ 应用程序端口转发. 
-D是该命令重要参数，他的后面跟着socks5服务器的地址与端口

## SSH图形转发(X)



ssh -C -f -N -L listen_port:DST_Host:DST_port user@Tunnel_Host 
ssh -C -f -N -R listen_port:DST_Host:DST_port user@Tunnel_Host 
ssh -C -f -N -D listen_port user@Tunnel_Host

## 参考

[http://hetaoo.iteye.com/blog/2299123](http://hetaoo.iteye.com/blog/2299123)

[http://www.linuxidc.com/Linux/2016-01/127868.htm](http://www.linuxidc.com/Linux/2016-01/127868.htm)

{% include links.html %}
