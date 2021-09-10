n = int(input())
persons = []
for i in range(n):
    x, y = map(int, input().split())
    persons.append([x,y,i+1])

sorted_persons = sorted(persons, key=lambda x : x[0], reverse=True)
sorted_persons[0].append(1)


for i in range(1,n):
    rank = 0
    for j in range(i):
        if (sorted_persons[j][1] > sorted_persons[i][1]) and (sorted_persons[j][0] > sorted_persons[i][0]):
            rank += 1
    sorted_persons[i].append(rank+1)

sorted_persons = sorted(sorted_persons, key=lambda x: x[2])
for i in range(n):
    print(sorted_persons[i][3],end=' ')