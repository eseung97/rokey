print("raise>_exception")

try:
    print("start")
    print("good morning")
    raise NameError("Hi there!")
    print("good afternoon")
    print("good evening")
except NameError as e:
    print("예외가 발생했습니다!")
    print(e)

print("program exception")
