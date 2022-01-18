#!/bin/bash

docker run \
    --detach \
    --publish 3306:3306 \
    --name mysql \
    --restart always \
    --env MYSQL_DATABASE="parking" \
    --env MYSQL_USER="pk" \
    --env MYSQL_PASSWORD="1234" \
    --env MYSQL_ROOT_PASSWORD="123456" \
    --env TZ="Asia/Shanghai" \
    --volume /etc/localtime:/etc/localtime:ro \
    mysql \
    --character-set-server=utf8 \
    --collation-server=utf8_bin \
    --default_authentication_plugin="mysql_native_password"