a = [10, 11, 12, 13]
print(id(a))
print(id(a[0]))
print(id(a[1]))
print(id(a[2]))
a[1] = 21
print(id(a))
print(id(a[0]))
print(id(a[1]))
print(id(a[2]))
b = a
print(id(b))
print(id(b[0]))
print(id(b[1]))
print(id(b[2]))
b = [30, 31, 32, 33]
print(id(b))
print(id(b[0]))
print(id(b[1]))
print(id(b[2]))
print(id(b[3]))

print('------------')
def fk(cb):
    total=0
    for sb in range(0, 3, 1):
        total=total+cb[sb]
    cb[2]=total
    return cb
ca = [10,20,30]
print(ca)
cd=fk(ca)           # cb = ca : 얕은 복사(주소 참조)
print(ca)
print(cd)