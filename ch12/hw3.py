path = "C:/rokey/ch12/pizza_file1.txt"
mode = "r"
with open(path, mode, encoding="utf-8") as f:
    lines = f.readlines()
    pizzas = []
    for line in lines:
        lineList = line.split(" ")
        pizzas.append(lineList[0])
    print(pizzas)