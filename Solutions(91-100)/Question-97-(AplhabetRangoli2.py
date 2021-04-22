# My second solution
from string import ascii_letters


def rangoli(N):
    width = 4*N-3  # Number of symbols in one row

    final = []
    for i in range(N):
        right = '-'.join(ascii_letters[N-i-1:N])
        middle = right[-1:0:-1] + right
        half = middle.center(width, '-')
        final.append(half)

    for i in range(N-1):
        final.insert(N, final[i])

    for line in final:
        print(line)


rangoli(int(input('N: ')))
