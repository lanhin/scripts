#/usr/bin/env python
'''
@2016-01  by lanhin

Transform fastq format into fasta format.
Usage: python2 q2a.py fastqFileName.fq

Fastq format:
    @readid/direction
    sequence line
    +
    quality line

Fasta format:
    >readid/direction
    sequence line
'''
import sys
import os

if (len(sys.argv)) != 2:
    print "Usage: python2 q2a.py <fastq_file_name>"
    exit(1)

fqfilename=sys.argv[1]
fafilename=fqfilename + '.fa'

print "Transforming",fqfilename,"\nOutput file:", fafilename

if os.path.isfile(fafilename):
    os.remove(fafilename)
linenum = 0
with open (fafilename, 'w') as faOut:
    with open (fqfilename, 'r') as fqIn:
        for line in fqIn.readlines():
            if linenum == 0:
                line = line.replace('@', '>')
                #print line
                faOut.write(line)
            elif linenum == 1:
                faOut.write(line)
            linenum = ( linenum + 1 ) % 4
