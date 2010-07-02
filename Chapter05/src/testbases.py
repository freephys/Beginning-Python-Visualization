execfile('base_conversion.py')
def testbases():
    """Tests implementation of base conversion functions"""
    v0 = {'bin':'0', 'oct':'0', 'dec':'0', 'hex':'0x0'}
    v1 = {'bin':'1111', 'oct':'017', 'dec':'15', 'hex':'0xf'}

    
    for v in [v0, v1]:
        perms = [(a, b) for b in v for a in v if a != b]
        for (s1, s2) in perms:
            tc = "assert %s2%s(v['%s']) == v['%s']" % (s1, s2, s1, s2)
            exec tc            
