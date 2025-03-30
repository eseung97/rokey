# for 변수 in 리스트:
#     코드블록

for num in [0,1,2]:
    print('hi', num)

print('--------------')
characters = ['엘리스','도도새','3월토끼']
for character in characters:
    print(character)

print('--------------')
for letter in '체셔고양이':
    print(letter)

print('--------------')
for letter in '체셔고양이':
    pass

print('--------------')
nums = [1,2,3]
for num in nums:
    print(num)
print(nums)

print('--------------')
nums = [1,2,3]
for num in nums:
    print(num)
    print(nums)

print('--------------')
print(list(range(10)))
print(list(range(1,3)))
print(list(range(2,9,2)))
print(list(range(1,101,5)))
print(list(range(2,11,-1)))
print(list(range(11,2,-1)))
# print(list(range(2,5,0.1)))

print('--------------')
for num in range(3):
    print(num)
print('--------------')
for num in range(0,3):
    print(num)
print('--------------')
for num in range(1,9,2):
    print(num)

print('--------------')
for j in range(5):
    for i in range(10):
        print("*", end = "")
    print()

# 이스케이프 문자
# \n new line
# \t tab
# \r return