#!/bin/bash

VERBOSE=N
start=2
end=4

n=$# #number of parameters, the last parameter should be the target directory
if [ $VERBOSE = Y ]; then
    echo "Number of args: $n"
fi

# Split args into $filesList and $targetDir
i=0
for arg  in $*
do
    i=`expr $i + 1`
    if [ $VERBOSE = Y ]; then
	echo "i: $i    arg: $arg"
    fi
    if [ $i -ge $n ]; then
	targetDir="$arg"
    else
	filesList=$filesList" $arg"
    fi
done

if [ $VERBOSE = Y ]; then
    echo "filesList: $filesList"
    echo "targetDir: $targetDir"
fi

# Copy files to target nodes.
for i in `seq $start $end` #set the begin and end points as needed
do
    echo -e "\n    [Info]: copy files to node$i..."
    ssh node$i "[ -d $targetDir ] || mkdir -p $targetDir"
    if [ $? -ne 0 ]; then
	echo "[Error]: on node$i, no target dir and can't build one."
    else
	scp -r $filesList node$i:$targetDir
    fi
done
