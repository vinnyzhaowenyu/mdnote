---
title: Centos7 Jekyll Dockerfile 
keywords: sample homepage
tags: [getting_started]
sidebar: note_sidebar
permalink: note_jekyll_theme_centos_dockerfile.html
summary:  
---

## 新版本 v2.3

centos7版本

```
FROM  docker.io/centos

MAINTAINER from admin@zhaowenyu

ENV PS1   '\n\e[1;37m[\e[m\e[1;32m\u\e[m\e[1;33m@\e[m\e[1;35m\H\e[m \e[4m`pwd`\e[m\e[1;37m]\e[m\e[1;36m\e[m\n\$'
ENV LANG  'en_US.UTF-8'

#install comm software
RUN rm -f /etc/yum.repos.d/*
RUN curl -o /etc/yum.repos.d/Aliyun-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo 
RUN curl --silent --location https://rpm.nodesource.com/setup | bash -
RUN rpm -Uvh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm
RUN yum clean all && yum -y install  wget unzip make gcc libgcc gcc-c++ openssl-devel git which nodejs nginx

RUN cd /tmp/ && wget https://ruby.taobao.org/mirrors/ruby/ruby-2.3.0.tar.gz && tar xf ruby-2.3.0.tar.gz && cd ruby-2.3.0 && ./configure && make && make install
 
#config gem source
RUN gem sources --add http://gems.ruby-china.org/ --remove https://rubygems.org/  && gem sources -l
RUN gem update --system 
RUN gem install bundler jekyll 

RUN cd / && git clone https://github.com/vinnyzhaowenyu/mdnote && cd /mdnote &&  bundle update 

RUN echo 'server {'                           >/etc/nginx/conf.d/default.conf  \
 && echo '    listen 80 default_server;'      >>/etc/nginx/conf.d/default.conf \
 && echo '    listen [::]:80 default_server;' >>/etc/nginx/conf.d/default.conf \
 && echo '    location / {'                   >>/etc/nginx/conf.d/default.conf \
 && echo '        root /mdnote/_site;'        >>/etc/nginx/conf.d/default.conf \
 && echo '    }'                              >>/etc/nginx/conf.d/default.conf \
 && echo '}'                                  >>/etc/nginx/conf.d/default.conf 

RUN echo '#!/bin/bash'                                                         >  /tmp/run.sh && \
    echo 'nginx &'                                                             >> /tmp/run.sh && \
    echo 'touch /tmp/jekyll.log'                                               >> /tmp/run.sh && \
    echo 'while true'                                                          >> /tmp/run.sh && \
    echo 'do'                                                                  >> /tmp/run.sh && \
    echo '    cd /mdnote && git pull'                                          >> /tmp/run.sh && \
    echo '    date >> /tmp/jekyll.log'                                         >> /tmp/run.sh && \
    echo '    JEKYLL=`ps aux|grep "jekyll build"|grep -v grep|wc -l`'          >> /tmp/run.sh && \
    echo '    if [ $JEKYLL -gt 0 ];then'                                       >> /tmp/run.sh && \
    echo '        sleep 10'                                                    >> /tmp/run.sh && \
    echo '    fi '                                                             >> /tmp/run.sh && \
    echo '    cd /mdnote && bundle exec jekyll build >> /tmp/jekyll.log'       >> /tmp/run.sh && \
    echo '    sleep 10'                                                        >> /tmp/run.sh && \
    echo 'done'                                                                >> /tmp/run.sh
EXPOSE 80
RUN chmod +x /tmp/run.sh
CMD ["/bin/bash /tmp/run.sh"]
```

## 老版本

