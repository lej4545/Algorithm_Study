a = int(input())
num = 1
variable_add = 6
door = 1
while num < a:
    num += variable_add
    door += 1
    variable_add += 6
print(door)