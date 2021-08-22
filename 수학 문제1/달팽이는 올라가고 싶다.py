a, b, v = map(int, input().split())
day = 0
days = 0
night = 0
while True:
    if day < v:
        day = night + a
        night = day - b
        days += 1
    else:
        break

print(days)