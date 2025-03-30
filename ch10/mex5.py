# import mex1
# from mex1 import *
from mex1 import plus

# mex5.py를 메인 모듈로 실행했을 때
# mex1.py 하위 모듈로 동작한다.
# mex1.py에 있는 __name__ 은 mex1 출력됨

# print(__name__)

if __name__ == "__main__":
    value = plus(10,20)
    print(value)