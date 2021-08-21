def check_common_difference(n):
    if n < 100:
        result = True
        return result

    n = str(n)
    diff = int(n[1]) - int(n[0])

    for i in range(1, len(n)-1):
        next_diff = int(n[i+1]) - int(n[i])
        if diff == next_diff:
            result = True
        else:
            result = False
            return result
    return result


a = int(input())
count = 0
for j in range(1, a+1):
    if check_common_difference(j) is True:
        count += 1

print(count)