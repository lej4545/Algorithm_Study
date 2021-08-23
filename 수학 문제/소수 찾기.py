def check_prime_number(n):
    if n == 1:
        return False

    result = True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

case = int(input())

numbers = list(map(int, input().split()))
prime_number_list = []

for j in numbers:
    if check_prime_number(j) is True:
        prime_number_list.append(j)

print(len(prime_number_list))
