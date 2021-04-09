words = input().split()

my_dict = {i:words.count(i) for i in words}

print(my_dict)
