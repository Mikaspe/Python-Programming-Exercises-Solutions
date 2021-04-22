m = input('M: ')
m_set = set(map(int, input('M integers: ').split()))
n = input('N: ')
n_set = set(map(int, input('N integers: ').split()))

symmetric_difference = sorted(list(m_set ^ n_set))

for num in symmetric_difference:
    print(num)
