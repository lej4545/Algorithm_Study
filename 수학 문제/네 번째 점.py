rect = []
rect.append(list(map(int, input().split())))
rect.append(list(map(int, input().split())))
rect.append(list(map(int, input().split())))

x_dict = {}
y_dict = {}

for i in range(3):
    if rect[i][0] in x_dict:
        x_dict[rect[i][0]] += 1
    else:
        x_dict[rect[i][0]] = 1

for j in range(3):
    if rect[j][1] in y_dict:
        y_dict[rect[j][1]] += 1
    else:
        y_dict[rect[j][1]] = 1

for key in x_dict:
    if x_dict[key] == 1:
        print(key, end=" ")

for key in y_dict:
    if y_dict[key] == 1:
        print(key)