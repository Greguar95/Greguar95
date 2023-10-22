fname = input('Enter file: ')
if len(fname) < 1: fname = 'clown.txt'
hndl = open(fname)

dic = dict()
for line in hndl:
    line = line.rstrip()
    words = line.split()
    #print(words)
    for w in words:       
        dic[w] = dic.get(w, 0) + 1
        # Retrieve, create, update counter in one line
# print(dic)
largest = -1
theword = None
for k, v in dic.items():
    # print(k, v)
    if v > largest:
        largest = v
        theword = k

print('Final:', theword, largest)