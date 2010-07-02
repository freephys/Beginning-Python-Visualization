from pylab import *

def magic_arrow(x, y, top_right, n, c=0):
    """Draws an arrow from point x, y."""

    d, my_colors = 0.15, 'rbymg'

    if top_right:   # top-right arrow
        mc = my_colors[c % len(my_colors)]
        ar = Arrow(x+0.5+d, n-y-0.5+d, 1-2*d,1-2*d, width=0.2, fc=mc, ec=mc)
    else:           # down arrow
        ar = Arrow(x+0.5, n-y-0.5-d, 0, 2*d-1, width=0.2, fc='k', ec='k')
        
    # patch the arrow
    gca().add_patch(ar)


def show_alg(n=3):
    """Draws a magic square, n must be odd."""
    
    if n % 2 != 1:
        raise ValueError, "Magic(n) requires n to be odd."

    # prepare the figure, draw grid lines, hide ticks
    axis('scaled')
    axis([0, n, 0, n])
    for i in range(n):
        plot([0, n], [i, i], 'b')
        plot([i, i], [0, n], 'b')
    xticks([])
    yticks([])
    
    # alternating color index
    altc = 0
    
    # initialize variables
    m, row, col = zeros([n, n]), 0, n/2
    
    # go through all the numbers from 1 to n**2
    for num in xrange(1, n**2+1):
        
        # assign the current number and display it on the figure
        m[row, col] = num
        text(col+0.5, n-row-0.5, str(num), va='center', ha='center')
        
        # store current row and col
        pcol, prow = col, row
        
        # increment row and col
        col = (col+1) % n
        row = (row-1) % n
        
        # if location (col, row) is non-zero, it means the cell
        # is occupied, move down 
        if m[row, col]:
            col = pcol % n
            row = (prow+1) % n
            
        # if current location minus previous location is (1, 1)
        # draw a top-right arrow
        if col-pcol == 1 and prow-row == 1:
            magic_arrow(pcol, prow, True, n, altc)
            
        # if previous col location is identical to current
        # col location, draw a down arrow (unless it's the last cell)
        elif pcol == col and num != n**2:
            magic_arrow(pcol, prow, False, n)
            altc += 1
        
        # the following two elif sentences take care of drawing two
        # arrows in case of wrapping: one originating from the current
        # location, the other to the next location
        elif col-pcol == 1 and prow-row != 1:
            magic_arrow(pcol, prow, True, n, altc)
            magic_arrow(pcol, n, True, n, altc) 
        elif col-pcol != 1 and prow-row == 1:
            magic_arrow(pcol, prow, True, n, altc)
            magic_arrow(-1, prow, True, n, altc)

        # last cell
        elif num == n**2:
            pass
        
        # if we've reached this point, there's a bug
        else:
            raise ValueError, "We should never be here."

def show_some():
    figure()
    for i in range(4):
        subplot(2, 2, i+1)
        show_alg(2*i+3)
        title('N='+str(2*i+3))

show_some()
show()
