from itertools import permutations

n = int(input())
data = list(range(1, n+1))

for i in permutations(data):
    for j in i:
        print(j, end=' ')
    print()