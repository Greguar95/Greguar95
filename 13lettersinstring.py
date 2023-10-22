word = 'brontosaurus'
d = dict()
for l in word:
    if l not in d:
        d[l] = 1
    else:
        d[l] = d[l] + 1
print(d)