# 2. 다음의 작업을 수행하는 파이썬 프로그램을 작성하세요.

# -data.txt라는 파일을 쓰기(w 모드)로 열고, 1부터 10까지의 숫자를 "n번째 줄입니다." 형식으로 파일에 저장합니다.
# -파일을 읽기(r 모드)로 열고 모든 내용을 출력합니다.

path = r'C:\rokey\ch15.5\data.txt'
mode = 'w'
with open(path, mode, encoding="utf-8") as f:
    for i in range(1,11):
        data = "%d번째 줄입니다.\n" % i
        f.write(data)

mode = 'r'
with open(path, mode, encoding="utf-8") as f:
    line = f.read()
    print(line)