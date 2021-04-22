s = input()
digit = letter = 0

for char in s:
    if char.isdigit():
        digit += 1
    elif char.isalpha():
        letter += 1

print('Digit -', digit)
print('Letter -', letter)
