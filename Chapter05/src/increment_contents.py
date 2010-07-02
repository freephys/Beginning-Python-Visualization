def increment_contents(filename):
    """Increments values in a file, creating a new file with extension 'inc'."""

    data = open(filename, 'rt').readlines()
    for i, line in enumerate(data):
        for word in line.split():
            try:
                data[i] = line.replace(word, str(int(word)+1))
            except ValueError:
                # uncomment the following if you'd like feedback
                # print word, "is not a number"
                pass
    open(filename+'.inc', 'wt').writelines(data)


def increment_contents_both(filename):
    """Increments values in a file, creating a new file with extension 'inc'.

Works with both ints and floats."""

    data = open(filename, 'rt').readlines()
    for i, line in enumerate(data):
        for word in line.split():
            try:
                data[i] = line.replace(word, str(int(word)+1))
            except ValueError:
                try:
                    data[i] = line.replace(word, str(float(word)+1))
                except ValueError:
                    # uncomment the following if you'd like feedback
                    # print word, "is not a number"
                    pass
    open(filename+'.inc', 'wt').writelines(data)

