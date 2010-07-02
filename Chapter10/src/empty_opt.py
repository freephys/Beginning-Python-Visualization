from optparse import OptionParser
from sys import exit

usage = "Usage: python empty_opt.py [options] filename"

# create an OptionParser instance
parser = OptionParser(usage)

# these are the options
parser.add_option("-n", "--numbytes", dest="nbytes",
    type = "int", default=1000, help="number of bytes in file")
parser.add_option("-x", "--ext", dest="ext", 
    action="store_true", default=False, help="adds 'bin' extension to filename")
(opt, args) = parser.parse_args()

# must have a filename
if len(args) != 1:
    print "Improper number of arguments."
    exit()

# append extension if switch is on    
filename = args[0]+'.bin' if opt.ext else args[0]

# create the file
try:
    f = open(filename, 'wb')
except IOError:
    print "Unable to create file", filename
    exit()

f.seek(opt.nbytes-1)
f.write(chr(0))
f.close()

print "Successfully created file %s of size %d." % (filename, opt.nbytes)
