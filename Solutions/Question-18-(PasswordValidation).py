import string

correctpasswords = []
passwords = input('Type one or more password separated with comma: ').split(',')


for password in passwords:

    islower = isupper = isdigit = ischaracter = False

    if 6 <= len(password) <= 12:
        for symbol in password:
            if symbol in string.ascii_lowercase:
                islower = True
            elif symbol in string.ascii_uppercase:
                isupper = True
            elif symbol in string.digits:
                isdigit = True
            elif symbol in ['$', '#', '@']:
                ischaracter = True

        if islower and isupper and isdigit and ischaracter:
            correctpasswords.append(password)


print(','.join(correctpasswords))


