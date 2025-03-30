from tkinter import Tk
from tkinter import Label

oroot = Tk()                # 생성
oroot.geometry("300x200")
olabel1 = Label(oroot, text="적색", bg="red", width=20)
olabel2 = Label(oroot, text="녹색", bg="green", width=30)
olabel3 = Label(oroot, text="파란색", bg="blue", width=40)

olabel1.pack()              # 배치
olabel2.pack()
olabel3.pack()
                            # 동작(이벤트)
oroot.mainloop()

