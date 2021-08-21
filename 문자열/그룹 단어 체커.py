case = int(input())
result = case
for i in range(case):
    word = input()
    for j in range(len(word)-1):
        if word[j] == word[j+1]:
            continue
        elif word[j] in word[j+1:]:
            result -= 1
            break

print(result)