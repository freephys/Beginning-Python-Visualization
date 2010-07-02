def head_large(filename, n=10):
    """Returns the first n lines of a very large file."""
    for i, line in enumerate(open(filename)):
        print line.rstrip()
        if i == n-1: break
