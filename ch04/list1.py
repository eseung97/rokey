candy0 = '딸기맛'
candy1 = '레몬맛'
candy2 = '수박맛'
candy3 = '박하맛'
candy4 = '우유맛'

print(candy0)

print('--------------')
candies = ['딸기맛', '레몬맛', '수박맛', '박하맛', '우유맛']
print(candies)

print('--------------')
lista = ['list', 1, 0.7, True]
print(lista)

print('--------------')
ca = [10,11,21]
print(ca)
print(ca[0])
print(ca[1])
print(ca[2])
# print(ca[3])

print('--------------')
a= [1,2,3,4,5]
a[2] = 30
print(a)
a[3] = 40
print(a)
a[4] = 'hi'
print(a)
a[1] = False
print(a)
a[0] = [0, 3.14]
print(a)

print('--------------')
listc = []
print(listc)
listc.append(300)
print(listc)
listc.append("파이썬")
print(listc)
listc.append(3.7)
print(listc)
listc.append(True)
print(listc)
listc.append([1.1, 2.2])
print(listc)
print(listc[4][0])
print(listc[4][1])

print('--------------')
clovers = ['클로버1', '클로버2', '클로버3']
print(clovers[1])
del clovers[1]
print(clovers)
print(clovers[1])

print('--------------')
# 리스트에 해당 값이 여러번 등장하면 앞에 값이 우선 삭제
list_class = [1,2,3,4,5]
list_class.append(6)
print(list_class)
list_class.remove(3)
print(list_class)
list_class.append(7)
print(list_class)
list_class.append(6)
print(list_class)
list_class.remove(6)
print(list_class)

print('--------------')
list_fruits = ['감', '배','사과']
print(list_fruits[2])
list_fruits.insert(2, '복숭아')
print(list_fruits)
print(list_fruits[3])

print('--------------')
print(list_fruits)
list_fruits.extend(['귤','망고', '파인애플', '딸기', '수박', '패션후르츠'])
print(list_fruits)
list_fruits.extend([1,2,3,4,5])
print(list_fruits)