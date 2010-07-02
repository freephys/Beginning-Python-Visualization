import random, time, array

N = 10
fname = '../data/binary_data.f64'
data = array.array('d')

# create data
for value in range(N):
    time.sleep(random.random())
    data.append(time.time())
    data.append(value)

# store data to file
f = open(fname, 'wb')
data.tofile(f)
f.close()

