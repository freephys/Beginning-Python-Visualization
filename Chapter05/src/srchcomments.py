def srchcomments(filename, substr):
    """Searches inside Python source comments."""
    for index, line in enumerate(open(filename, 'rt')):
        L = line.split('#')
        if len(L) == 2:
            if L[1].find(substr) != -1:
                print "%5d: %s" % (index, line.rstrip())
