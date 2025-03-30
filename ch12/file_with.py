path = "./ch12/file2.txt"
mode = "w"
with open(path, mode) as f:
    f.write("No pain, no gain.")


mode = "r"
with open(path, mode) as f:
    data = f.read()
print(data)