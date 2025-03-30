from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import PhotoImage

oroot = Tk()
oroot.geometry("189x50")

# img1 = PhotoImage(file="C:/rokey/ch11/widget2/logo.png")
img1 = PhotoImage(file="./ch11/widget2/logo.png")

img_label = Label(oroot, image=img1)
img_label.place(x=0, y=0)

obtn1 = Button(oroot, text="PUSH1")
obtn2 = Button(oroot, text="PUSH2")
obtn3 = Button(oroot, text="PUSH3")

obtn1.place(x=10, y=60)
obtn2.place(x=140, y=60)
obtn3.place(x=80, y=10)

oroot.mainloop()