import math


def factorial1(x):  # By using recursive
    return 1 if x == 0 else x * factorial1(x - 1)


def factorial2(x):  # By using In-built function
    return math.factorial(x)


x = int(input('Pick a number: '))
print('With recursive solution:', factorial1(x))
print('With In-built solution:', factorial1(x))
