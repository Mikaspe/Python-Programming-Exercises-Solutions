log = input().split()
NET = 0
i = 0

while i < len(log):
    if log[i] == 'D':
       NET += int(log[i+1])
    elif log[i] == 'W':
        NET -= int(log[i+1])

    i += 2

print(NET)