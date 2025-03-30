a = int(input("아무 숫자를 입력하세요: "))
def zeroDevide(x):
        x = x / 0
        return x
try:
    zeroDevide(a)
except ZeroDivisionError as e:
    print("0으로 나눌 수 없습니다.")