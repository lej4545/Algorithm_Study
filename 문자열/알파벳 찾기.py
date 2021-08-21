a = input()
result = [-1] * 26

for i in range(len(a)):
    b = ord(a[i]) - 97
    if result[b] == -1:
        result[b] = i
    else:
        continue

for j in result:
    print(j,end=" ")
