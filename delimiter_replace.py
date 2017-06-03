#/usr/bin/env python

'''
@2016-01  by lanhin

Usage: python2  delimiter_replace.py  <old_del>  <new_del>  <filename>
<old_del>:  the old delimiter used in <filename>
<new_del>:  the new delimiter to replace <old_del>
The output file name is <filename>.replace
'''

import sys
import os
import csv

if (len(sys.argv)) != 4:
    print "Usage: python2 delimiter_replace.py <old_del> <new_del> <filename>"
    exit(1)

old_del = sys.argv[1]
new_del = sys.argv[2]
filein = sys.argv[3]
fileout = filein + '.replace'
#TODO: check <old_del> and <new_del> here
#TODO: check if filein exists.

#print "delimiters:",csv.list_dialects()

print "Input:",filein
if (old_del == ' '): # In case there may be multiple spaces
    tmpfile = filein + '.tmp'
    if os.path.isfile(tmpfile):
        os.remove(tmpfile)
    with open(filein, "rb") as source, open(tmpfile, "wb") as middle:
        middle_out = csv.writer(middle, delimiter = old_del)
        for line in source:
            middle_out.writerow(line.split())
    filein = tmpfile
        
if os.path.isfile(fileout):
    os.remove(fileout)

print "Output:",fileout
with open(filein, "rb") as source, open(fileout, "wb") as result:
    in_txt = csv.reader(source, delimiter = old_del)
    out_csv = csv.writer(result, delimiter = new_del)

    out_csv.writerows(in_txt)

if (old_del == ' '):
    os.remove(tmpfile)
