ss = input().split()

words = sorted(set(ss))  # List of sorted, unique words
my_dict = {word: ss.count(word) for word in words}

print(my_dict)
