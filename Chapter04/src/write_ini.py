# creating an INI (config) file
import ConfigParser
options = ConfigParser.ConfigParser()
options.add_section('User Options')
options.set('User Options', 'all_data', True)
options.set('User Options', 'graph', 1)
options.add_section('Plot')
options.set('Plot', 'grid', True)
f = open('../data/options.ini', 'w')
options.write(f)
f.close()