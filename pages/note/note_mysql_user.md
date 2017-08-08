---
title: MySQL用户管理
keywords: documentation t
last_updated: June 1, 2017
tags: [getting_started]
summary: MySQL用户创建、删除、权限等管理
sidebar: note_sidebar
permalink: note_mysql_user.html
folder: note 
---

MySQL/MariDB关系型数据库的用户合理管理能很好的提供数据库的安全，是DBA的基础技能之一。

## 创建新用户
系统默认有个默认用户`root`,`root`用户用来在本地登录管理;  远程登录MySQL时建议创建一个普通用户。

* 创建新用户并设置密码

```
mysql> create user user00  IDENTIFIED by 'xxxxx';  
```

`IDENTIFIED by` 会将纯文本密码加密作为散列值存储在user表中



## 修改用户名称
用户名需要修改时可以修改用户名

* 使用rename命令修改用户名

```
mysql> rename  user  user00 to  newuser;
```

mysql 5之后可以使用，之前需要使用update 更新user表

* 修改`mysql.user`表修改用户名

```
mysql> update user set username = 'newuser' where username = 'user00' 
```



## 设置用户密码
远程登录的用户必须使用密码，创建新用户没有设置密码是无法连接到MySQL的。给用户配置密码可以有多重方式

* 创建新用户时指定密码

```
mysql> create user  user00 IDENTIFIED by 'xxxxx'; 
```

创建新用户时通过`identified by`指定密码,密码会使用password函数加密保存在`mysql.user`表中

* 使用set命令设置密码

```
mysql> set password for user00  = password('xxxxxx');   
```

root用户可以使用set命令可以直接给用户设置密码,而不用知道原有的密码

* 修改user表设置密码

```
mysql> update  mysql.user  set  password = password('xxxx')  where user = 'otheruser';  
```

无论在创建创建用户时指定密码，还是使用set命令设置密码，最终的加密后密码都会保存在`mysql.user`表中。可以直接修改该表来设置用户密码,设置的密码建议设置成加密过的字符串，或者使用password函数加密。



## 查看用户权限

* 查看一个用户的权限

```
mysql> show grants for user00;
```

* 查看用户在主机上的权限

```
mysql> show grants for user00@10.0.0.1;
```


## MySQL赋予权限

grant和revoke可以在几个层次上控制访问权限      
* 整个服务器，使用 grant ALL  和 revoke  ALL   
* 整个数据库，使用on  database.\*   
* 特点表，使用on  database.table   
* 特定的列   
* 特定的存储过程   

不同的角色需要赋予不同的权限,权限赋予应该按照最小化原则

* 授予user00管理员权限,可以在任意机器上访问

```
mysql> grant all on *.* to user00@'%';      
mysql> grant all privileges *.* to user00@'%';
```
关键字privileges可以省略，以下操作都贱省略该关键字

* 授权user00管理员权限，但来源只能在指定网段内

```
mysql> grant all on *.* to user00@'192.168.0.%';
```

* 授权user00管理权限，但只能在指定IP上访问

```
mysql> grant all on *.* to user00@'192.168.0.10';
```

* 授权user00对test_db库所有权限

```
mysql> grant all on test_db.* to user00@'192.168.0.10';
```

* 授权user00对`test_db.test_table`表的所有权限

```
mysql> grant all on test_db.test_table to user00@'192.168.0.10';
```

* 授权user00指定的几个权限

```
mysql> grant select,update  on test_db.test_table  to user00@'192.168.0.10';
```

* 授权user00在表中列的权限

```
mysql> grant select(id, se, rank) on test_db.test_table to user00@'192.168.0.10';
```

* 授权user00在存储过程、函数上的权限

```
grant execute on procedure test_db.test_table to user00@'192.168.0.10';

grant execute on function test_db.test_table to user00@'192.168.0.10'; 
```



## MySQL权限回收
用户权限设置不合理时需要回收部分或全部权限。回收权限除了将`grant`命令改为`revoke`，还有将`to`改为`from`外，其他部分操作和grant相同。

* 回收指定权限

```
msyql> revoke update  on test_db.test_table  from  user00@'192.168.0.10'; 
```



## 删除用户
mysql5之前删除用户时必须先使用revoke 删除用户权限，然后删除用户，mysql5之后drop 命令可以删除用户的同时删除用户的相关权限更改密码

* 使用drop命令删除用户

```
mysql> drop user newuser;   
```

* 通过删除表记录来删除用户


## 配置生效
修改权限之后权限不会立即生效，需要刷新一下系统的权限，或者重启数据库。

* 刷新数据库权限：

```
mysql> flush  privileges;
```



## `mysql.user`表理解

### user表中host列的值的意义

|键值|描述|
|---|---|
|%           | 匹配所有主机 |
|localhost   | localhost不会被解析成IP地址，直接通过UNIXsocket连接 |
|127.0.0.1   | 会通过TCP/IP协议连接，并且只能在本机访问 |
|::1         | ::1就是兼容支持ipv6的，表示同ipv4的127.0.0.1 |


{% include links.html %}
