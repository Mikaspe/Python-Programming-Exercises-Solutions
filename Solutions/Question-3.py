def dict_seq1(x):  # IMO better solution
    return {i: i*i for i in range(1, x+1)}


def dict_seq2(x):
    d = dict()
    for i in range(1, x + 1):
        d[i] = i*i

    return d


x = (int(input('Pick a number:')))

print('Solution nr 1:', dict_seq1(x))
print('Solution nr 2:', dict_seq2(x))

