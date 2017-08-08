---
title: SSH秘钥认证-无密码登录
keywords: ssh 
last_updated: June 20, 2017
tags: [getting_started]
summary: aa 
sidebar: note_sidebar
permalink: note_ssh_rsa.html
folder: note 
---

在一些业务场景下需要快速无密码登录远程服务器，SSH提供无密码认证登录方式。

## 创建秘钥对

创建秘钥对，即公钥和私钥。公钥进行加密，需要发送给远端服务器。而私钥用于解密，需要安全保存。

创建公私钥对可以使用`ssh-keygen`命令，一步步的输入。也可以一次性指定所需要的参数直接生成。如下示例就是直接生成

```
ssh-keygen  -t rsa -P '' -f /root/.ssh/id_rsa
```

```
[root@VM_11_7_centos ~]# ssh-keygen  -t rsa -P '' -f /root/.ssh/id_rsa
Generating public/private rsa key pair.
Your identification has been saved in /root/.ssh/id_rsa.
Your public key has been saved in /root/.ssh/id_rsa.pub.
The key fingerprint is:
ac:ef:85:ca:c7:41:ea:47:98:06:03:56:94:69:f4:37 root@VM_11_7_centos
The key\'s randomart image is:
+--[ RSA 2048]----+
|   ++o           |
|  o +.           |
| . o  . E        |
|    o  o..       |
|     o =S        |
|      =.o.       |
|     o.o...      |
|     ..o+.       |
|      o+o        |
+-----------------+
```

* -t : 加密类型；SSHv1可以使用`rsa1`，对于SSHv2可以使用 `dsa`、 `ecdsa`、 `ed25519` 或者 `rsa` 
* -P : 指定密码；无密码登录这里不能输入内容。
* -f : 秘钥文件路径；默认是`/root/.ssh/id_rsa`

## 发送公钥

发送公钥可以有很多种方式，就是复制`/root/.ssh/id_rsa.pub`文件到目标主机上，可以通过scp、ftp、http、nft、U盘等方法。同时ssh也提供一种便捷的方式`ssh-copy-id`

使用ssh-copy-id可以直接将公钥复制到远端服务器上，并自动配置到`/root/.ssh/authorized_keys`文件。如果使用其他方式复制需要进行下一步配置任务。

```
ssh-copy-id -i /root/.ssh/id_rsa  root@192.168.100.100
```

* -i : identity_file 指定认证文件。默认认证文件是`/root/.ssh/id_rsa`。
* root@ : 默认是用户是当前用户

待验证方法

```
cat ~/.ssh/id_rsa.pub | ssh -p 22 user@host ‘cat >> ~/.ssh/authorized_keys’
```


## 配置认证

如果使用scp等复制文件的方式将`id_rsa.pub`复制到远程服务器上，还需要后续的配置。
将公钥追加到目标的机器`authorized_keys`文件中

```
cat /tmp/192-168-100-99-id_rsa.pub >> /root/.ssh/authorized_keys
```

## 权限配置

在配置使用SSH的时候需要注意一些权限的配置，合理配置当前用户的权限。

例如root用户(需要验证)

```
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
chmod 600 ~/.ssh/id_rsa.pub
chmod 600 /etc/rsyncd.secrets 
```

## 其他

虽然配置了密钥认证，但是第一次登录还是需要输入密码的

{% include links.html %}
