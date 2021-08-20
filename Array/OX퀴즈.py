case = int(input())

for i in range(case):
    result = input()
    a = 0
    total = 0
    for j in result:
        if j == 'X':
            a = 0
        else:
            a += 1
        total += a

    print(total)