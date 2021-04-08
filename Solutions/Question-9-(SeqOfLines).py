lines = []

while True:
    line = input()

    if line:    # Czyli gdy nie jest to znak pustej lini
        lines.append(line.upper())
    else:       # Czyli znak bialej linii
        break

for sentence in lines:
    print(sentence)
