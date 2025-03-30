# 리스트 컴프리헨션
#  [expression for item in iterable if condition]

numbers = [1,2,3,4]
squared = [x**2 for x in numbers]
print(squared)

numbers = [1,2,3,4]
squared = [x**2 for x in numbers if x % 2 ==0]
print(squared)


# 딕셔너리 컴프리헨션
# {key_expression: value_expression for item in iterable if condition}

squared_dict = {x:x**2 for x in range(5)}
print(squared_dict)

squared_dict = {x:x**2 for x in range(10) if x % 2 == 0}
print(squared_dict)