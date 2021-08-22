case = int(input())
for i in range(case):
    h, w, n = map(int, input().split())
    y = (n % h)
    x = (n // h) + 1
    if x < 10:
        x = '0' + str(x)
    else:
        x = str(x)
    print('%s%s'%(y,x))