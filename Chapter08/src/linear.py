from pylab import *

# number of data points
N     = 100
start = 0
end   = 1

A = rand()
B = rand()

# our linear line will be y = A*x + B

x = linspace(start, end, N)
y = A*x + B
y += randn(N)/10

# linear regression
p = polyfit(x, y, 1)

figure()
title('Linear regression with polyfit()')
plot(x, y, 'o', 
    label='Measured data; A=%.2f, B=%.2f' % (A, B))
plot(x, polyval(p, x), '-', 
    label='Linear regression; A=%.2f, B=%.2f' % tuple(p))
legend(loc='best')

show()

