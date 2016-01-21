#!/bin/bash
#
# @2016-01  by lanhin
#
# Update files' access and modified time.
#
# TIMEFILE example:
# hello.c 2014-01-12 14:34:22
# (Note: a newline char required at end!)
#

if [ $# -ne 1 ]; then
    echo "Usage: ./update-file-time.sh timefile"
    exit 1
fi

TIMEFILE=$1

if [ -f $TIMEFILE ]; then
    while read LINE
    do
	FILENAME=`echo $LINE | awk '{print $1}'`
	TIME=`echo $LINE | awk '{print $2, $3}'`
	touch -d "$TIME" $FILENAME
#	echo $LINE
    done < $TIMEFILE
else
    echo "$TIMEFILE is not a normal file or doesn't exist."
    exit 1
fi
