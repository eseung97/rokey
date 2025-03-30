path = "C:/rokey/ch12/pizza_file1.txt"
mode = "r"
with open(path,mode,encoding='utf-8') as f:
    data = f.read()
    print(data)

    