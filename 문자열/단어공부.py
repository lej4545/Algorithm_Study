a = input()
a_upper = a.upper()

result = dict()
for i in range(len(a_upper)):
    alpha = a_upper[i]
    if alpha in result:
        result[alpha] += 1
    else:
        result[alpha] = 1

# print(max(result, key = result.get))
max_list = [key for key, val in result.items() if max(result.values()) == val]
if len(max_list) >= 2:
    print("?")
else:
    print(max_list[0])
