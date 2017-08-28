---
title: Redis介绍
keywords: redis 
last_updated: Augus 28, 2017
tags: [sql]
summary: Key-Value 键值存储 
sidebar: note_sidebar
permalink: note_redis_index.html
folder: note 
---

## 编译安装

```
wget http://download.redis.io/releases/redis-4.0.1.tar.gz
tar xf redis-4.0.1.tar.gz
cd redis-4.0.1
make MALLOC=libc
make install
```

默认会安装在`/usr/loca/bin/`目录，配置文件需要从redis-4.0.1目录中复制`redis.conf`

## 链接登录

```
redis-cli -h host -p port -a password
```

## 参考资料

http://www.runoob.com/redis/redis-tutorial.html

http://www.redis.cn/

https://redis.io/


{% include links.html %}
