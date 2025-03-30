import tkinter as tk
root = tk.Tk()
root.geometry("200x200")
# 옵션 리스트
option_list = ['Option 1', 'Option 2', 'Option 3']

# 선택한 옵션을 저장할 변수
selected_option = tk.StringVar()

# 초기 선택 옵션
selected_option.set(option_list[0])

# OptionMenu 생성
option_menu = tk.OptionMenu(root, selected_option,*option_list)
# option_menu = tk.OptionMenu(root, selected_option,option_list)

option_menu.pack()
root.mainloop()