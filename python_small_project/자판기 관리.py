# 음료와 가격, 제고, 금액에 대한 변수 정의
menu = (('',0),('사이다',1200),('콜라',1100),('생수',700),('주스',1500),('커피',1300))
money_list = [0, 10000, 5000, 1000, 500, 100]
product_list = {'':0, '사이다':3, '콜라':3, '생수':3, '주스':3, '커피': 3}

print('돈을 투입하세요:')
print()
money = 0

# 관리자 모드에서 1번과 2번을(추가와 제거) 선택 했을 때 실행되는 함수
def add_remove_mode(mode):
    if mode == 1:
        word = '추가'
    elif mode == 2:
        word = '제거'
    print(word,': 제품을 선택하세요 - ', sep="",end="")
    select_product = int(input())
    print(menu[select_product][0], '는', product_list[menu[select_product][0]], '개 재고가 있습니다')
    print('몇 개를',word,'하나요 - ',end="")
    plus = int(input())
    product_list[menu[select_product][0]] += plus
    print(menu[select_product][0], '의 총 재고가', product_list[menu[select_product][0]], '개로 변경 되었습니다.')

# 재고 관리 모드 실행
def product_management_mode():
    while True:
        mode = int(input('재고 관리 모드입니다. 1:제품 추가 2:제품 제거 3:현재 수량 0:재고 관리 종료\n숫자를 입력해주세요 - '))
        if mode == 1 or mode == 2:
            add_remove_mode(mode)
        if mode == 3:
            for i in range(1, 6):
                print(i, '.', menu[i][0], ' 수량: ', product_list[menu[i][0]], sep="")
        if mode == 0:
            print('재고 관리 모드를 종료하겠습니다.')
            break
        print()
    print()

# 금액 안내와 돈 투입 part
while True:
    print('1:10,000원 2:5,000원 3:1,000원 4:500원 5:100원 0:입력완료 99:재고 관리 모드')
    money_number = int(input('금액 번호를 고르세요 : '))
    if 0 < money_number < 5:
        money += money_list[money_number]
        print('누적금액:', money, '원')
    elif money_number == 99:
        product_management_mode()
    elif money_number == 0:
        print('총 투입 금액은', money, '원입니다.')
        break
    else:
        print('금액 번호가 잘못되었습니다. 다시 입력해주세요.')
    print()
print()

balance = money  # 투입 금액 백업

# 음료 선택 part
while True:
    print('[자판기 판매 메뉴]')
    for i in range(1, 6):
        print(i,'.',menu[i][0],' 가격: ',menu[i][1], sep="")

    menu_number = int(input('메뉴번호를 선택하세요[선택완료:0]: '))
    if 0 < menu_number < len(menu):
        if product_list[menu[menu_number][0]] > 0:
            if balance < menu[menu_number][1]:
                print('돈이 부족합니다! 다시 입력해주세요.')
            else:
                product_list[menu[menu_number][0]] -= 1
                balance -= menu[menu_number][1]
                print(menu[menu_number][0], '구입완료\n잔액:',balance)
        else:
            print('재고가 부족합니다.')
    elif menu_number >= len(menu):
        print('해당 번호에 맞는 제품이 없습니다. 다시 입력해주세요.')
    elif menu_number == 0:
        print('투입 =',money,'잔액 =',balance)
        break
    print()

print('\n거스름돈은 다음과 같습니다.')

rest = balance # 남은 잔액 백업

# 거슬러 줄 돈 part
for i in range(1, 6):
    cnt = rest // money_list[i]
    rest -= (cnt * money_list[i])
    print(money_list[i],'원짜리 지폐:', cnt, '장', sep="")

print('\n자판기 종료, 잔액',balance,'반환')