from itertools import combinations
import math




def solution(nums):
    answer = 0

    def is_prime_num(n):
        if n == 1:
            return False
        else:
            for i in range(2, int(math.sqrt(n)) + 1):  # n의 제곱근을 정수화 시켜준 후 + 1
                if n % i == 0:
                    return False
            return True
    for data in combinations(nums,3):
        if is_prime_num(sum(data)) is True:
            answer += 1


    return answer

print(solution([1,2,3,4]))