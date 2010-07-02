# a script to create unique filenames using a running index
from os.path import exists

index_stamp = 1
max_index   = 999   # maximum number of files
title       = '../data/SysALogs'
ext         = 'txt'

while index_stamp<max_index:
    unique_filename='%s-%03d.%s' % (title, index_stamp, ext)
    if exists(unique_filename):
        index_stamp += 1
        continue
    f=open(unique_filename, 'wt')
    f.write("Data")
    f.close()
    break

# report status
if index_stamp >= max_index:
    print "Could not create a unique filename"
else:
    print "Created unique file: ", unique_filename
