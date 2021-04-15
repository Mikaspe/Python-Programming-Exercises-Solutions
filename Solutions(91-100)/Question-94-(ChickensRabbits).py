heads = 35
legs = 94


for chickens in range(heads+1):
    rabbits = heads - chickens
    if (2*chickens)+(4*rabbits) == 94:
        num_of_chickens = chickens
        num_of_rabbits = rabbits


print('Chickens: {}, Rabbits: {}'.format (num_of_chickens, num_of_rabbits))
