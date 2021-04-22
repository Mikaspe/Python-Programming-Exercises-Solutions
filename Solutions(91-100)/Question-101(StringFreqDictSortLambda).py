s = input()

dct = {}

for letter in s:
    dct[letter] = dct.get(letter, 0) + 1

ans = sorted(dct.items(), key=lambda item: item[1], reverse=True)

for item in ans:
    print(item[0], item[1])
