from time import localtime
# a script to create unique filenames based on title, 
# date and time stamp and an extension
datetime_stamp  = '%4d-%02d-%02dT%02d-%02d-%02d' % localtime()[:6]
title = 'SysALogs'
ext = 'csv'
print 'Unique filename: %s-%s.%s' % (title, datetime_stamp, ext)