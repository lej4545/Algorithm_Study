import tkinter as tk

def calc():
    a = e_up.get()
    b = rbvar.get()
    c = e_down.get()
    if c == '0' and b == '/':
        result = '0으로 나눌 수 없습니다.'
    else:
        result = format(eval(a + b + c), ".2f")

    result_label.config(text=result)

# Tk 객체 인스턴스 생성
root = tk.Tk()

# 첫번째 인자 입력 박스
e_up = tk.Entry(root)
e_up.pack()

# 두번째 인자 입력 박스
e_down = tk.Entry(root)
e_down.pack()

# Radiobutton에서 사용되는 변수
rbvar = tk.StringVar(root, 0)
radios = []
operator = ['+', '-', '*', '/']

# rb 버튼 생성
for idx in range(4):
    rb = tk.Radiobutton(root, text='Button %s'%operator[idx], variable=rbvar, value=operator[idx], indicatoron=1)
    radios.append(rb)
    rb.pack()

# # +버튼
# plus_button = tk.Radiobutton(root, text='Button +', variable=rbvar, value='+', indicatoron=1)
# plus_button.pack()
#
# # -버튼
# minus_button = tk.Radiobutton(root, text='Button -', variable=rbvar, value='-', indicatoron=1)
# minus_button.pack()
#
# # * 버튼
# multi_button = tk.Radiobutton(root, text='Button *', variable=rbvar, value='*', indicatoron=1)
# multi_button.pack()
#
# # / 버튼
# divide_button = tk.Radiobutton(root, text='Button /', variable=rbvar, value='/', indicatoron=1)
# divide_button.pack()

# 버튼을 누르면 calc가 실행되는 함수
result_bt = tk.Button(root, text='Result', command=calc)
result_bt.pack()

# calc에서 계산된 값을 출력할 함수
result_label = tk.Label(root, text='결과 표시창', underline=3)
result_label.pack()

root.mainloop()
