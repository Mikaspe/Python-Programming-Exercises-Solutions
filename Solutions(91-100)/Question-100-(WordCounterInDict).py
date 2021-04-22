n = int(input('n: '))
dic = {}
ls = []
for i in range(n):
    word = input()
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1
        ls.append(word)

print(len(ls))
for word in ls:
    print(dic[word], end=' ')
