while True:
    a, b, c = map(int, input().split())
    if a == 0:
        break
    if a**2 + b**2 == c**2:
        print('right')
    else:
        if b**2 + c**2 == a**2:
            print('right')
        else:
            if c**2 + a**2 == b**2:
                print("right")
            else:
                print('wrong')