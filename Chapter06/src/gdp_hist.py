# a script to plot GDP histogram
from pylab import *

# initialize variables; N is the number of countries, B is the bin size
N, B = 50, 1000

execfile('read_world_data.py')
gdp, labels = read_world_data(N)

# plot the histogram
prob, bins, patches = hist(gdp, arange(0, max(gdp)+B,B), align='center')

# annotate with text
for i, p in enumerate(prob):
    percent = int(float(p)/N*100)
    # only annotate non-zero values
    if percent:
        text(bins[i], p, str(percent)+'%', 
            rotation=45, va='bottom', ha='center')
ylabel('Number of countries')
xlabel('Income, billions of dollars')
title('GDP histogram, %d largest economies' % N)

# some axis manipulations
xlim(-B/2, xlim()[1]-B/2)

show()

