def head(filename, n=10):
    """Prints the first n lines of the file."""
    for line in open(filename).readlines()[:n]: 
        print line.rstrip()

def tail(filename, n=10):
    """Returns the last n lines of the file."""
    for line in open(filename).readlines()[-n:]:
        print line.rstrip()
        