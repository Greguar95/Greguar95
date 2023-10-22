fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('Invalid input')
    exit()
dd = dict()
for line in fhand:
    if line.startswith('From '):
        line = line.rstrip()
        #print(line)
        words = line.split()
        day = words[1]
        # print(day)
        dd[day] = dd.get(day, 0) + 1
print(dd)