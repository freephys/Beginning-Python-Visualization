from pylab import *
from scipy import signal

# parameters controlling the signal
n = 100
t = arange(n)
y = zeros(n)
num_pulses = 3
pw = 11
amp = 20

for i in range(num_pulses):
    loc = floor(rand()*(n-pw+1))
    y[loc:loc+pw] = signal.triang(pw)*amp

# add some noise
y += randn(n)

figure()
title('Simple signal detection in noise')
hold(True)
xlabel('t')
ylabel('y')
plot(t, y)

# detect signals
thr = amp/2
I = find(y > thr)

# plot signal with noise plus detection
plot(t, y, 'b', label='signal with noise')
plot(t[I], y[I], 'ro', label='detections')
plot([0, n], [thr, thr], 'g--')

# annotate the threshold
text(2, thr+.2, 'Threshold', va='bottom')
legend(loc='best')

# peak detections
J = find(diff(I) > 1)
for K in split(I, J+1):
    ytag = y[K]
    peak = find(ytag == max(ytag))
    plot(peak+K[0], ytag[peak], 'sg', ms=7)

show()