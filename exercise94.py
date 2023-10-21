fname = input('Enter file:')
try:
    fhand = open(fname)
except:
    fname = "mbox-short.txt"
    fhand = open(fname)
dc = dict()
for line in fhand:
    if line.startswith('From '):
        line = line.rstrip()
        words = line.split()
        eml = words[1]
        dc[eml] = dc.get(eml, 0) + 1
maxeml = None
maxcnt = None

    if maxcnt is None or cnt > maxcnt:
        maxeml = eml
        maxcnt = cnt
print(maxeml, maxcnt)
# New New Stuff