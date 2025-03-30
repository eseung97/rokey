# 1. tkinter를 사용하여 간단한 GUI 프로그램을 작성하세요. 
# 프로그램의 요구사항은 다음과 같습니다.
# -Tk 윈도우를 생성하고 제목을 "간단한 Tkinter 앱"으로 설정합니다.
# -버튼을 추가하고, 클릭 시 "버튼이 클릭되었습니다!"라는 메시지를 출력하도록 설정합니다.

import tkinter
otk = tkinter.Tk()
otk.title("간단한 Tkinter 앱")
otk.geometry("300x200")

def click():
    print("버튼이 클릭되었습니다!")

obtn = tkinter.Button(otk, text = "click", command=click)
obtn.pack()

otk.mainloop()
