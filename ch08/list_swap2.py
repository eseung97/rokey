a = [10, 11, 12, 13]
print("리스트 a 값", a)

a[1] = 21
print("리스트 a 값", a)

b = a
print("리스트 b 값", b)
print("리스트 b 주소", id(b))

b = [30, 31, 32, 33]
print("리스트 b 값", b)
print("리스트 b 주소", id(b))

c = [10, 11, 12, 13]
print("리스트 a 주소", id(a))
print("리스트 c 주소", id(c))

# 주소 같음 => 동일한 데이터를 참조
aa = 10
bb = 10
print("리스트 aa 주소", id(aa))
print("리스트 bb 주소", id(bb))
