ls = list(map(int, input().split()))

sorted_scores = sorted(list(set(ls)))

print(sorted_scores[-2])