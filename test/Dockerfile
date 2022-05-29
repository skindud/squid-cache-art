# encoding: UTF-8

FROM 	fedora:35

LABEL maintainer="Sergey Dudkin <biperdev@gmail.com>"
LABEL Description="SQUID test image" Version="0.0.1"

USER root # DL3002 warning: Last USER should not be root
# DL4006 warning, SC3037 warning
RUN	sed -i '/fedora-cisco-openh264-$releasever/i \#baseurl=http://codecs.fedoraproject.org/openh264/$releasever/$basearch/os/' /etc/yum.repos.d/fedora-cisco-openh264.repo && \
	sed -i 's%http://download.example/pub/fedora/%http://ftp.halifax.rwth-aachen.de/fedora/%g' $(grep -ril 'baseurl' /etc/yum.repos.d/) && \
	sed -i 's/#baseurl/baseurl/g' $(grep -ril 'baseurl' /etc/yum.repos.d/) && \
	sed -i 's/metalink/#metalink/g' $(grep -ril 'metalink' /etc/yum.repos.d/) && \
	echo -e 'deltarpm=false\nzchunk=false\nproxy=http://bro:3128' | tee -a /etc/dnf/dnf.conf && \
        time yum makecache && \
    	yum clean all && rm -rf /var/cache/yum
#	time yum --disablerepo=* --enablerepo=fedora  -y install htop && \


this check

#docker build -t fedora:35-squidtest -f Dockerfile.test . 
