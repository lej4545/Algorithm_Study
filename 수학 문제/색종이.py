# 백준 2563번 색종이

def check_color_paper(x, y):
    global points
    result = False
    for point in points:
        if (point[0] <= x < point[0] + 10) and (point[1] <= y < point[1] + 10):
            result = True
            break

    return result

case = int(input())
points = []
area = 0

for _ in range(case):
    x, y = map(int, input().split())
    points.append([x, y])

for i in range(101):
    for j in range(101):
        a = check_color_paper(i, j)
        if a is True:
            area += 1

print(area)