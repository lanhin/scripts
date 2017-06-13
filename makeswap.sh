#!/bin/bash
#
# @2017-06  by lanhin
#
# Brief: Create a swap file and turn on it
# Usage: ./makeswap.sh <swapfilename> <bs> <count>
#
# TODO: Exception handle
#

# $1  swap file name
# $2  block size
# $3  count

if [ $# -ne 3 ]; then
    echo "Usage: ./makeswap.sh <string filename> <int bs> <int count>"
    exit 1
fi

swapfile=$1
blocksz=$2
blockct=$3

echo "Make swap file "$swapfile" with block size="$blocksz", count="$blockct

dd if=/dev/zero of=$swapfile bs=$blocksz count=$blockct

mkswap $swapfile

chmod 600 $swapfile

swapon $swapfile


echo -e "\nYou can add the following statements into your /etc/rc.local:"
echo "    swapon "$swapfile
echo -e "\nTo remove this swap, run:\n    swapoff "$swapfile
