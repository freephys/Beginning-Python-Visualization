# read an INI (config) file
import ConfigParser
read_opts=ConfigParser.ConfigParser()
read_opts.read('../data/options.ini')

# print parameters and values
for section in read_opts.sections():
    print "[%s]" % section
    for param in read_opts.items(section):
        print param
