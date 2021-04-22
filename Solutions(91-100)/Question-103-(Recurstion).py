def sum_of_1_to_n(n):
    return sum_of_1_to_n(n-1) + n if n!=0 else 0

n = int(input())

print(sum_of_1_to_n(n))