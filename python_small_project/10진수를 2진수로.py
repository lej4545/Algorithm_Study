num = int(input('2진수로 변환할 10진수 입력 : '))
result = []

# 입력 받은 값을 2로 계속 나누는데 ( 더이상 안나눠질 때까지= 몫이 0이 될 때까지) 거기서 몫을
while num > 0:
    num, b = divmod(num, 2)
    result.insert(0, str(b))

print(''.join(result))
