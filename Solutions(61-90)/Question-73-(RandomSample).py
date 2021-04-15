import random

# IMO better solution
print(random.sample(range(100, 201, 2), k=5))

#print(random.sample([i for i in range(100, 201) if i%2==0], k=5))