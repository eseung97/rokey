def simple_generator():
    yield 'a'
    yield 'b'
    yield 'c'

g = simple_generator()
print(g, type(g))

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

for i in g:
    print(i)

def mygen():
    for i in range(1, 1000):
        result = i * i
        yield result
gen = mygen()
print(next(gen))
print(next(gen))
print(next(gen))

print('-----------')
# 제너레이터 컴프리헨션
gen = (i*i for i in range(2,100, 2))
print(next(gen))
print(next(gen))
print(next(gen))
for val in gen:
    print(val)