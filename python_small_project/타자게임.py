import random
import time
import keyboard

def game():
    words_list = ['cat', 'dog', 'fox', 'monkey', 'mouse', 'panda', 'frog', 'snake', 'wolf', 'python', 'k-digital']
    cnt = 1
    start = time.time()
    while cnt <= 5:
        random_word = random.choice(words_list)
        print('*문제',cnt)
        print(random_word)
        while True:
            input_word = input()
            if input_word == "":
                continue
            elif random_word == input_word:
                print('통과!')
                cnt += 1
                break
            else:
                print('실패!')
                print(random_word)
        print()
    take_time = '{:.2f}'.format(time.time() - start)
    return take_time

print('[타자 게임] 준비되면 Enter!')

while True:
    if keyboard.is_pressed('enter'):
        take_time = game()
        print('타자 시간 : ', take_time, '초')
        break


