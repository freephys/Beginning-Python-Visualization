from random import random
from pylab import *

N   = 40000 # number of events

# generate N events of friends times
friend1, friend2 = [], []
for i in range(N):
    friend1.append(random())
    friend2.append(random())

# find all occurrences of friends meeting    
met = array([(x, y) for (x, y) in zip(friend1, friend2) if abs(y-x) < 1.0/6])
not_met = array([(x, y) for (x, y) in zip(friend1, friend2) if abs(y-x) >= 1.0/6])

# plot the result, this might shed some light on the problem!
plot(met[:, 0], met[:, 1],'+m')
plot(not_met[:, 0], not_met[:, 1],'og')
title("Probability of meeting: %1.3f" % (float(len(met))/N))
xlabel('Time of arrival of Friend 1')
ylabel('Time of arrival of Friend 2')
axis('scaled')
show()
