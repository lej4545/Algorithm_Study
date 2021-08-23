import math

def check_prime_number(n):
    if n == 1:
        return False

    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

m = int(input())
n = int(input())
prime_number = list()
for b in range(m, n+1):
    if check_prime_number(b) is True:
        prime_number.append(b)

if len(prime_number) == 0:
    print('-1')
else:
    print(sum(prime_number))
    print(prime_number[0])