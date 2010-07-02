# a script to plot GDP pie chart
from pylab import *

# initialize variables, N is the number of countries
N = 10

execfile('read_world_data.py')
gdp, tags = read_world_data(N)

# plot the bar chart
pie(gdp, labels=tags, shadow=True)
title('GDP rank, data from CIA World Factbook')

show()