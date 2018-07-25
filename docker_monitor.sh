#!/bin/bash
#
# @2018-05  by lanhin
#
# Monitor docker container running status on vps.
# If something isn't running, start it.
#
# Usage: Add this script into the /etc/crontab. An example entry:
# m h dom mon dow user  command
# */10 *  * * *   lh      cd /home/lh && ./docker_monitor.sh
#

#while true; do
    docker ps | grep mysql
    if [ $? -ne 0 ]; then
	echo "no mysql running, now start it..."
	docker start wp_mysql
    fi

    docker ps | grep lanhin
    if [ $? -ne 0 ]; then
	echo "no wordpress running, now start it..."
	docker start wp_lanhin
    fi

    docker ps | grep nginx
    if [ $? -ne 0 ]; then
	echo "no nginx running, now start it..."
	docker start nginx_lanhin
    fi

#    sleep 600
#done
