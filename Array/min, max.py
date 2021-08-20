# n = int(input())
# data = list(map(int, input().split()))
# print(min(data), max(data))

list = []
for i in range(9):
    a = int(input())
    list.append(a)
print(max(list))
print(list.index(max(list))+1)