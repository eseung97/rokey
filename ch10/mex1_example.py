import mex1

# from 모듈명 import 클래스명
# from 모듈명 import 함수명
from mex1 import Cvalue
from mex1 import plus

# class
p2 = mex1.Cvalue()
print(p2.lista)
p2.add(11)
p2.add(22)
p2.add(33)
p2.fprint()

#function
sum = mex1.plus(10,20)
print(sum)

#variable
mex1.p1.fprint()