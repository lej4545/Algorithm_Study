n, t = map(int, input().split())
position = {}
for i in range(n):
    a, b = map(int, input().split())
    r_p = a + (t * b)
    position[a] = r_p

position = sorted(position.items(), reverse=True)
count = 1
group = position[0][1]
for j in range(1, n):
    if position[j][1] >= group:
        continue
    else:
        group = position[j][1]
        count += 1
print(count)