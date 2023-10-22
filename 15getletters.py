word = 'brontosaurus'
dic = dict()
for l in word:
    dic[l] = dic.get(l, 0) + 1
print(dic)