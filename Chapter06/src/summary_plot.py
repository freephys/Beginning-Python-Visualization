from pylab import *

I = arange(0, 2*pi+0.1, 0.1)
plot(I, sin(I), label='sin(I)')
title('Function y = sin(x)')
xlabel('x [rad]')
ylabel('Function y = sin(x)')
text(pi/2, 1, 'Max value', ha='center', va='bottom')
text(3*pi/2, -1, 'Min value', ha='center', va='top')
xticks(arange(0, 2*pi, pi/2), \
    ('0', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$'))
xlim([0, 2*pi])
ylim([-1.2, 1.2])
grid()
show()
