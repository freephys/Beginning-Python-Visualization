import struct

filename = '../data/structs.bin'
format = 'Lff'

# values is a list of values in the form long, float, float; long, float, float
L = [[ 10L, 1.0, 2.0], [20L, 0.125, 0.25]]

# write the list of values to file
fout = open(filename, 'wb')
for row in L:
    data = struct.pack(format, row[0], row[1], row[2])
    fout.write(data)
fout.close()

struct_size = struct.calcsize(format)

# Method 1: read the binary file, a struct at a time
fin = open(filename, 'rb')
data = fin.read(struct_size)
while data:
    values = struct.unpack(format, data)
    print values
    data = fin.read(struct_size)
fin.close()
    
# Method 2: read the entire binary file at once
data = open(filename, "rb").read()
print struct.unpack(format*(len(data)/struct_size), data)

