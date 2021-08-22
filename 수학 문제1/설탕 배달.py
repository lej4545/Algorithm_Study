a = int(input())
total = []
for five_kg in range(a // 5 + 1):
    three_kg = (a - 5 * five_kg) / 3
    if three_kg == int(three_kg):
        total.append(int(three_kg + five_kg))

if len(total) == 0:
    print("-1")
else:
    print(min(total))