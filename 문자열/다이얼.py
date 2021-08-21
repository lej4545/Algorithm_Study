a = input()
b = 0

for i in a:

    if i == 'A' or i == 'B' or i == 'C':
        b += 3
    elif i == 'D' or i == 'E' or i == 'F':
        b += 4
    elif i == 'G' or i == 'H' or i == 'I':
        b += 5
    elif i == 'J' or i == 'K' or i == 'L':
        b += 6
    elif i == 'M' or i == 'N' or i == 'O':
        b += 7
    elif i == 'P' or i == 'Q' or i == 'R' or i == 'S':
        b += 8
    elif i == 'T' or i == 'U' or i == 'V':
        b += 9
    elif i == 'W' or i == 'X' or i == 'Y' or i == 'Z':
        b += 10
print(b)