def odd(s):
    """A generator function to iterate through odd elements of s"""
    i = 0
    while(i < len(s)):
        yield s[i]
        i+=2

def odd2(s):
    for elem in s[::2]:
        yield elem
    
def odd3(s):
    for elem in xrange(0, len(s), 2):
        yield s[elem]