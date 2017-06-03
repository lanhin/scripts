# Scripts Collection

## What?

| File Name | Description | Example |
| ------ | ------ | ------ |
| batchrun.sh | Run a command in a batch of nodes. | ./batchrun.sh 1 4 ls |
| copy2all.sh | Copy a list of files/directories into all nodes(from node1 to node10). | ./copy2all.sh yarn-site.xml mapred-site.xml `pwd` |
| delimiter_replace.py | Replace delimiter in a file. | python2 delimiter_replace.py '\t' ' ' syn.data |
| mat2csv.py | Generate csv file from matrix format. | python2 mat2csv.py mat.data |
| q2a.py | Transform fastq format into fasta format. | python2 q2a.py sample.fq |
| un2fq.py | Transform seq format into fastq format. | python2 un2fq.py sample0.seq |
| update-file-time.sh | Update files' access and modified time. | ./update-file-time.sh timefile |


## How?

All(at least most) of the scripts has useage information. Just type ```./filename``` and check the info.

## TODO

1. Usage for ```copy2all.sh```
2. Data file templates (under dir ```datafiles```)