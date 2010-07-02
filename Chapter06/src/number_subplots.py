from pylab import *

def number_subplots(fignum):
    """Numbers the subplots in a figure."""
    
    # switch to the requested figure
    figure(fignum)
    
    fig = gcf()
    
    for i, fig_axe in enumerate(getp(fig, 'axes')):
        fig_axe.set_title(str(i+1))
        
    axis()