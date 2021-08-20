a = input()
if len(a) < 2:
    a = '0' + a

b = a
count = 0
while True:
    plus = int(b[0]) + int(b[1])
    b = b[1] + str(plus % 10)
    count += 1
    if a == b:
        break
print(count)