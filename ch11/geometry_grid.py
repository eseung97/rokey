import tkinter
oroot = tkinter.Tk()
oroot.geometry("200x100")
obtn1 = tkinter.Button(oroot, text="PUSH1")
obtn2 = tkinter.Button(oroot, text="PUSH2")
obtn3 = tkinter.Button(oroot, text="PUSH3")
obtn1.place(x=10, y=60)
obtn2.place(x=140, y=60)
obtn3.place(x=80, y=10)

oroot.mainloop()
