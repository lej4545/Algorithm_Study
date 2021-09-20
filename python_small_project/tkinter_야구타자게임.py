import tkinter as tk
import random

# 아웃이 3점 이상 되면 총점(새 창) 띄우기
def create_window(total):
    window = tk.Toplevel(root)
    result_text = '게임종료 : 총점은 '+str(total)+'점 입니다.'
    label_child = tk.Label(window, text = result_text)
    label_child.pack()

# 버튼을 클릭하면 입력한 숫자가 1부타, 2루타, 3루타, 홈런 인지 결과 처리
def func():
    global score, out, total, random_list

    number = int(text_box.get())
    if number in random_list[0:3]:
        result_label.config(text = '1루타 입니다')
        score += 1
    elif number in random_list[3:5]:
        result_label.config(text='2루타 입니다')
        score += 2
    elif number == random_list[5]:
        result_label.config(text='3루타 입니다')
        score += 3
    elif number == random_list[6]:
        result_label.config(text='홈런 입니다.')
        score += 4
    else:
        result_label.config(text='아웃입니다.')
        out += 1

    # 누적 후 함계가 4점이면 실제 1점으로 인정
    if score >= 4:
        score -= 4
        total += 1

    # 3 아웃되면 게임 종료 화면 창이 띄워짐
    if out == 3:
        create_window(total)

    random_list = list(random.sample(range(1, 11), 10))
    print(random_list[0: 7])
    return random_list

# 전연변수 설정.
score = 0
out = 0
total = 0

random_list = list(random.sample(range(1, 11), 10))
print(random_list[0: 7])

# Tk 객체 인스턴스 생성
root = tk.Tk()

# text box 입력 박스 생성
text_box = tk.Entry(root)
text_box.pack()

# 클릭 버튼 생성
click_button = tk.Button(root, text='Click', command=func)
click_button.pack()

# 텍스트 출력 라벨 생성
result_label = tk.Label(root, text='')
result_label.pack()

root.mainloop()