```
FROM  docker.io/centos:7.2.1511 

MAINTAINER from www.zhaowenyu.com

VOLUME /data

ADD etc/    /etc/
ADD root/   /root/
ADD data/   /data/

ENV PS1   '\n\e[1;37m[\e[m\e[1;32m\u\e[m\e[1;33m@\e[m\e[1;35m\H\e[m \e[4m`pwd`\e[m\e[1;37m]\e[m\e[1;36m\e[m\n\$'
ENV LANG  'en_US.UTF-8'
ENV PATH   /usr/local/rvm/bin:/usr/local/rvm/rubies/ruby-2.3.0/bin:$PATH

#config yum source in /etc/yum.repos.d/
RUN ls -l /etc/yum.repos.d/ &&  yum clean all 
RUN yum -y install  wget unzip which patch  libyaml-devel  autoconf  gcc-c++  readline-devel  zlib-devel  libffi-d  evel  openssl-devel automake libtool  bison sqlite-devel make gcc libgcc libffi-devel

#install rvm to update ruby 2.3.0
RUN curl -sSL https://rvm.io/mpapis.asc | gpg2 --import -
RUN curl -L get.rvm.io |bash -s stable
RUN mkdir -p ~/.rvm/user/ && echo "ruby_url=https://cache.ruby-china.org/pub/ruby" > ~/.rvm/user/db
RUN /usr/local/rvm/bin/rvm   install 2.3.0

#config gem source
RUN gem sources --add http://gems.ruby-china.org/ --remove https://rubygems.org/ 
RUN gem update --system && gem install json_pure bundler jekyll i18n 

WORKDIR /data/
#RUN wget https://github.com/tomjohnson1492/documentation-theme-jekyll/archive/gh-pages.zip && unzip gh-pages.zip
WORKDIR /data/documentation-theme-jekyll-gh-pages/
RUN  bundle update 
RUN  bundle install

#install nodejs
RUN curl --silent --location https://rpm.nodesource.com/setup | bash -
RUN yum -y install nodejs

RUN rpm -ivh http://nginx.org/packages/centos/6/noarch/RPMS/nginx-release-centos-6-0.el6.ngx.noarch.rpm
RUN yum clean all
RUN yum -y install nginx

#Gemfile source change
EXPOSE 80 

CMD ["/data/run.sh"]

```


```
FROM  docker.io/centos:7.2.1511 

MAINTAINER from www.zhaowenyu.com

VOLUME /data

ADD etc/    /etc/
ADD root/   /root/
ADD data/   /data/

ENV PS1   '\n\e[1;37m[\e[m\e[1;32m\u\e[m\e[1;33m@\e[m\e[1;35m\H\e[m \e[4m`pwd`\e[m\e[1;37m]\e[m\e[1;36m\e[m\n\$'
ENV LANG  'en_US.UTF-8'
ENV PATH   /usr/local/rvm/bin:/usr/local/rvm/rubies/ruby-2.3.0/bin:$PATH



#config yum source in /etc/yum.repos.d/
#RUN rm -f /etc/yum.repos.d/CentOS-*
RUN ls -l /etc/yum.repos.d/ &&  yum clean all 
RUN yum -y install  wget unzip which patch  libyaml-devel  autoconf  gcc-c++  readline-devel  zlib-devel  libffi-d  evel  openssl-devel automake libtool  bison sqlite-devel make gcc libgcc libffi-devel

#install rvm to update ruby 2.3.0
RUN curl -sSL https://rvm.io/mpapis.asc | gpg2 --import -
RUN curl -L get.rvm.io |bash -s stable
RUN mkdir -p ~/.rvm/user/ && echo "ruby_url=https://cache.ruby-china.org/pub/ruby" > ~/.rvm/user/db
RUN /usr/local/rvm/bin/rvm   install 2.3.0


#config gem source
RUN gem sources --add http://gems.ruby-china.org/ --remove https://rubygems.org/ 
RUN gem update --system && gem install json_pure bundler jekyll i18n 

WORKDIR /data/
#RUN wget https://github.com/tomjohnson1492/documentation-theme-jekyll/archive/gh-pages.zip && unzip gh-pages.zip
WORKDIR /data/documentation-theme-jekyll-gh-pages/
RUN  bundle update 
RUN  bundle install

#install nodejs
RUN curl --silent --location https://rpm.nodesource.com/setup | bash -
RUN yum -y install nodejs

RUN rpm -ivh http://nginx.org/packages/centos/6/noarch/RPMS/nginx-release-centos-6-0.el6.ngx.noarch.rpm
RUN yum -y install nginx

RUN useradd admin && chown admin:admin /data -R  && su - admin 
EXPOSE 80 
#bundle exec jekyll serve        

CMD ["/data/aa.sh"]

```
