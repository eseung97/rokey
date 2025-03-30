square = lambda x : x**2

# map 함수
numbers = [1,2,3]
squared_num = map(square, numbers)
print(list(squared_num))

numbers = [1,2,3]
squared_num = map(square, numbers)
for i in squared_num:
    print(i)

print('-------------')

# 소수점 첫쨰자리까지 표현된 숫자 => 정수
numbers1 = (1.1, 2.1, 3.1, 4.1, 5.1)
floatToInt = lambda x:int(x)
for i in range(5):
    print(floatToInt(numbers1[i]))

print('-------------')

intNums = map(lambda x:int(x), numbers1)
for num in intNums:
    print(num)

# num1리스트와 num2리스트를 각 인덱스별로 더하시오
num1 = [11,12,13]
num2 = [21,22,23]

addNums = map(lambda x,y: x+y, num1, num2)
print(list(addNums))

