num = 0
while num < 3:
    print('안녕 거북이', num)
    # num = num + 1
    num += 1

print('----------')

# while True:
#     print('ctrl+c를 누르세요')

stra = "파이썬"
strb = "프로그래밍"
# stra = stra + strb
stra += " " + strb
print(stra)

print('----------')
count = 0
while count < 3:
    # count = count + 1
    count += 1

    if count == 2:
        continue
    print(count)
print('반복문이 종료 되었습니다.')

print('----------')
count = 0
while count < 3:
    count = count + 1
    if count == 2:
        break
    print(count)
print('반복문이 종료 되었습니다.')

print('----------')
count = 0
while count < 3:
    count += 1
    for num in [0,1,2]:
        if num == 1:
            continue
        print(num)
    print(count)
print('반복문이 종료 되었습니다.')
