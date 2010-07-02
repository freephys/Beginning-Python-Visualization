import tarfile, os, filecmp

os.chdir('../data')
if not os.path.exists('new1'):
    os.mkdir('new1')
if not os.path.exists('new2/new3'):
    os.makedirs('new2/new3')

tf = tarfile.open('files.tar.bz2', 'r:bz2')
tf.extractall('new1')
tf.extractall('new2')
tf.extractall('new2/new3')
tf.close()

cmp = filecmp.dircmp('new1', 'new2')
cmp.report()

os.chdir('../src')