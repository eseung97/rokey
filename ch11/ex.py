from tkinter import *

window = Tk()
window.title("5반 전용 응원창")
window.geometry("300x100")

label = Label(window, text="오늘도 수고했어요, 5반!")
label.pack()

button = Button(window, text="눌러보세요!")
button.pack()

window.mainloop()