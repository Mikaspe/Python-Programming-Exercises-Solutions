letters = input('letters: ')

d = dict.fromkeys(letters, 0)

for letter in letters:
        d[letter] += 1

print(d)

