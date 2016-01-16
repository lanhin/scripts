#!/bin/bash
#
# @2016-01  by lanhin
#
# Thanks to hch@mail.ustc.edu.cn
#
# Usage: ./batchrun.sh  num1  num2  command
# Which num1 is the start node index while num2 is the end.
# If command is a long one with options, you should use "" to declare it.
#

if [ $# -ne 3 ]; then
    echo "Usage: ./batchrun.sh  num1  num2  command"
    echo "Which num1 is the start node index while num2 is the end."
fi

for i in `seq $1 $2`
do
 ssh node$i $3;
done
