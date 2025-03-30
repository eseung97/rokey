muna = "python"
print(muna[0])
print(muna[1])
print(muna[2])
print(type(muna))
try:
    muna[0] = 'k'
except TypeError as e:
    print(type(e), e)

munb = ["python"]
print(munb[0])
print(type(munb))

munc = ["p","y","t","h","o","n"]
print(munc[0])
print(munc[1])
print(munc[2])
print(type(munc))
munc[0] = 'k'
print(munc)

for i in range(0,6,1):
    print(munc[i])

for i in munc:
    print(i)

length = len(munc)
print(length)

for i in range(0, length, 1):
    print(munc[i])

print('-------------')

print(ord("a"))
print(chr(97))
print(ord('가'))
print('-------------')
ma = "chatGPT" + "를 활용한 python"
print(ma)