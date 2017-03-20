#/usr/bin/env python
'''
@2016-01  by lanhin

Transform seq format into fastq format.
Usage: python2 un2fq.py  <unnormal_file_name>

Fastq format:
    @readid/direction
    sequence line
    +
    quality line

'''
import sys
import os

if (len(sys.argv)) != 2:
    print "Usage: python2 un2fq.py <unnormal_file_name>"
    exit(1)

unnormalfilename=sys.argv[1]
fqfilename=unnormalfilename + '.fq'

print "Transforming",unnormalfilename,"\nOutput file:", fqfilename

if os.path.isfile(fqfilename):
    os.remove(fqfilename)

with open (fqfilename, 'w') as fqOut:
    with open (unnormalfilename, 'r') as unIn:
        for line in unIn.readlines():
            #line = line.replace('\t', ' ')
            line = line.replace('\n', '')
            splited = line.split('\t')
            #different ops according to different number of fields
            outputLines = '@'+splited[0]+"/1\n"+splited[-1]+'\n'+"+\n"+splited[-1]+'\n'
            fqOut.write(outputLines)
#            print splited[0]
