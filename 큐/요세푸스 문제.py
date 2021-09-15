from collections import deque
k, n = map(int, input().split())

lst = list(range(1,k+1))
dq = deque([])
for i in lst:
    dq.append(i)

result = []
while True:
    for i in range(n-1):
        a = dq.popleft()
        dq.append(str(a))
    b = dq.popleft()
    result.append(str(b))
    if len(result) == k:
        break
print("<",end="")
print(", ".join(result),end="")
print(">",end="")

