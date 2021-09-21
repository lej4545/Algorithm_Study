from itertools import combinations

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
dish = {}

# def solution(orders, course):
#     for i in orders:
#         for j in i:
#             if j in dish:
#                 dish[j] += 1
#             else:
#                 dish[j] = 1
#     print(dish)
#     a = list(dish.keys())
#     for k in course:
#         for data in combinations(a, k):
#
#
#     return a
#
# print(solution(orders, course))

data = ('A','B')
for i in orders:
    for j in data:
        if j in j:
            print('있다')
