# encoding: UTF-8

FROM       alpine:3.15.4
MAINTAINER Sergey Dudkin <biperdev@gmail.com>

RUN apk add --update squid python
RUN rm -rf /var/cache/apk/*

CMD /squid.py