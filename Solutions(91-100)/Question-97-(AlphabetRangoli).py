#My first solution
from string import ascii_lowercase
N = 25

y_size = 4*N-3

y_mid = int((4*N-3)/2)  # Middle column
alphabet = ascii_lowercase[N-1::-1]

rangoli = [['-' for y in range(y_size)] for x in range(N)]
index_letter = []  # Index in which column will be a letter

for x in range(N):
    index_letter[:0] = [y_mid - 2 * x, y_mid + 2 * x]
    print(index_letter)
    for k in range(N):
        for y in index_letter[2*k : 2*k+2]:
            print(y)
            rangoli[x][y] = alphabet[k]

# Printing result
for x in range(N):
    print('')
    for y in range(y_size):
        print(rangoli[x][y], end='')

for x in range(N - 2, -1, -1):
    print('')
    for y in range(y_size):
        print(rangoli[x][y], end='')
