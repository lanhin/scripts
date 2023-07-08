#!/bin/bash
#
# @2023-06  by lanhin
#
# Check IP address periodly
# and update index.html according
#
# Usage: ./index_update.sh &
#

myhome="/home/yinan"
orgIPfile="ip.txt"
ipkeywd="wlp3s0"
orgip="0.0.0.0"
indexfile="$myhome/index.html"
remoteindfile="nginx/html/"
sleept=0
backupdir="$myhome/backs/"

backupFunc(){ #tarfile name, dir to backup
    tarfilename=$1
    dirtoback=$2
    gzfilename="$tarfilename.gz"
    if [ -e $gzfilename ]; then
        rm $gzfilename
    fi
    if [ -e $tarfilename ]; then
        rm $tarfilename
    fi

    echo $tarfilename
    echo $dirtoback
    tar -cf $tarfilename $dirtoback
    while [ $? -ne 0 ]; do
        rm $tarfilename
        sleep 60
        tar -cf $tarfilename $dirtoback
    done
    tar -czf $gzfilename $tarfilename
    rm $tarfilename
    mv $gzfilename $backupdir
}

while true; do
    # 0. Backup files: $myhome/gitlab and $myhome/jupyter_docker
    if [ $sleept -ge 259200 ]; then
        sleept=`expr ${sleept} - 259200`
        echo "Start file backup at `date`, ${sleept}"

        tag=`date "+%y%m%d_%H%M"`
        tarfilename="git$tag.tar"
        backupFunc $tarfilename $myhome/gitlab/

        tarfilename="jupyter$tag.tar"
        backupFunc $tarfilename $myhome/jupyter_docker/
    fi

    # 1. Get IP address
    ip=`ifconfig ${ipkeywd} | grep broadcast | awk '{print $2}' | cut -f1 -d'/'`

    echo -e "ip=${ip}\n"
    # 2. Check if it changed
    if [ -e $orgIPfile ]; then
        orgip=`head -1 ${orgIPfile}`
        if [ "$orgip" == "$ip" ]; then
            echo -e "Not changed, skip at `date`...\n"
            sleep 36000
            sleept=`expr ${sleept} + 36000`
            continue
        fi
    fi
    # orgip != ip
    echo ${ip} > ${orgIPfile}
    echo `date` >> ${orgIPfile}

    # 3. Update IP file
    su -c "scp ${orgIPfile} vp:${remoteindfile}" yinan
    echo -e "Updated at `date`"

    # sleep 10h
    sleep 36000
    sleept=`expr ${sleept} + 36000`
done
