b = 0
print("b의 값은", b)
b = 1
print("b의 값은", b)

def scope_test():
    # global a
    a = 0
    a = a + 3
    print("scope_test() 함수 안의 a 값은", a)
    return a

a = 0
print("scope_test() 함수 밖의 a 값은", a)
a = scope_test()
print("scope_test() 함수 호출 후 a 값은", a)
