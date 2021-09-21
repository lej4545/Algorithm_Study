import math

def solution(n, k):
    answer = -1
    change = ''
    while True:
        n, b = divmod(n, k)
        change = str(b) + change
        if n == 0:
            break
    print(change)
    check_list = change.split("0")
    check_list = ' '.join(check_list).split()

    check_list = list(map(int, check_list))
    print(check_list)
    max_num = max(check_list)
    primes = []

    def is_prime_num(n):
        if n == 1:
            return False
        else:
            for i in range(2, int(math.sqrt(n)) + 1):  # n의 제곱근을 정수화 시켜준 후 + 1
                if n % i == 0:
                    return False
            return True
    # a = [False, False] + [True] * (max_num - 1)
    # for i in range(2, max_num + 1):
    #     if a[i] is True:
    #         for j in range(2 * i, max_num + 1, i):
    #             a[j] = False
    for j in check_list:
        if is_prime_num(j) is True:
            primes.append(j)
    answer = len(primes)

    return answer


print(solution(99999999, 10))
