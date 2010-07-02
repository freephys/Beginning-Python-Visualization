from pylab import *

theta = arange(0, 2*pi, 0.01)
polar(theta, cos(theta), theta, -cos(theta))
rgrids([0.5, 1.0], ['Half', 'Full'])
theta_labels = ['0', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3*\pi}{2}$']
thetagrids(arange(0, 360, 90), theta_labels)
title(r'A polar plot of $\pm cos(\theta)$')

show()