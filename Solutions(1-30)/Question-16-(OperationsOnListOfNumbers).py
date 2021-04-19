numbers = input('Type comma separated numbers: ').split(',')
values = []

for number in numbers:
    if int(number) % 2 != 0:
        values.append(str(int(number) * int(number)))

# Druga metoda
# values = [str(int(number)*int(number)) for number in numbers if int(number) % 2 != 0]

print(','.join(values))



