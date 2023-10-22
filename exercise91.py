wordstxt = open('words.txt')
dic = dict()
for line in wordstxt:
    line = line.rstrip()
    words = line.split()
    # print(words)
    for w in words:
        dic[w] = dic.get(w)
#print(dic)
findword = input('Enter word: ')
print(findword, findword in dic)