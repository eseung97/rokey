from tkinter import *

def order():
    print('주문하세요')

otk = Tk()
otk.geometry("300x200")

mlabel = Label(otk, text="시작레이블")
mlabel.pack(side='top')

obtn = Button(otk, text="주문", command=order)
obtn.pack(side='bottom')

otk.mainloop()