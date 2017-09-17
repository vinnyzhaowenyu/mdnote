---
title: Docker Registry 搭建
keywords: docker 
last_updated: September 17, 2017
tags: [docker]
summary: Docker Rgistry V2 搭建 
sidebar: note_sidebar
permalink: note_docker_registry.html
folder: note 
---

## 安装Docker环境


请参考[note_docker_install.html]

## 下载Docker Registry V2 镜像

```
docker pull docker.io/registry
```

## 运行Docker Registry 服务

```
docker run -itd -p 5000:8000  --name registry docker.io/registry
``` 

## 上传镜像docker Registry中

```
docker tag docker.io/centos localhost:5000/centos:latest
docker push localhost:5000/centos:latest
```

## 镜像存储
默认会将镜像放置在Registry容器的这个目录中
```
/var/lib/registry
```
远程访问
到目前为止，docker registry 已经可以正常使用，且可以指定数据存储位置。但也只能在本地使用，要想在远程使用该 registry，就必须使用 TLS 来确保通信安全，就像使用 SSL 来配置 web 服务器。也可以强制 docker registry 运行在 insecure 模式，这种模式虽然配置起来要简单一些，但很不安全，一般不建议使用。
这里偷懒使用这个简单的 insecure 模式，假设你在一个域名为 test.docker.midea.registry.hub 的主机上运行 docker registry，步骤如下：
1，在你要远程访问 docker registry 的机器上，修改文件 /etc/default/docker 或 /etc/sysconfig/docker，具体是哪个取决于你的系统。

2，编辑里面的 DOCKER_OPTS 选项，如果没有这个选项字段，就添加一个。改成下面这样的：
```
ADD_REGISTRY='--add-registry test.docker.midea.registry.hub:5000'  
DOCKER_OPTS="--insecure-registry test.docker.midea.registry.hub:5000"  
INSECURE_REGISTRY='--insecure-registry test.docker.midea.registry.hub:5000'  
```

3.重启你的 docker 守护进程
通过以上3步，你的这个机器就能远程从 test.docker.midea.registry.hub 上运行的 docker registry 拉取镜像了：
```
$ docker pull test.docker.midea.registry.hub:5000/hello-world  
```
也可以省略 registry 的域名和端口（会先尝试从 test.docker.midea.registry.hub 中拉取，失败后再尝试从 docker.io 拉取）：
```
$ docker pull hello-world  
```
前提是你的机器要能访问主机 test.docker.midea.registry.hub，可以修改 /etc/hosts。


{% include links.html %}
