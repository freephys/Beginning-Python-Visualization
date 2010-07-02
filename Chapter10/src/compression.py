import tarfile, glob

import os
os.chdir('../data')

# create some files
for i in range(5):
    f = open('file%d.txt' % i, 'w')
    # write some data
    for j in range(100):
        f.write('Some data: %d\n' % j)
    f.close()

# archive the files using bz2 compression
tf = tarfile.open('files.tar.bz2', 'w:bz2')
for filename in glob.glob('file*'):
    tf.add(filename)
tf.close()

os.chdir('../src')