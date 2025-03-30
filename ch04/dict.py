my_dict1 = {}
print(my_dict1, type(my_dict1))

my_dict2 = {0:1}
print(my_dict2, type(my_dict2))

my_dict2 = {0:1, 1:-2, 2:3.14}
print(my_dict2, type(my_dict2))

my_dict3 = {'이름':'앨리스', '나이':10, '직업':['개발자','학생'], '메일수신동의여부': True}
print(my_dict3)
my_dict3['성별'] = '여성'
print(my_dict3)
my_dict3['나이'] = '28'
print(my_dict3)

print('---------')
clover = {'나이': 27, '직업': '학생'}
print(clover)
clover['번호'] = 206
print(clover)

print(clover['번호'])
clover['번호'] = 15
print(clover.get('번호'))

print('---------')
dic = {'apple': 'apple.com', '파이썬': 'python.org','마소':'microsoft.com'}

print(dic.items())
print(dic.keys())
print(dic.values())
