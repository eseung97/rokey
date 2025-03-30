x = 10
def fadd(num):
    b=x+num
    print("변수 x값은", x)
    print("변수 b값은", b)
fadd(10)


print('---------')
x = 10
def fadd(num):
    # x=x+num
    print("변수 x값은", x)
fadd(10)


print('---------')
x = 10
def fadd(num):
    global x
    x=x+num
    print("변수 x값은", x)
fadd(10)


print('---------')
# def print_lower_price(price = 0):
#     discounted_price = int(price * 0.9 / 10 )* 10
#     print("할인된 가격", discounted_price,"(원)")
#     return discounted_price

# price = int(input('현재 가격을 입력:'))

# discounted_price = print_lower_price(price)


print('---------')
def func1(num):
    return num + 4

a = func1(10)
b = func1(a)
c = func1(b)
print(c)

print('---------')
x = 10  

def change():  
    x = 20  
    print("함수 내부:", x)  

change()  
print("함수 외부:", x)  