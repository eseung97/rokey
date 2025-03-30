clovers = ('클로버1','하트2','클로버3')
print(clovers[1])
print(type(clovers))

print('--------------')
my_tuple1 = ()
print(my_tuple1)
print(my_tuple1, type(my_tuple1))

print('--------------')
my_tuple2 = (1, -2, 3.14)
print(my_tuple2)

my_tuple3 = '앨리스', 10, 1.0, 1.2
print(my_tuple3)

my_tuple1= (True, False)
print(my_tuple1)

print('--------------')
my_int = (1)
print(type(my_int))

my_tuple = (1,)
print(type(my_tuple))

print('--------------')
a = (1, 2, 3)
# a[0] = 7
print(type(a))
a= list(a)
print(type(a))
print(a, "a의 데이터형식은", type(a))
a[0] = 7
print(a)

print('--------------')
my_tuple4 = 1,
print(type(my_tuple4))