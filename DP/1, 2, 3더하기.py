def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    if n > 3:
        return solution(n-1) + solution(n-2) + solution(n-3)

case = int(input())
for i in range(case):
    n = int(input())
    print(solution(n))