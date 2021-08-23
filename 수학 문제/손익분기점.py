a, b, c = map(int, input().split())
if b == c:
    print("-1")
else:
    result = a // (c - b)

    if result < 0:
        print("-1")
    else:
        print(result + 1)