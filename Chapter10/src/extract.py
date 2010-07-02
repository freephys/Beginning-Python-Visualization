import tarfile, os

os.chdir('../data')

if not os.path.exists('new'):
    os.mkdir('new')

tf = tarfile.open('files.tar.bz2', 'r:bz2')
tf.extractall('new')
tf.close()

os.chdir('../src')