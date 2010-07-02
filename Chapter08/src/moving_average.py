from pylab import *
from scipy import signal

N = 512
t = linspace(0, 10, N)
x = 1-exp(-t) +randn(N)/10

W = 32  # num points in moving average

# the slow method
xf = zeros(len(x)-W+1)
for i in range(len(x)-W+1):
    xf[i] = mean(x[i:i+W])

# the fast method (and the one we plot)
xf2 = signal.lfilter(ones(W)/ W, 1, x)

figure()
hold(True)
plot(t, x)
plot(t, xf2, lw=3)
title('Moving average')
xlabel('t [seconds]')
ylabel('x []')
legend(['signal with noise', 'filtered signal'])
show()
