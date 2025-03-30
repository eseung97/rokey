# def hello():
#     print("hello there")

# def printPosition():
#     print(obtn.winfo_x())           # 현재 x 좌표 확인
#     print(obtn.winfo_y())           # 현재 y 좌표 확인


# from tkinter import *

# otk = Tk()      # 메인 윈도우 객체 생성
# otk.geometry("600x400+600+600")
# # obtn = Button(otk, text="click me", command=hello)
# obtn = Button(otk, text="printPosition", command=printPosition)
# obtn.pack()
# otk.mainloop()


def hello1():
    print("hello there 1")
def hello2():
    print("hello there 2")
def hello3():
    print("hello there 3")

from tkinter import *

otk = Tk()      # 메인 윈도우 객체 생성
otk.geometry("600x400+600+600")
obtn1 = Button(otk, text="PUSH1", command=hello1)
obtn2 = Button(otk, text="PUSH2", command=hello2)
obtn3 = Button(otk, text="PUSH3", command=hello3)
obtn1.pack()
obtn2.pack()
obtn3.pack()
otk.mainloop()