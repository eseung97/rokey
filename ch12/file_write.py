# f = open("C:/rokey/ch12/file1.txt", 'w')
# result = f.write('123')
# # print(result)
# result = f.write('hi')
# # print(result)
# f.close()

# f = open("C:/rokey/ch12/file1.txt", 'w')
f = open("C:/rokey/ch12/file1.txt", 'w', encoding="utf-8")
for i in range(1, 11):
    data = "%d번째 줄입니다. \n" % i
    f.write(data)
f.close()