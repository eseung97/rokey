# Entry: 입력 상자
from tkinter import Tk
from tkinter import Entry
from tkinter import StringVar
from tkinter import Label



oroot = Tk()                # 생성
oroot.geometry("300x200")
ostring = StringVar()       # 문자열변수 생성
# 입력된 텍스트가 ostring 변수와 연결 생성
oentry = Entry(oroot, textvariable=ostring)
oentry.pack()
olabel = Label(oroot, textvariable=ostring)
olabel.pack()
oroot.mainloop()