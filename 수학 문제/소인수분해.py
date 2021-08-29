a = int(input())
lst = []
def prime(n):
    for i in range(2, (n/2) + 1):
        if n % i == 0:
            lst.append(i)
            print(i)
            prime(n // i)
            break
prime(a)

if len(lst) == 0:
    if a != 1:
        print(a)