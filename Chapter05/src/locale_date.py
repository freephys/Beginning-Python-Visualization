import locale
from time import strftime, strptime, localtime
from sys import platform
if platform == 'linux2':
    locale.setlocale(locale.LC_ALL, 'hebrew')
elif platform == 'win32':
    locale.setlocale(locale.LC_ALL, 'Hebrew_Israel')
elif platform == 'cygwin':
    raise Exception('Cygwin not supported')
else:
    print "Untested platform: ", sys.platform
today = strftime('%B %d, %Y', localtime())
todayU = unicode(today, 'cp1255')
open('../data/today.txt', 'w').write(todayU.encode('utf-16'))