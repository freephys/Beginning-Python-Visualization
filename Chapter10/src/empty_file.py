from sys import argv, exit

usage = "Usage: python empty_file.py nbytes filename"

# we expect three arguments: script name, size and file name
if len(argv) != 3:
    print "Improper number of arguments."
    print usage
    exit()

# is size an integer?
try:
    nbytes = long(argv[1])
except ValueError:
    print "First argument is not an integer number."
    print usage
    exit()

# retrieve the requested file name
filename = argv[2]

# can we create the file?
# here a failure could be due to a non-existing path
try:
    f = open(filename, 'wb')
except IOError:
    print "Unable to create file", filename
    print usage
    exit()

# finally! create the file
f.seek(nbytes-1)
f.write(chr(0))
f.close()
print "Successfully created file %s of size %d." % (filename, nbytes)
