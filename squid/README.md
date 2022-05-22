# Squid

## Description

It is a light docker squid image based on Alpine Linux 
Checked on alpine:3.15.4

## Build

docker build -t squid-cache-art:0.0.1 .
# podman build --tag squid-cache-art:0.0.1 -f ./Dockerfile

You can use https://hub.docker.com/r/b4tman/squid at the stage.

## ToDo

- https://github.com/scbunn/docker-squid/issues/5
- add acl rules to limit the access