# end of day report
from time import mktime, strptime, ctime
import csv

d = {}

for row in csv.reader(open('../data/SystemALogs.txt')):
    # t is a struct_time tuple
    t = strptime(row[0], '%a %b %d %H:%M:%S %Y')
    
    # calculate seconds since the epoch
    t_epoch = mktime(t)
    
    # construct a key and value
    key = (t.tm_year, t.tm_yday)
    val = (t_epoch, row[1])
    
    try:
        # do we have a more recent entry?
        if d[key][0] < t_epoch:
            d[key] = val
    except KeyError:
        # current date is not in dictionary
        d[key] = val
        
for epoch, line in d.itervalues():
    print ctime(epoch), line
