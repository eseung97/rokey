def my_func():
    print('토끼야 안녕!')

my_func()
my_func()
my_func()

print('----------')
def funca(na,nb):
    nc = na + nb 
    print(na, "+", nb, "=", nc)

funca(10,20)

print('----------')
def add(num1, num2):
    return num1 + num2
print(add(2,3))

print('----------')
def subtract(num1, num2):
    return num1 - num2
print(subtract(2,3))

print('----------')
def funca(pa, pb):
    nc = pa + pb
    return nc

na = 10
nb = 11

nd = funca(na, nb)
print(na, "+", nb, "=", nd)

print('----------')
def myabs(arg):
    if(arg < 0):
        result = arg * -1
    else:
        result = arg
        return result
    
print(myabs(10))

print('-----------')
def freturn(a, b, c, d):
    dica = {a:b, c:d}
    return dica

a ="이름"
b = "이나겸"
c = "학점"
d = 4.3

dicb = freturn(a, b, c, d)
print(dicb)
print(type(dicb))

print('-----------')
def fplusminus(arg):
    if arg > 0:
        return "plus"
    elif arg < 0:
        return "minus"
    else:
        return "zero"
stra = fplusminus(0)
print(stra)