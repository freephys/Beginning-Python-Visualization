from numpy import *
from sys import getrecursionlimit

def flood_fill(x, y, m, total):
    """A function to flood fill an image (matrix)."""

    if total > getrecursionlimit():
        return total
        
    # nothing to fill
    if m[x, y] != 255:
        return total
        
    m[x, y] = 128
    if(x-1 >= 0): 
        total = flood_fill(x-1, y, m, total+1)
    if(x+1 <= m.shape[0]-1): 
        total = flood_fill(x+1, y, m, total+1)
    if(y-1 >= 0): 
        total = flood_fill(x, y-1, m, total+1)
    if(y+1 <= m.shape[1]-1): 
        total = flood_fill(x, y+1, m, total+1)
    return total+1
