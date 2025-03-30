a = [1,2,3]
# next(a)
# 'list' object is not an iterator

iter_a = iter(a)
# print(len(iter_a))      # 불가능
print(type(iter_a))

# next 함수
# print(next(iter_a))     # 1
# print(next(iter_a))     # 2
# print(next(iter_a))     # 3
# print(next(iter_a))   # StopIteration

for i in iter_a:
    print(i)
print('-----------')
for i in iter_a:
    print(i)

print(next(iter_a))     # StopIteration
