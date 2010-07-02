from pylab import *
from PIL import Image
from sys import getrecursionlimit

execfile('flood_fill.py')

# read the image
im = Image.open('../images/nightsky.png')

# split the image into individual bands
cols, rows = im.size
R, G, B, A = im.split()

# retrieve the data from the red band as a matrix array
data = array(R.getdata())

# set all values that are non-zero to 255
# (could be values due to antialiasing)
data[find(data != 0)] = 255
data=data.reshape(rows, cols)

# count the stars
count, recursion_limit_reached = 0, 0
for i in range(rows):
    for j in range(cols):
        tot = flood_fill(i, j, data, 0)
        if tot > getrecursionlimit():
            recursion_limit_reached += 1
        elif tot > 0:
            count+=1
            
if recursion_limit_reached:
    print "Recursion limit reached %d times" % recursion_limit_reached
print "I counted %d stars!" % count

R.putdata(data.reshape(cols*rows))
Image.merge('RGB', (R, G, B)).show()