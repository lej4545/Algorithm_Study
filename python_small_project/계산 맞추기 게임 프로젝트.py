import random
cnt = 0

def make_question():
    operator = {1 : '+', 2 : '-', 3 : '*'}
    a, b = random.choices(range(-99, 100), k=2)
    operator_number = random.randint(1,3)
    queistion = '%d %s %d'%(a, operator[operator_number], b)
    return queistion

for i in range(5):
    question = make_question()
    print(question, '=')
    answer = int(input())
    if eval(question) == answer:
        cnt += 1

print('총 5문제 중', cnt,'문제 맞췄습니다.',sep='')