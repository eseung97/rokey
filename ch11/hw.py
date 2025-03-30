from tkinter import *

window = Tk()
window.title("조각 피자 주문 프로그램")
window.geometry("400x300")

pizza = {0:("치즈 피자",3200), 1:("콤비네이션 피자 ", 3500), 2:("불고기 피자", 3600)}
check_value={}      #선택한 메뉴를 담을 자료형 생성

label = Label(window, text="피자")
label.pack()

for i in range(len(pizza)):
    check_value[i] = BooleanVar()
    checkbutton = Checkbutton(window, text=f"{pizza[i][0]} ({pizza[i][1]}원)", variable=check_value[i])
    checkbutton.pack(anchor="w")

def buy():
    order_text = "주문내역:\n"
    total_price = 0

    for i in range(len(pizza)):
        if check_value[i].get():  # 체크된 항목이면
            order_text += f"- {pizza[i][0]} ({pizza[i][1]}원)\n"
            total_price += pizza[i][1]

    # 주문 내역 & 총 가격 업데이트S
    order_label.config(text=order_text)
    total_label.config(text=f"총 가격: {total_price}원")

Button(window, text="주문", command=buy).pack()

# 주문 내역을 출력할 Label
order_label = Label(window, text="주문내역:")
order_label.pack()

# 총 가격을 출력할 Label
total_label = Label(window, text="총 가격: 0원")
total_label.pack()

window.mainloop()