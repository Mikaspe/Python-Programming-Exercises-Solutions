str = input('Pass 4 comma separated binary numbers: ').split(',')

solution = []

for n in str:
    if int(n, 2) % 5 == 0:
        solution.append(n)


print(','.join(solution))
