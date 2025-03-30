from tkinter import Tk
from tkinter import Button
from tkinter import IntVar
from tkinter import Radiobutton

oroot = Tk()            # 메인윈도우 객체 생성
oroot.geometry("200x200")
radio_value = IntVar()  # 정수형 변수 생성
# radio_value.set(2)      # 정수값 설정
radio_value.set(-1)      # 아무것도 선택 안되도록 설정하는 방법
lunch = {0:"A런치", 1:"B런치", 2:"C런치", 5:"D런치"}

# radio_value => 어떤 버튼에 선택되어 있는지 저장할 변수
# variable => 클릭된버튼의 정보를 저장할 변수명 설정
# value => radio_value에 저장될 데이터를 지정하는 인수
orb1 = Radiobutton(oroot, text=lunch[0], variable=radio_value,value=0)
orb2 = Radiobutton(oroot, text=lunch[1], variable=radio_value,value=1)
orb3 = Radiobutton(oroot, text=lunch[2], variable=radio_value,value=2)
orb4 = Radiobutton(oroot, text=lunch[5], variable=radio_value,value=5)
orb1.pack()
orb2.pack()
orb3.pack()
orb4.pack()

# 기능: 선택된 라디오버튼의 값을 변수로 가져와 출력
def buy():
    value = radio_value.get()
    print(lunch[value])

obtn = Button(oroot, text="주문", command=buy)
obtn.pack()

oroot.mainloop()