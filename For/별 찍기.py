line = int(input())

# # 별 찍기 - 1 문제
# for i in range(1, line+1):
#     star = "*"*i
#     print(star)

# 별 찍기 -2 문제
for i in range(1,line+1):
    print(" " * (line - i) + "*" * i)

