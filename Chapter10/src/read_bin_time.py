import random, time, array

N = 10
fname = '../data/binary_data.f64'
data = array.array('d')

# read data
f = open(fname, 'rb')
data.fromfile(f, N*2)
f.close()

# display data
L = data.tolist()
for t, val in zip(L[::2], L[1::2]):
    print time.ctime(t), val