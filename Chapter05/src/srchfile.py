# for the solution to the exercise
from math import ceil, log10

def srchfile(filename, substr):
    """Searches for a substring in a file."""
    for index, line in enumerate(open(filename,'rt')):
        if line.find(substr) != -1:
            print "%5d: %s" % (index, line.rstrip())

def srchfile_ex(filename, substr):
    """Searches for a substring in a file."""
    lines = open(filename).readlines()
    fmt = r'%' + str(int(log10(len(lines)))+1) + r'd: %s'
    for index, line in enumerate(lines):
        if line.find(substr) != -1:
            print fmt % (index, line.rstrip())
