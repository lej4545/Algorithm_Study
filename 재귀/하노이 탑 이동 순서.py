# x = int(input())
# x -= 20
# if x >= 0:
#     print(x)
# else:
#     print('0')

# x = int(input())
# x -= 20
# if 0 <= x <= 255:
#     print(x)
# elif x < 0:
#     print('0')
# else:
#     print('255')

# time = input('현재시간 : ')
# if time[3:] == '00':
#     print('정각 입니다.')
# else:
#     print('정각이 아닙니다.')

# personal = input('주민번호 뒷자리 : ')
# Q = int(personal[0])
# if len(personal) == 7:
#     if Q == 1 or Q == 3:
#         print('남자')
#     elif Q == 2 or Q == 4:
#         print('여자')
#     else:
#         print('잘못된 입력 입니다.')
# else:
#     print('자릿수가 틀립니다.')

# money = int(input('금액을 입력하세요 :'))
# if money <= 10000:
#     choice = int(input('음료를 선택하세요 :'))
#     if choice == 1:
#         drink = 700
#     elif choice == 2:
#         drink = 600
#     elif choice == 3:
#         drink = 800
#     else:
#         print('다른 번호를 입력해주세요.')
#
#     change = money - drink
#     if change >= 0:
#         print('잔액은', change, '원입니다.')
#     else:
#         print('금액이 부족합니다.')
# else:
#     print('최대 금액 초과했습니다.')

# x1 = int(input('첫번째 연산:'))
# x2 = int(input('두번째 연산:'))
# xcal = input('cal:')
# if x2==0 and xcal == '/':
#     print('예외')
# else:
#     cal = {'+':x1+x2,'-':x1-x2,'*':x1*x2,'/':x1/x2}
#     if xcal not in cal:
#         print('잘못된 연산자입니다')
#     else:
#         print('정답:',cal[xcal])

# apple = int(input('사과 구입 개수:'))
# orange = int(input('귤 구입 개수:'))
# prices = {'apple':150,'orange':30}
# total = apple * prices['apple'] + orange * prices['orange']
# if apple >= 5 and orange >= 3:
#     total *= 0.7
# print('총 금액은',total,'입니다')

# year = int(input('연도를 입력하세요 :'))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print('윤달입니다.')
#         else:
#             print('윤달이 아닙니다.')
#     else:
#         print('윤달입니다')
# else:
#     print

# x = [19,-17,25,102,8,62,21]
# for i in x:
#     print(10*i,end=' ')

# num = int(input())
# for i in range(1, 10):
#     print(num,'*',i,'=',num*i)

# a = int(input())
# total = 0
# for i in range(a+1):
#     total += i
# print(total)

# total = 0
# for i in range(10):
#     print(i+1,'번째의 돌')
#     total += float(input('무게(g) : '))
# print('평균   : ', total /10, 'g')

# student = int(input('학생의 수 : '))
# total = 0
# for i in range(student):
#     print(i, '번 학생의 점수 : ',end='')
#     total += int(input())
# print('평균   : ', total / student,'점')

# i = 100
# while i >= 1:
#     print('Hello, world!', i)
#     i -= 1

# kor = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# a = 0
# total = 0
# while a < len(kor):
#     total += kor[a]
#     a += 1
# print(total/len(kor))

# i = 1
# total = 1
# while i <= 20:
#     total *= 2
#     i += 1
# print('2의 20승은',total,'입니다')

# while True:
#     year = float(input('년도를 입력해주세요 : '))
#     if year != -1:
#         if year % 4 == 0:
#             if year % 100 == 0:
#                 if year % 400 == 0:
#                     print('윤년입니다.')
#                 else:
#                     print('평년입니다.')
#             else:
#                 print('윤달입니다')
#     else:
#         break
# print('종료되었습니다.')

import random

# for i in range(1,5):
#     for j in range(5):
#         if j >= i:
#             print(" ",end="")
#     print('*'*(2*i-1))

# for i in range(1,5):
#     for j in range(5-i):
#         print('b',end="")
#     for j in range(2*i - 1):
#         print('*',end='')
#     print()

# for i in range(1,5):
#     space = ' '
#     star = '*'
#     print(space*(4-i)+star*(2*i-1))

# for i in range(1,6):
#     for j in range(i-1):
#         print('n',end="")
#     for j in range(6-i):
#         print('*',end="")
#     print()

# height = int(input())
# for i in range(height):
#     print(' '*i+'*'*(2*(height-i)-1))

