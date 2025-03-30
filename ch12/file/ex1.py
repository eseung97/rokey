path = './ch12/file/계좌1.txt'
mode = "w"

f = open(path, mode, encoding="utf-8")

f.write('김삿갓 597-89-000089\n')
f.write('이수근 343-64-000064\n')
f.write('박혁거세 136-97-000097')

f.close()
