def d(n):
    x = 0
    a = list(str(n))
    for i in a:
        x = x + int(i)
    return n + x

s_list = [False] * 10000

for k in range(1, 10000):
    if d(k) >= 10000:
        continue
    s_list[d(k)] = True

for j in range(1, 10000):
    if s_list[j] == False:
        print(j)