# for i in range(1,101):
# #     if (i % 3 == 0) and (i % 5 == 0):
# #         print('FizzBuzz',end=' ')
# #     elif i % 3 == 0:
# #         print('Fizz',end=' ')
# #     elif i % 5 == 0:
# #         print('Buzz',end=' ')
# #     else:
# #         print(i,end=' ')

# for i in range(1, 101):
#     print('Fizz'*(i % 3 == 0) + 'Buzz'*(i % 5 == 0) or i)

# import turtle as t
# t.pensize(10)
#
# # 삼각형 만들기
# t.penup()
# t.goto(-200,-50)
# t.pendown()
# t.circle(40,steps=3)
#
# # 사각형 만들기
# t.penup()
# t.goto(-100,-50)
# t.pendown()
# t.circle(40,steps=4)
#
# # 오각형 만들기
# t.penup()
# t.goto(0,-50)
# t.pendown()
# t.circle(40,steps=6)
#
# #원 만들기
# t.penup()
# t.goto(100,-50)
# t.pendown()
# t.circle(40)

import turtle as t
# import keyboard
# while True:
#     if keyboard.is_pressed('left'):
#         print('left')
#     elif keyboard.is_pressed('right'):
#         print('right')
#     elif keyboard.is_pressed('up'):
#         print('up')
#     elif keyboard.is_pressed('down'):
#         print('down')
#     elif keyboard.is_pressed('a'):
#         print('quit')
#         quit()
#         break
#
# import turtle as t
#
# t.shapesize(1, 1, 1)
# t.shape('turtle')
# t.pensize(3)
#
# pos_angle = 0
# pos_pos = 0
#
# import keyboard
#
# while True:
#     if keyboard.is_pressed('left'):
#         t.lt(pos_angle)
#         pos_angle += 1
#         print('left')
#
#     elif keyboard.is_pressed('right'):
#         pos_angle += 1
#         t.rt(pos_angle)
#         print('right')
#
#     elif keyboard.is_pressed('up'):
#         pos_pos += 1
#         t.forward(pos_pos)
#         print('up')
#
#     elif keyboard.is_pressed('down'):
#         pos_pos += 1
#         t.backward(pos_pos)
#         print('down')
#
#     elif keyboard.is_pressed('a'):
#         print('quit')
#         t.bye()
#         break
#
#
# import turtle as t
#
# n = 60
# t.shape('turtle')
# t.speed('fastest')
# for i in range(n):
#     t.circle(120)
#     t.right(360/n)

# import turtle as t
#
# n = 5
# t.shape('turtle')
# for i in range(n):
#     t.forward(100)
#     t.right(144)
#     t.forward(100)
#     t.left(72)

# for i in range(1, 11):
#     print(i, end=" ")
# print()
#
# num = 1
# while num <= 10:
#     print(num ,end =" ")
#     num += 1

# start = int(input('시작하는 정수 입력 : '))
# end = int(input('끝나는 정수 입력 : '))
# cnt = 0
# for i in range(start,end+1):
#     cnt += i
# print(cnt)
#
# total = 0
# while start <= end:
#     total += start
#     start += 1
# print(total)

# start = int(input('시작하는 정수 입력 : '))
# end = int(input('끝나는 정수 입력 : '))
# cnt = 0
# for i in range(start,end+1):
#     if i % 2 == 0:
#         cnt += i**2
# print(cnt)
#
# total = 0
# while start <= end:
#     if start % 2 == 0:
#         total += start**2
#     start += 1
# print(total)

# kor = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# total = 0
# for i in kor:
#     total += i
# print(total//len(kor))
# total, i = 0, 0
# while i < len(kor):
#     total += kor[i]
#     i += 1
# print(total//len(kor))

# total = 0
# for i in range(1000):
#     if i % 5 == 0 or i % 3 == 0:
#         total += i
# print(total)
#
# i, total = 0, 0
# while i < 1000:
#     if i % 5 == 0 or i % 3 == 0:
#         total += i
#     i += 1
# print(total)

# scores = list(map(int, input('실기점수를 입력하세요 : ').split()))
# min = scores[0]
# max = scores[0]
# for i in scores:
#     if i <= min:
#         min = i
#     if i >= max:
#         max = i
#
# total = 0
# for i in scores:
#     if i == min or i == max:
#         continue
#     else:
#         total += i
# print('이 학생의 평균 점수는', total/3, '입니다.')

# name_list = ['matthew', 'mark', 'luke', 'john', 'paul', 'peter']
# count = 0
# for i in name_list:
#     if 'm' in i or 'h' in i:
#         count += 1
# print('m 또는 h가 이름에 포함된 사람은',count,'명 입니다.')

