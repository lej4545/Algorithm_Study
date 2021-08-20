n = int(input())
scores = list(map(int, input().split()))
m = max(scores)
new_scores = [i/m*100 for i in scores]

avg_scores = sum(new_scores) / n

print(avg_scores)