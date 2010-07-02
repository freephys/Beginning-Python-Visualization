import difflib

content = """A string
123, 456
789
some text\n"""
fname1 = '../data/file1.txt'
fname2 = '../data/file2.txt'

f1 = open(fname1, 'wb')
f1.write('before\n')
f1.write(content)
f1.close()

f2 = open(fname2, 'wb')
f2.write(content)
f2.write('after\n')
f2.close()
lines1 = open(fname1).readlines()
lines2 = open(fname2).readlines()
for line in difflib.context_diff(lines1, lines2, fname1, fname2):
    print line,

