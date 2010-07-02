# cmp_fy.py is a script file to test performance of different implementations
# locating duplicate files

import os, time

def get_all_files(srchpath):
    """Get the names of all the files in a folder, recursively, 
    including path, name and size."""
    allfiles = []

    for root, dirs, files in os.walk(srchpath):
        for file in files:
            pathname = os.path.join(root, file)
            filesize = os.path.getsize(pathname)
            allfiles.append([file, pathname, filesize])
    return allfiles

def find_dupes_1(thefiles):
    """Searches for file duplicates, method 1."""
    result1 = []
    mydict1 = dict()

    for filename, pathname, filesize in thefiles:
        if filename in mydict1:
            [dup_file, dup_size] = mydict1[filename]
            if dup_size == filesize:
                result1.append(pathname)
        else:
            mydict1[filename] = [pathname,filesize]
    return result1

def find_dupes_2(thefiles):
    """Searches for file duplicates, method 2."""
    result2 = []
    mydict2 = dict()

    for filename, pathname, filesize in thefiles:
        for k, v in mydict2.iteritems():
            if v[0] == filename and v[1] == filesize:
                result2.append(pathname)
        else:
            mydict2[pathname] = [filename, filesize]
    return result2

def find_dupes_3(thefiles):
    """Searches for file duplicates, method 3."""
    result3 = []
    mydict3 = dict()

    for filename, pathname, filesize in thefiles:
        if mydict3.get(filename):
            for [dup_file, dup_size] in mydict3[filename]:
                if dup_size == filesize:
                    result3.append(pathname)
            mydict3[filename].append([pathname, filesize])
        else:
            mydict3[filename] = [[pathname, filesize]]
    return result3

srchpath = 'c:/Python25'
from time import clock as clk
t = []
allfiles = get_all_files(srchpath)
t.append(clk()); res1 = find_dupes_1(allfiles); t.append(clk())
t.append(clk()); res2 = find_dupes_2(allfiles); t.append(clk())
t.append(clk()); res3 = find_dupes_3(allfiles); t.append(clk())
print "Number of files processed: ", len(allfiles)
print "method 1: %5.5f; method 2: %5.5f; method 3: %5.5f" % \
    (t[1]-t[0], t[3]-t[2], t[5]-t[4])

