# 3. 위 data.txt 에 ‘11번째 줄입니다.’ 를 추가하는 코드를 만드세요
path = r'C:\rokey\ch15.5\data.txt'
mode = 'a'
with open(path, mode, encoding="utf-8") as f:
    f.write("11번째 줄입니다.")