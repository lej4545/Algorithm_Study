from itertools import combinations
import sys

n, m = map(int,sys.stdin.readline().rstrip().split())
cards = list(map(int,sys.stdin.readline().rstrip().split()))

combi = list(combinations(cards, 3))
result = []

for i in combi:
    if sum(i) <= m:
        result.append(sum(i))
print(max(result))