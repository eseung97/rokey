ca = [10, 11]
print("ca[0]의 값은", ca[0], "ca[1]의 값은", ca[1])
temp = ca[0]
ca[0] = ca[1]
ca[1] = temp
print("ca[0]의 값은", ca[0], "ca[1]의 값은", ca[1])

print('----------')
def funca(na, nb):
    temp = na
    na = nb
    nb = temp

ca = [10, 11]
print("ca[0]의 값은", ca[0], "ca[1]의 값은", ca[1])
funca(ca[0], ca[1])
print("ca[0]의 값은", ca[0], "ca[1]의 값은", ca[1])

print('----------')
ca = [10, 11]
cb = ca
print("리스트ca 값은", ca)
print("리스트ca 주소", id(ca))
print("리스트cb 값은", cb)
print("리스트cb 주소", id(cb))

print('----------')
temp = cb[0]
cb[0] = cb[1]
cb[1] = temp
print("리스트ca 값은", ca)
print("리스트cb 값은", cb)
print("ca[0]:", id(ca[0]))
print("cb[0]:", id(cb[0]))

print('----------')
def funca(cb):
    print("리스트cb 주소", id(cb))
    temp = cb[0]
    cb[0] = cb[1]
    cb[1] = temp
ca = [10, 11]
print("ca[0]의 값은", ca[0], "ca[1]의 값은", ca[1])
print("리스트ca 주소", id(ca))
funca(ca)           # cb = ca
print("ca[0]의 값은", ca[0], "ca[1]의 값은", ca[1])
