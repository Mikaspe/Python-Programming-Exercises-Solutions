a = 1000
b = 3000
values = []

for x in range(a, b+1):
    s = str(x)
    if int(s[0]) % 2 == 0 and int(s[1]) % 2 == 0 and int(s[2]) % 2 == 0 and int(s[3]) % 2 == 0:
        values.append(s)

print(','.join(values))
