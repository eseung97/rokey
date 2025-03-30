na = 10
nb = 11
print("na 값은", na, "nb 값은", nb)
temp = na

na = nb
nb = temp
print("na 값은", na, "nb 값은", nb)

print('-----------')
def funca(pa,pb):
    temp = pa
    pa = pb
    pb = temp
    return pa, pb

na = 10
nb = 11
print("na 값은", na, "nb 값은", nb)
na, nb = funca(na, nb)
print("na 값은", na, "nb 값은", nb)

import keyword
print(keyword.kwlist)