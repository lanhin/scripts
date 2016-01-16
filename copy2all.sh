#!/bin/bash
#
# @2016-01  by lanhin
#
# Copy files(usually config files for applicaton)
# from one node(usually the master, node1)
# to other nodes(from node2 to node10).
#
# Usage: ./copy2all.sh file1 file2 file3 ... targetDir
#
# For example:
#   $ ./copy2all.sh yarn-site.xml mapred-site.xml `pwd`
#
#

VERBOSE=N
start=2   # The start index of target node.
end=10    # The end index of target node.

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
