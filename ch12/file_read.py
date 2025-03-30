path = "C:/rokey/ch12/file1.txt"
f = open(path, 'r')
data = f.read()
print(data)
f.close()