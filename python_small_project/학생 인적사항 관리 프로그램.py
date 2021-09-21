# 인적사항 등록 함수
def register(person_dict):
    number = int(input('학번을 입력하세요 :'))
    name = input('이름을 입력하세요 :')
    score = input('학점을 입력하세요 :')
    person_dict[number] = [name, score]
    print('등록이 완료되었습니다.')

# 인적사항 수정 함수
def modify(person_dict):
    modify_number = research(person_dict)
    item = input('수정을 원하는 항목을 입력하시요(이름, 학점):')
    value = input('수정할 값 :')
    if item == '이름':
        person_dict[modify_number][0] = value
    else:
        person_dict[modify_number][1] = value

# 인적사항 검색 함수
def research(person_dict):
    while True:
        number = int(input('검색을 원하는 학생의 학번을 입력하세요 :'))
        if number in person_dict:
            print('학번 :',number)
            print('이름 :',person_dict[number][0])
            print('학점 :',person_dict[number][1])
            break
        else:
            print('입력한 학번을 찾을 수 없습니다. 다시 입력해주세요.')
    return number

# 인적사항 삭제 함수
def delete(person_dict):
    number = int(input('삭제를 원하는 학생의 학번을 입력하세요 :'))
    del person_dict[number]
    print('삭제가 완료되었습니다')

person_dict = {} # 학생, 학번, 학점을 담을 딕셔너리 변수
# key : 학번
# value : [이름, 학점]

# 프로그램 실행
while True:
    print('1.인적사항 등록\t2.학생 검색\t3.학생 수정\t4.학생 삭제\t5.전체학생 보기\t6. 프로그램 종료')
    num = int(input('원하는 번호를 입력하세요 :'))
    if num == 1:
        register(person_dict)
    elif num == 2:
        research(person_dict)
    elif num == 3:
        modify(person_dict)
    elif num == 4:
        delete(person_dict)
    elif num == 5:
        for i in person_dict:
            print('학번 :', i)
            print('이름 :', person_dict[i][0])
            print('학점 :', person_dict[i][1])
    elif num == 6:
        print('프로그램을 종료하겠습니다.')
        break
    else:
        print('번호가 잘못되었습니다. 다시 입력해주세요.')