def resident(k, n):
    for j in range(1, n+1):
        for m in range(1, k+1):
            house[m][j] = house[m][j-1] + house[m-1][j]

    return house[k][n]

house = []
case = int(input())

for i in range(15):
    house.append([0] * 15)
for i in range(15):
    house[0][i] = i

for _ in range(case):
    k = int(input())
    n = int(input())
    print(resident(k, n))