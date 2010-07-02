import cPickle

fname = '../data/mysession.pickle'
fin = open(fname, 'rb')
var_index = 0

while True:
    try:
        var_index += 1
        exec "v_%d = cPickle.load(fin)" % var_index
        exec "var_type = type(v_%d)" % var_index
        print "Read v_%d, type is: %s" % (var_index, var_type)
    except EOFError:
        break
fin.close()

