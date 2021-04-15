import random

ls = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(random.choice([i for i in ls if i%2==0]))
