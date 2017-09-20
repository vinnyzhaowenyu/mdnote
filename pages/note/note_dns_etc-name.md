---
title: /etc/named.conf
keywords: dns 
last_updated: August 10, 2017
tags: [dns,service,config,named]
summary: dns主配置文件
sidebar: note_sidebar
permalink: note_dns_etc-named.html
folder: note 
---

## /etc/named.conf 配置文件
`/etc/named.conf`是DNS协议实现软件bind的进程named的主配置文件,其他部分配置文件会通过include的方式包含在主配置中。
### key
```
key "rndc-key" {
    algorithm hmac-md5;
    secret "kBw8Lfdsafsdfdsfsdacg==";
};
```
* key :
* algorithm :
* secret :

### controls
```
controls {
    inet 127.0.0.1 port 953;
    allow { 127.0.0.1; } keys { "rndc-key"; };
};
```
* controls :
* inet :
* allow :

### 主备DNS配置
```
acl slavedns { 
    172.31.57.161;
};
```
* acl :
* IPADDR : 

### options 全局配置
options是named的全局配置
```
options { 
    listen-on port 53 { 127.0.0.1;0.0.0.0/0 };
    listen-on-v6 port 53 { ::1; };
    directory       "/var/named";
    dump-file       "/var/named/data/cache_dump.db";
    statistics-file "/var/named/data/named_stats.txt";
    memstatistics-file "/var/named/data/named_mem_stats.txt";
    allow-query     { localhost; };
    recursion yes;
    dnssec-enable yes;
    dnssec-validation yes;
    dnssec-lookaside auto;
    bindkeys-file "/etc/named.iscdlv.key";
    managed-keys-directory "/var/named/dynamic";
};
```
* listen-on : 监听的端口和提供服务IP，IP可以配置any或0.0.0.0不限制客户端
* listen-on-v6 : ipv6的监听
* directory : 住配置文件，这个必须有，而且必须是这个位置，不能修改
* dump-file : 缓存文件存放的地方，默认没有。要是用rpch dumpdb同步内存
* statistics-file : 统计dns
* memstatistics-file : 统计dns服务消耗的内存及时间段
* allow-query : 
* recursion : 是否解析互联网dns，默认是yes
* dnssec-enable : 
* dnssec-validation :
* dnssec-lookaside :
* bindkeys-file :
* managed-keys-directory :

### logging
```
logging {
    channel default_debug {
        file "data/named.run";
        severity dynamic;
    };
};
```
* logging :
* channel :
* file :
* severity :

### zone
```
zone "." IN { 
    type hint;
    file "named.ca";
};
```
* zone : 用来定义一个域，这里点代表根域，全球的根域服务器保存在name.ca文件中   
* type : 用来定义角色。`hint`表示互联网根域，`master`表示主域名服务器，`slave`表示辅助域名服务器   
* file : 用来指定该域DNS记录文件，默认路径保存在/var/name/中   

```
zone "test.com" IN {
    type master;
    file "test.com" ;
    allow-update { none; };
};
```
* zone "test.com" :  定义域名为localhost的正向解析域

```
zone "0.192.168.in-addr.arpa" IN { //定义一个IP为168.192.0.*反向域区
    type master;
    file "168.192.0";
};
```
* zone "0.168.192.in-addr.arpa" :  指定IP地址`192.168.0.*`的反向解析域

### include
```
include "/etc/named.rfc1912.zones";
include "/etc/named.root.key";
```
* include : 把其他配置文件包含进来 

{% include links.html %}