# arr = [1, 4, 2, 3]
#
# left, right = 0, len(arr)-1
# while left <= right:
#     arr[left],arr[right] = arr[right],arr[left]
#     left += 1
#     right -= 1
# print(arr)

# num = int(input())
# for i in range(1,10):
#     print(num, '*', i, '=', num*i)
#
# i = 1
# while i < 10:
#     print(num, '*', i, '=', num*i)
#     i += 1

# for i in range(1,10):
#     for j in range(2,10):
#         print(j,'X',i,'=',i*j, end='\t')
#     print()
#
# print()
# i = 1
# while i < 10:
#     j = 2
#     while j < 10:
#         print(j, 'X', i, '=', i * j,end='\t')
#         j += 1
#     print()
#     i += 1

# votes = [5,2,3,4,1,2,1,2,2,3]
# candidates = ['','전정국','김남준','박지민','정호석','김태형']
# counter = [0]*6
#
# for i in votes:
#     counter[i] += 1
#
# max_votes = counter[0]
# for j in range(len(counter)):
#     if counter[j] >= max_votes:
#         max_votes = counter[j]
#         max_counter = j
#
# print(candidates[max_counter],'후보가 총',max_votes,'표를 얻어 당선되었습니다.')

# num = int(input('순환할 숫자를 입력하시용 : '))
# num_list = list(range(1,num+1))
# for i in range(num):
#     a = num_list[i:]+num_list[:i]
#     for j in a:
#         print(j, end=" ")
#     print()

# a = [10, 20, 30, 40, 20, 50, 20, 30, 60, 70, 20]
# result = []
# for i, v in enumerate(a):
#     if v == 20:
#         result.append(i)
#
# print(result)

# a = [38, 21, 53, 62, 19]
# min, max = a[0], a[0]
# for i in a:
#     if i <= min:
#         min = i
#     if i >= max:
#         max = i
#
# print(min, max)

# a = [38, 21, 53, 62, 19]
# a.sort()
# print(a[0],a[-1])

# numbers = []
#
# for i in range(1,11):
#     numbers.append(i)
#
# for j in numbers:
#     if j % 2 != 0:
#         numbers.remove(j)
#
# numbers.sort(reverse=True)
# print(numbers)

# a = ['alpha','foxtrot']
# b = [i for i in a if len(i) == 5]
# print(b)


# while True:
#     a, b = map(int, input().split())
#     if (1 <= a <= 20) and (10 <= b <= 30) and (a < b):
#         lst = [2**i for i in range(a, b+1)]
#         del lst[1]
#         del lst[-2]
#         print(lst)
#         break
#     else:
#         print('입력 범위가 잘 못 되었습니다. 다시 입력해주세요.')

# ai_classes = {
#      'class01' : [
#                 {'name' : '서준', 'age' : 24},
#                 {'name' : '하준', 'age' : 34},
#                 {'name' : '도윤', 'age' : 37},
#                 {'name' : '시윤', 'age' : 19},
#                 {'name' : '은우', 'age' : 31}
#      ],
#      'class02' : [
#                   {'name' : '지호', 'age' : 34},
#                   {'name' : '예준', 'age' : 19},
#                   {'name' : '동원', 'age' : 21},
#                   {'name' : '민정', 'age' : 22},
#                   {'name' : '효주', 'age' : 24}
#      ]
#  }
#
# for i in ai_classes.values():
#     for j in i:
#         if j['age'] >= 30:
#             print(j['name'],':', j['age'],' / ',end="")

# def operation(operator):
#     a = int(input('첫번쨰 숫자를 입력하세요. '))
#     b = int(input('두번쨰 숫자를 입력하세요. '))
#     if operator == 1:
#         result = a+b
#     elif operator == 2:
#         result = a-b
#     elif operator == 3:
#         result = a*b
#     elif operator == 4:
#         if b == 0:
#             print('연산을 할 수 없습니다. 다시 입력해주세요.')
#         else:
#             result = a/b
#     elif operator == 5:
#         result = a%b
#     return result
#
#
# print('==================')
# print('1. 더하기\n2. 빼기\n3. 곱하기\n4. 나누기\n5. 나머지 구하기\n6. 나가기')
# print('==================')
#
# while True:
#     operator = int(input('원하는 연산자를 입력하세요. '))
#     if 0 < operator < 6:
#         result = operation(operator)
#         print("결과는 %.2f 입니다."%result)
#     elif operator == 6:
#         print('종료를 선택하셨습니다. 프로그램을 종료합니다..')
#         break
#     else:
#         print('잘못입력하셨습니다. 다시 입력해 주세요.')

