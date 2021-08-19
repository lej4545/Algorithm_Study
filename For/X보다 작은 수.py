n, x = map(int, input().split())

a = [int(i) for i in input().split()]

for i in a:
    if i < x:
        print(i, end = " ")