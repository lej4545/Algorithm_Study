menu = (('',0),('사이다',1200),('콜라',1100),('생수',700),('주스',1500),('커피',1300))
money_list = [0, 10000, 5000, 1000, 500, 100]

print('돈을 투입하세요:')
print()
money = 0
while True:
    print('1:10,000원 2:5,000원 3:1,000원 4:500원 5:100원 0:입력완료')
    money_number = int(input('금액 번호를 고르세요 : '))
    if money_number != 0:
        money += money_list[money_number]
        print('누적금액:', money, '원')
    else:
        print('총 투입 금액은', money, '원입니다.')
        break
    print()
print()

balance = money

while True:
    print('[자판기 판매 메뉴]')
    for i in range(1, 6):
        print(i,'.',menu[i][0],' 가격: ',menu[i][1], sep="")

    menu_number = int(input('메뉴번호를 선택하세요[선택완료:0]: '))

    if menu_number != 0:
        balance -= menu[menu_number][1]
        if balance < 0:
            print('돈이 부족합니다! 다시 입력해주세요.')
            balance += menu[menu_number][1]
        else:
            print(menu[menu_number][0], '구입완료\n잔액:',balance)
    else:
        print('투입 =',money,'잔액 =',balance)
        break
    print()

print('\n거스름돈은 다음과 같습니다.')

rest = balance

for i in range(1,6):
    cnt = rest // money_list[i]
    rest -= (cnt * money_list[i])
    print(money_list[i],'원짜리 지폐:', cnt, '장', sep="")

print('\n자판기 종료, 잔액',balance,'반환')