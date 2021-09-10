# from itertools import combinations
#
n, s = map(int,input().split())
n_list = list(map(int, input().split()))
#
#
# count = 0
# for i in range(1,n+1):
#     combi = list(combinations(n_list, i))
#     for j in combi:
#         if sum(j) == s:
#             count += 1
#
#
# print(count)

# 모듈을 사용하지 않은 풀이
import sys

def make_comb(arr, comb, s):
    cnt = 0
    for front in arr:
        for end in list(comb):
            comb.append(front + end)
            print(comb)
            if comb[-1] == s:
                cnt += 1
    return cnt

cnt = make_comb(n_list, [0], s)

print(cnt)

