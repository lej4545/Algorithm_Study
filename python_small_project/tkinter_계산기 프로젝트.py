import tkinter as tk


def func(s):
    global equation
    equation += s
    display_label.config(text=equation)

def zero():
    global equation
    equation = ''
    display_label.config(text='0')

def calc():
    global equation
    result = eval(equation)
    display_label.config(text=result)

window = tk.Tk()
window.title("계산기")
window.geometry("400x210") #창 크기
window.resizable(False,False) #창 고정


display_label = tk.Label(window, text='')
display_label.pack()

sel = tk.StringVar()
equation = ''

b1 = tk.Button(window, text=1, command=lambda: func('1'))
b2 = tk.Button(window, text=2, command=lambda: func('2'))
b3 = tk.Button(window, text=3, command=lambda: func('3'))
b4 = tk.Button(window, text=4, command=lambda: func('4'))
b5 = tk.Button(window, text=5, command=lambda: func('5'))
b6 = tk.Button(window, text=6, command=lambda: func('6'))
b7 = tk.Button(window, text=7, command=lambda: func('7'))
b8 = tk.Button(window, text=8, command=lambda: func('8'))
b9 = tk.Button(window, text=9, command=lambda: func('9'))
bc = tk.Button(window, text='C', command=zero)
b0 = tk.Button(window, text=0, command=lambda: func('0'))
bm = tk.Button(window, text='=', command=calc)
p1 = tk.Button(window, text='+', command=lambda: func('+'))
p2 = tk.Button(window, text='-', command=lambda: func('-'))
p3 = tk.Button(window, text='*', command=lambda: func('*'))
p4 = tk.Button(window, text='/', command=lambda: func('/'))

b1.place(x=50, y=50,width=50, height=25)
b2.place(x=130, y=50, width=50, height=25)
b3.place(x=210, y=50, width=50, height=25)
b4.place(x=50, y=90, width=50, height=25)
b5.place(x=130, y=90, width=50, height=25)
b6.place(x=210, y=90, width=50, height=25)
b7.place(x=50, y=130, width=50, height=25)
b8.place(x=130, y=130, width=50, height=25)
b9.place(x=210, y=130, width=50, height=25)
bc.place(x=50, y=170, width=50, height=25)
b0.place(x=130, y=170, width=50, height=25)
bm.place(x=210, y=170, width=50, height=25)
p1.place(x=290, y=50, width=50, height=25)
p2.place(x=290, y=90, width=50, height=25)
p3.place(x=290, y=130, width=50, height=25)
p4.place(x=290, y=170, width=50, height=25)

window.mainloop()