import fileinput, sys

# string to search is the first argument
for line in fileinput.input(sys.argv[2:]):
    if line.find(sys.argv[1]) != -1:
        print "File %s, #%d: %s" % (fileinput.filename(),  
            fileinput.filelineno(), line.rstrip())
