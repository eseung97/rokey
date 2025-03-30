
path = "C:/rokey/ch12/file1.txt"
# f = open(path, 'a')
f = open(path, 'a', encoding="utf-8")
for i in range(11, 21):
    data = "%d번째 줄입니다. \n" % i
    f.write(data)
f.close()