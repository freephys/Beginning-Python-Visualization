from pylab import *

x = arange(10)
y = x**2
plot(x, y)
ars = [(x0, y0, dx, dy) for (x0, y0, dx, dy) in zip(x, y, diff(x), diff(y))]
cur_axes = gca()
for x0, y0, dx, dy in ars:
    cur_axes.add_patch(Arrow(x0, y0, dx, dy))
title('Arrows!')
show()
