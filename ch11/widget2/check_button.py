from tkinter import Tk
from tkinter import Button
from tkinter import Checkbutton
from tkinter import BooleanVar

oroot = Tk()
oroot.geometry("300x200")

coffee = {0:"아메리카노", 1:"라떼", 2:"카푸치노", 3:"에스프레소"}
check_value={}      #선택한 메뉴를 담을 자료형 생성

for i in range(len(coffee)):
    check_value[i] = BooleanVar()
    ocheckbutton = Checkbutton(oroot, text=coffee[i], variable=check_value[i])
    ocheckbutton.pack(anchor="w")

# check_value[0] = BooleanVar()
# ocheckbutton = Checkbutton(oroot, text="아메리카노", variable=check_value[0])
# ocheckbutton.pack()

# check_value[1] = BooleanVar()
# ocheckbutton = Checkbutton(oroot, text="라떼", variable=check_value[1])
# ocheckbutton.pack()

# check_value[2] = BooleanVar()
# ocheckbutton = Checkbutton(oroot, text="카푸치노", variable=check_value[2])
# ocheckbutton.pack()

# check_value[3] = BooleanVar()
# ocheckbutton = Checkbutton(oroot, text="에스프레소", variable=check_value[3])
# ocheckbutton.pack()






# 기능: 
def buy():
    print("주문한 커피 메뉴: ")

    for i in range(len(coffee)):
        if check_value[i].get() == True:        # 아메리카노 선택 여부(True/False)
            print(coffee[i])

    # if check_value[0].get() == True:        # 아메리카노 선택 여부(True/False)
    #     print(coffee[0])
    # if check_value[1].get() == True:        # 라떼 선택 여부(True/False)
    #     print("라떼")
    # if check_value[2].get() == True:        # 카푸치노 선택 여부(True/False)
    #     print("카푸치노")
    # if check_value[3].get() == True:        # 에스프레소 선택 여부(True/False)
    #     print("에스프레소")

obtn = Button(oroot, text="주문", command=buy)
obtn.pack(anchor="w")

oroot.mainloop()