path = './ch12/file/계좌1.txt'
mode = "r"

with open(path, mode, encoding="utf-8") as f:
    lines = f.readlines()

    account_dict = {}
    for line in lines:
        lineList = line.split(" ")
        print(lineList[0])       # 예금주
        print(lineList[1].strip())       # 계좌번호

        account_dict[lineList[0]] = lineList[1].strip()
    print(account_dict)