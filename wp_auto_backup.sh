#!/bin/bash
#
# @2018-05  by lanhin
#
# Backup wordpress directories periodly
# and copy packed file to a backup computer.
#
# Usage: ./wp_auto_backup.sh &
#

gzfilename="test"
while true; do
    if [ -e $gzfilename ]; then
	rm $gzfilename
    fi
    tag=`date "+%y%m%d_%H%M"`
    tarfilename="wp$tag.tar"
    gzfilename="$tarfilename.gz"
    tar -cf $tarfilename myWordpress
    while [ $? -ne 0 ]; do
	rm $tarfilename
	tar -cf $tarfilename myWordpress
    done
    tar -czf $gzfilename $tarfilename
    rm $tarfilename
    scp $gzfilename db2:/seg/DataBackup/wp/

    # sleep 72h
    sleep 259200
done
