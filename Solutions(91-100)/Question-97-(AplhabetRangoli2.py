# My second solution
from string import ascii_letters


def rangoli(n):
    width = 4*n - 3  # Number of symbols in one row
    final = []

    for i in range(n):
        right = '-'.join(ascii_letters[n-i-1 : n])
        middle = right[-1:0:-1] + right
        half = middle.center(width, '-')
        final.append(half)

    for i in range(n - 1):
        final.insert(n, final[i])

    for line in final:
        print(line)


rangoli(int(input('N: ')))
