from pylab import *

N = [4, 8, 16, 64]
for i, n in enumerate(N):
    subplot(2, 2, i+1)
    stem(arange(n), hamming(n))
    xticks(arange(0,n+1, n/4))
    yticks([0, 0.5, 1])
    xlim(-0.5, n+0.5)
    legend(['N = %d' % n])

show()