#/usr/bin/env python

'''
@2016-01  by lanhin

Usage: python2 mat2csv.py <matrix>
<matrix>:  the file stores the original matrix data.
The output file name is <matrix>.replace
'''
import sys
import os

if (len(sys.argv)) != 2:
    print "Usage: python2 mat2csv.py <matrix>"
    exit(1)

filein = sys.argv[1]
fileout = filein + '.csv'
rowidx = 0
colidx = 0
print "Input:",filein
if os.path.isfile(fileout):
    os.remove(fileout)
with open(filein, "rb") as source, open(fileout, "wb") as result:
    for line in source:
        for val in line.split(','):  # the default delimeter in matrix file is ','
            if ( val != "0" and val != "0.0" and val != "-0" and val != "-0.0" and val != ""):
                outline = str(rowidx)+","+str(colidx)+","+val
                if (outline[-1] != '\n'):
                    outline = outline + "\n"
                result.write(outline)
            colidx += 1
        colidx = 0
        rowidx += 1

