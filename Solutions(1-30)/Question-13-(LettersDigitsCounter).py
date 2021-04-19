LettersCounter = 0
DigitsCounter = 0
sentence = input('Type a sentence: ')

for letter in sentence:
    if letter.isalpha():
        LettersCounter += 1
    elif letter.isdigit():
        DigitsCounter += 1

print('LETTERS:', LettersCounter, 'DIGITS:', DigitsCounter)
