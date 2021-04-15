import math

def binary_search(ls, item):
    L = 0
    H = len(ls) - 1
    i = math.floor((L+H)/2)

    while True:
        if item > ls[i]:
            L = i
            i = math.ceil(((L+H)/2))
        elif item < ls[i]:
            H = i
            i = math.floor((L+H)/2)

        if ls[i] == item: return i
        if H - L == 1: return -1


ls = [1, 4, 6, 7, 9, 22, 24, 43, 54, 56, 65]

print(binary_search(ls, int(input('Item to search: '))))
