while :
    m, n = map(int, input().split())
    array = [False, False] + [True] * (n - 1)
    primes = []
    for i in range(2, n+1):
      if array[i] is True:
        if i >= m:
            print(i)
        for j in range(2*i, n+1, i):
            array[j] = False

