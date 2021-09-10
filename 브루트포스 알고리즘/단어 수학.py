from itertools import permutations

# case = int(input())
# words = {}
# alpha = {}
# for i in range(case):
#     a = input()
#     words[a] = len(a)
#     for j in a:
#         if j in alpha:
#             alpha[j] += 1
#         else:
#             alpha[j] = 1
#
# words = sorted(words.items(), key=lambda x: x[1], reverse=True)
# numbers = list(range(9, 9-len(alpha),-1))
# print(words)
# print(numbers)
# if len(words) >= 2:
#     diff = words[0][1] - words[1][1]
# else:
#     diff = words[0][1]
# dic_alpha = {}
# if diff > 0:
#     first = words[0][0]
#     m = 9
#     for i in range(diff):
#         dic_alpha[first[i]] = m
#         m -= 1
# print(dic_alpha)

# for i in permutations(numbers[diff:]):
#     print(i, end=" ")
#

import sys
alphabet_dict = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0}
alphabet_list = []
sorted_list = []
answer = 0

n = int(sys.stdin.readline())

for i in range(n):
    alphabet = input()
    alphabet_list.append(alphabet)

for alphabet in alphabet_list:
    for i in range(len(alphabet)):
        num = 10**(len(alphabet)-i-1)
        alphabet_dict[alphabet[i]] += num

for value in alphabet_dict.values():
    if value > 0:
        sorted_list.append(value)

sorted_list = sorted(sorted_list, reverse=True)

for i in range(len(sorted_list)):
    answer += sorted_list[i] * (9-i)

print(answer)