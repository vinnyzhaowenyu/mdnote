---
title: /var/named/domain.com 
keywords: dns 
last_updated: August 10, 2017
tags: [dns,service,config]
summary: dns域名解析文件
sidebar: note_sidebar
permalink: note_dns_var-named-domain.html
folder: note 
---

## /var/name/ 

|DNS解析类型|
|:--:|--|
| SOA   |指示该区的权威|
| NS    |列出该区的一个名字服务器|
| A     |名字到地址的映射|
| PTR   | 地址到名字的映射|
| CNAME | 别名 |
| TTL值 |名字服务器在查询响应中提供这个TTL值，允许其他服务器将数据在缓存中存放TTL所指定的时间。如果你的数据不是经常变动或变动不大，可以考虑将TTL值默认设置为1天。1周大概是这个值的最大限度。象1个小时这样短的值也可以使用，但是我们通常不会建议使用短值。|

```
$TTL    86400
@       IN    SOA   ns.test.net. root.test.net. (
              2007041501      ;Serial
              3600            ;Refresh
              1800            ;Retry
              604800          ;Expire
              86400           ;Minimum TTL
)
              IN        NS    ns.server-linux.info.
              IN        A     172.16.0.82
              IN        MX 10 ns.server-linux.info.
 
ns            IN        A     172.16.0.82
ftp           IN       CNAME   ns.server-linux.info. 
```
* $TTL : 
* @ : `@`符号代表相应的域名，如在这里代表test.net,即表示一个域名记录定义的开始。`IN`表示后面的数据使用的是INTERNET标准。而ns.test.net则是这个域的主域名服务器，而root.test.net则是管理员的邮件地址。注意这是邮件地址中用`.`来代替常见的邮件地址中的`@`.
* Serial : 本行前面的数字表示配置文件的修改版本，格式是年月日当日修改的修改的次数，每次修改这个配置文件时都应该修改这个数字，要不然你所作的修改不会更新到网上的其它DNS服务器的数据库上，即你所做的更新很可能对于不以你的所配置的DNS服务器为DNS服务器的客户端来说就不会反映出你的更新，也就对他们来说你更新是没有意义的。
* Refresh : 定义的是以为单位的刷新频率 即规定从域名服务器多长时间查询一个主服务器，以保证从服务器的数据是最新的。单位是秒？
* Retry :  规定了以秒为单位的重试的时间间隔，即当从服务试图在主服务器上查询更时，而连接失败了，则这个值规定了从服务多长时间后再试
* Expiry : 规定从服务器在向主服务更新失败后多长时间后清除对应的记录，上述的数值是以分钟为单位的
* Minimum TTL : 规定缓冲服务器不能与主服务联系上后多长时间清除相应的记录


### 配置文件注意事项

* 解析记录行首不能有空格

{% include links.html %}
