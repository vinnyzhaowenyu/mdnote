---
title: DNS服务配置
keywords: dns 
last_updated: August 10, 2017
tags: [dns,service,config]
summary: dns服务配置
sidebar: note_sidebar
permalink: note_dns_config.html
folder: note 
---

## 配置文件

## /etc/named.conf

```
key "rndc-key" {
      algorithm hmac-md5;
      secret "kBw8Lfdsafsdfdsfsdacg==";
};

controls {
      inet 127.0.0.1 port 953
      allow { 127.0.0.1; } keys { "rndc-key"; };
};

acl slavedns {    #主备DNS配置
    172.31.57.161;
};

options {        全局配置
        listen-on port 53 { 127.0.0.1;0.0.0.0/0 };   监听的端口和提供服务IP，IP可以配置any或0.0.0.0不限制客户端
        listen-on-v6 port 53 { ::1; };    ipv6的监听
        directory       "/var/named";住配置文件，这个必须有，而且必须是这个位置，不能修改
        dump-file       "/var/named/data/cache_dump.db";缓存文件存放的地方，默认没有。要是用rpch dumpdb同步内存
        statistics-file "/var/named/data/named_stats.txt";       统计dns
        memstatistics-file "/var/named/data/named_mem_stats.txt";统计dns服务消耗的内存及时间段
        allow-query     { localhost; };      可以删除
        recursion yes;  是否解析互联网dns，默认是yes

        dnssec-enable yes;可以删除
        dnssec-validation yes;可以删除
        dnssec-lookaside auto;可以删除

        /* Path to ISC DLV key */
        bindkeys-file "/etc/named.iscdlv.key";

        managed-keys-directory "/var/named/dynamic";
};

logging {
        channel default_debug {
                file "data/named.run";
                severity dynamic;
        };
};

zone "." IN {
        type hint;      
        file "named.ca";
};

include "/etc/named.rfc1912.zones";    把文件包含进来，
include "/etc/named.root.key";
```





## /var/name/ 


{% include links.html %}
