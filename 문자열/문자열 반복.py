case = int(input())

for i in range(case):
    r, s = input().split()
    r = int(r)
    result = ""
    for j in range(len(s)):
        result += s[j] * r

    print(result)