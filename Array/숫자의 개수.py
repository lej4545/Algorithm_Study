a = int(input())
b = int(input())
c = int(input())

multi = str(a*b*c)
result = [0] * 10

for i in range(len(multi)):
    result[int(multi[i])] += 1

for i in result:
    print(i)