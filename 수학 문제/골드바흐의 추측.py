import sys
arr = [False, False] + [True] * 9999
for i in range(2, 5001):
  if arr[i]:
    for j in range(i * 2, 10001, i):
      arr[j] = False

T = int(sys.stdin.readline())
for i in range(T):
  num = int(sys.stdin.readline())
  for j in range(num // 2, num):
    if arr[j]:
      if arr[num - j]:
        print(num - j, j, sep = ' ')
        break