# a = list(range(1,11))
# b = list(map(lambda x: str(x) if x== 1 else float(x) if x== 2 else x+10,a))
# def f(x):
#     if x == 1:
#         return str(x)
#     elif x == 2:
#         return float(x)
#     else:
#         return x + 10
#
# c = list(map(f,a))
# print(c)
#
# plus_ten = lambda x : x + 10
# print(plus_ten)
#
# data=plus_ten(1)
# print(data)
#
# a1 = lambda x : x + 10
# print(a1(10))
#
# y = 10
# a_10 = lambda x : y + 10
# print(a_10(10))
#
# a = [1, 2, 3, 4]
# b = [2, 4, 6, 8]
#
# a_list = list(map(lambda x, y : x*y, a, b))
# print(a_list)

# from functools import reduce
# def f(x, y):
#     return x + y
#
# a = [1,2,3,4,5]
# print(reduce(f, a))
#
# print(reduce(lambda x, y:x + y, a))

# x = 10
# def foo():
#     global x
#     x = 20
#     print(x)
# print(x)
# foo()
# print(x)

# inFp = open("C:/Users/EunJin/Documents/data/data1.txt", 'r', encoding='utf-8')
# inStr = inFp.readline()
# print(inStr, end="")
# inStr = inFp.readline()
# print(inStr,end="")

# filename = input('파일명을 입력하세요 :')
# document = "C:/Users/EunJin/Documents/data/"+filename
# inFp = open(document, 'r', encoding='utf-8')
# inList = []
# inList = inFp.readlines()
# for i in inList:
#     print(i,end="")
# inFp.close()

# inFp, outFp = None, None
# inStr = ""
# inFp = open('C:/Users/EunJin/Documents/data/data2.txt','r',encoding='utf-8')
# outFp = open('C:/Users/EunJin/Documents/data/data2_copy.txt','w',encoding='utf-8')
# inList = inFp.readlines()
# for inStr in inList:
#     outFp.write(inStr)

# while True:
#     outStr = inFp.readline()
#     if outStr != "":
#         outFp.write(outStr)
#     else:
#         break
# inFp.close()
# outFp.close()
# print("--정상적으로 파일이 복사되었음--")

# import datetime
# print(datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))

from collections import deque


# def solution(priorities, location):
#     answer = 0
#     dict_alpha = {}
#     result = []
#     result_idx = []
#     for i in range(len(priorities)):
#         dict_alpha[i] = priorities[i]
#     dq = deque(priorities)
#     while len(dq) > 1:
#         a = dq.popleft()
#         if a < max(dq):
#             dq.append(a)
#         else:
#             result.append(a)
#     a = dq.popleft()
#     result.append(a)
#
#     idx = 0
#     i = 0
#     while True:
#         if priorities[idx] != result[i]:
#             idx += 1
#         else:
#             result_idx.append(idx)
#             i += 1
#             idx += 1
#         if idx >= len(priorities):
#             idx -= len(priorities)
#         if i >= len(priorities):
#             break
#     answer = result_idx.index(location)+1
#     return answer

# class Person:
#     def __init__(self, name, age, address, wallet):
#         self.hello = '안녕하세요.'
#         self.name = name
#         self.age = age
#         self.address = address
#         self.__wallet = wallet
#
#     def pay(self, amount):
#         self.__wallet -= amount
#         print('이제 {0}원 남았네요.'.format(self.__wallet))
#
# maria = Person('마리아', 20, '서울시 서초구 반포동', 100000)
# maria.pay(1000)

# class OrangeBox:
#     def __init__(self):
#         self.__count = 10
#     def __del__(self):
#         print('Class종료')
#     def AddBox(self, add_count):
#         self.__count += add_count
#     def SubBox(self, sub_count):
#         self.__count -= sub_count
#     def DelBox(self):
#         self.__count = 0
#     def CountBox(self):
#         return self.__count
#
# MyOB = OrangeBox()
# nData = int(input('추가 수량'))
# MyOB.AddBox(nData)
# print('현재 수량 %d'%MyOB.CountBox())
#
# nData = int(input('제거 수량'))

# class Person:
#     def __init__(self):
#         print('Person __init__')
#         self.hello = '안녕하세요.'
#
# class Student(Person):
#     def __init__(self):
#         print('Student __init__')
#         super().__init__()
#         self.school = '파이썬 코딩 도장'
#
# james = Student()
# print(james.school)
# print(james.hello)