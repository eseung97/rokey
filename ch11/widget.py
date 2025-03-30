# import tkinter
# otk = tkinter.Tk()      # 메인 윈도우 객체 생성
# obtn = tkinter.Button(otk, text="click")
# obtn.pack()
# otk.mainloop()

print('--------------')

# from tkinter import Tk
# from tkinter import Button

# otk = Tk()      # 메인 윈도우 객체 생성
# obtn = Button(otk, text="click")
# obtn.pack()
# otk.mainloop()

print('--------------')

import tkinter
otk = tkinter.Tk()      # 메인 윈도우 객체 생성
# otk.geometry("100x150")
# otk.geometry("100x150+400+400")
otk.geometry("200x150+600+600")

obtn = tkinter.Button(otk, text="click")
obtn.pack()
otk.mainloop()