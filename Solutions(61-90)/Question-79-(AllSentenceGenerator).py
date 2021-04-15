subject = ['I', 'You']
verb = ['Play', 'Love']
obj = ['Hockey.', 'Football.']


for sub in subject:
    for v in verb:
        for o in obj:
            print('{} {} {}'.format(sub, v, o))
