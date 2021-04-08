sentence = input('Type a sentence: ')
lower = 0
upper = 0


for letter in sentence:
    if letter.islower():
        lower += 1
    elif letter.isupper():
        upper += 1

print('UPPER CASE', upper, 'LOWER CASE: ', lower)
