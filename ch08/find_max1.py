su = [5, 4, 7, 10, 6]

def fmax(su):
    return max

print(fmax(su))

print('-----------')

def fmax(a,b,c,d,e):
    max = a
    if max < b:
        max = b
    if max < c:
        max = c
    if max < d:
        max = d
    if max < e:
        max = e
    return max

# a = su[0]
# b = su[1]
# c = su[2]
# d = su[3]
# e = su[4]
# fmax(a,b,c,d,e)
max = fmax(su[0],su[1],su[2],su[3],su[4])
print(max)

print('-----------')
def fmax(a,b,c,d,e):
    fu = [a,b,c,d,e]
    max=fu[0]
    if max < fu[1]:
        max = fu[1]
    if max < fu[2]:
        max = fu[2]
    if max < fu[3]:
        max = fu[3]
    if max < fu[4]:
        max = fu[4]
    return max

# a = su[0]
# b = su[1]
# c = su[2]
# d = su[3]
# e = su[4]
# fmax(a,b,c,d,e)
max = fmax(su[0],su[1],su[2],su[3],su[4])
print(max)

print('-----------')
def fmax(a,b,c,d,e):
    fu = [a,b,c,d,e]
    max=fu[0]
    for i in range(1, 5, 1):
        if max < fu[i]:
            max = fu[i]
    return max

max = fmax(su[0],su[1],su[2],su[3],su[4])
print(max)

print('-----------')
def fmax(a,b,c,d,e):
    fu = [a,b,c,d,e]
    max=fu[0]
    for sfu in fu:
        if max <sfu:
            max = sfu
    return max

max = fmax(su[0],su[1],su[2],su[3],su[4])
print(max)

print('-----------')
def fmax(fu):
    max=fu[0]
    for sfu in fu:
        if max <sfu:
            max = sfu
    return max

max = fmax(su)
print(max)

print('-----------')
def fmax(fu):
    max=fu[0]
    for i in range(1,5,1):
        if max < fu[i]:
            max = fu[i]
    return max

max = fmax(su)
print(max)