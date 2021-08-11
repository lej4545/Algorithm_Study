n, m = list(map(int, input().split()))
d = [0] + [10001] * (m+1)
a = [0]* n
for i in range(n):
    a[i] = int(input())

for i in range(n):
    for j in range(a[i], m+1):
        if d[j-a[i]] != 10001:
            d[j] = min(d[j], d[j-a[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])