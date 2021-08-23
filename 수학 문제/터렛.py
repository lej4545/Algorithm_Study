case = int(input())
for _ in range(case):
    x_1, y_1, r_1, x_2, y_2 , r_2 = map(int,input().split())
    distance = ((x_1 - x_2)**2 + (y_1 - y_2)**2)**0.5
    if distance > r_1 + r_2:
        result = 0
    elif distance == r_1 + r_2:
        result = 1
    elif distance < r_1 + r_2:
        if distance + min(r_1, r_2) < max(r_1, r_2):
            result = 0
        elif distance + min(r_1, r_2) == max(r_1, r_2):
            if distance == 0 or r_1 == r_2:
                result = -1
            else:
                result = 1
        else:
            result = 2


    print(result)