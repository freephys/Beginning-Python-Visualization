from os.path import getsize

def tail_large(filename, n=10):
    """Returns the last n lines of a very large file."""

    N, data = 1024, ''

    # open the file and retrieve its size
    f = open(filename, 'rb')
    fsize = getsize(filename)

    # seek to the end of file
    f.seek(0, 2)

    for i in xrange(fsize-N, -N, -N):
        # read the next chunk of data
        last_loc = f.tell()
        f.seek(max(i, 0))
        
        # store read data, reversed order
        data += f.read(last_loc-f.tell())

        # do we have enough lines?
        if data.count('\n') > n:
            break

    # print the last n lines
    lines = data.splitlines()
    for line in lines[-n:]:
        print line
