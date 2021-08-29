while True:
    n = int(input())
    if n == 0:
        break
    else:
        array = [False, False] + [True] * (2*n - 1)
        primes = []
        for i in range(2, 2*n+1):
          if array[i] is True:
            if n < i <= 2 * n:
                primes.append(i)
            for j in range(2*i, 2*n+1, i):
                array[j] = False
        print(len(primes))

