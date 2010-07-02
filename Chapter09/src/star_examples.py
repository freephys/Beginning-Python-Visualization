# show some star examples
from pylab import *

# ensure the star patch is defined properly
execfile('star_patch.py')

examples=[ 
    "star(10, 0, 0, 'k')", 
    "star(10, 0, 0, 'k', 10)", 
    "star(10, 0, 0, 'k', 5, 0.2)", 
    "star(10, 0, 0, 'k', 3, 0.9)" ]
    
for i, example in enumerate(examples):
    subplot(2, 2, i+1)
    exec "new_star="+example
    gca().add_patch(new_star)
    title(example)
    axis('scaled')
    axis([-10, 10, -10, 10])

show()