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

acl slavedns {    #主备DNScocomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcocomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcomcommm配置
    172.31.57.161;
};

options {  全局配置
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

zone "." IN {    /*zone用来定义一个域，这里点代表根域，全球的根域服务器保存在name.ca文件中*/
        type hint;   /*type用来定义角色。hint表示互联网根域，master表示主域名服务器，slave表示辅助域名服务器*/   
        file "named.ca"; /*file用来指定该域DNS记录文件，默认路径保存在/var/name/中 */
};


zone "test.com" IN { /*定义一具域名为localhost的正向区域*/
    type master;
    file "test.com" ;
    allow-update { none; };
};


zone "0.192.168.in-addr.arpa" IN { //定义一个IP为168.192.0.*反向域区
type master;
file "168.192.0";
};




include "/etc/named.rfc1912.zones";    把文件包含进来，
include "/etc/named.root.key";
```






{% include links.html %}
