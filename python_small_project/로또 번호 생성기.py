import random

# 방법 1
for i in range(10):
    cnt = 0
    number_list = []
    while cnt < 7:
        number = random.randint(1, 50)
        if number in number_list:
            continue
        else:
            number_list.append(number)
            cnt += 1
    number_list.sort()
    print(number_list)
print()
# 방법 2
for i in range(10):
    number_list = random.sample(range(1,51),7)
    number_list.sort()
    print(number_list)