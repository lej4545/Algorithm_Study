import sys

n = int(sys.stdin.readline())
result = 0

if n < 45:
    for i in range(0, n):
        a_list = list(map(int, list(str(i))))
        if i + sum(a_list) == n:
            result = i
            break
else:
    for i in range(n - 45, n-1):
        a_list = list(map(int, list(str(i))))
        if i + sum(a_list) == n:
            result = i
            break

print(result)
