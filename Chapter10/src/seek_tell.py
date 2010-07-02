import struct
from math import sqrt
from random import randrange

# binary filename
bin_fn = '../data/large_file.bin'

Nfields = 1000      # number of fields
N = 766             # field to retrieve
fmt = 'cdL'         # format: char, float, long

fmt_size = struct.calcsize(fmt)

# create a random binary file
fout = open(bin_fn, 'wb')
for i in xrange(Nfields):
    data = struct.pack(fmt, chr(randrange(32, 128)), sqrt(float(i)), i)
    fout.write(data)
fout.close()

# read the N-th value
fin = open(bin_fn, 'rb')
fin.seek((N-1)*fmt_size)
data = fin.read(fmt_size)
(c, d, l) = struct.unpack(fmt, data)
print "At location %d, I read:" % (fin.tell()/fmt_size), (c, d, l)

