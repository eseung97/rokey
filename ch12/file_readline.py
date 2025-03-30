path = "./ch12/file1.txt"
f = open(path, 'r')
line = f.readline()
print(line)
f.close()