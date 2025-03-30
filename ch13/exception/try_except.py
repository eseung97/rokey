# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops! That was no valid number. Try again")

# try-except-finally 구문
# try 실행 후 동작
# except 실행한 후 동작
# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops! That was no valid number. Try again")
#     finally:
#         print("예외 처리 후 실행할 프로그램 작성")


try:
    path = r'ch13\exception\myfile.txt'
    f = open(path)
    s = f.readline()
    i = int(s.strip())
except Exception as e:
    print("앞서 처리한 예외가 아닌 다른 예외 발생시 처리!")
    print(e, type(e))
else:
    print("예외가 발생하지 않아 except절을 실행하지 않는 경우, 동작")
finally:
    print("예외 처리 후 실행할 프로그램 작성")              