print('try_except2')

try:
    path = r'ch13\exception\myfile.txt'
    # FileNotFoundError
    f = open(path, 'a') # mode 기본값이 'r'
    # f = open(path, 'w')
    # f.write("Hello")

    # io.UnsupportedOperation
    s = f.readline()

    # ValueError
    i = int(s.strip())

except (RuntimeError, TypeError, NameError):
    print("RuntimeError, TypeError, NameError 중 하나의 예외 처리!")
except OSError as err:
    print("OS error:", err)
    print(type(err))
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
except ValueError:
    print("정수형으로 변환할 수 없습니다.")
except Exception as e:
    print("앞서 처리한 예외가 아닌 다른 예외 발생시 처리!")
    print(e, type(e))

print('program exit')
