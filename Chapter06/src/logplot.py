from pylab import *

I = 2*logspace(1,5,5)
semilogx(I, [20, 19, 8, 2, 2], '+-')
grid()
title('Logarithmic plot, semilogx()')
xlabel('Frequency [Hz]')
ylabel('Amplitude [dB]')
show()