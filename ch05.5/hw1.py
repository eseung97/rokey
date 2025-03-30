# # 2번
# a = int(input("첫번째 숫자를 입력하세요"))
# b = int(input("두번째 숫자를 입력하세요"))

# print("덧셈 결과: ", a + b)
# print("뺄셈 결과: ", a - b)
# print("곱셈 결과: ", a * b)
# print("나눗셈 결과: ", a / b)



# # 3번
# a = 3.14
# b = True
# c = False



# print(type(a))
# print(type(b))
# print(type(c))



# 4번
# score = int(input("점수를 입력하세요: "))
# if score >= 90:
#     print("당신은 A학점입니다." )
# elif score >= 80:
#     print("당신은 B학점입니다." )
# elif score >= 70:
#     print("당신은 C학점입니다." )
# else:
#     print("당신은 F학점입니다." )



# 5번
# numbers = [1, 2, 3, 4, 5]
# print(numbers)



# 6번
# age = int(input("사용자의 나이를 입력하세요: "))
# if 20 <= age <= 60:
#     print("적정 연령대입니다.")
# else:
#     print("적정 연령대가 아닙니다.")



# 7번
# rows = [1, 5, 9, 13, 9, 5, 1]  
# for stars in rows:
#     print(" " * ((13 - stars) // 2) + "*" * stars)



# 8번
# fruits = ['바나나', '파인애플', '복숭아', '사과', '포도']
# for i in fruits:
#     if i == '사과':
#         print(i,"를 찾았습니다.")
#     else:
#         print(i)


rows = 4
for i in range(rows):
    print(' ' * (rows- i -1) + '*' * (2 * i + 1))
for i in range(rows- 2, -1, -1):
    print(' ' * (rows- i -1) + '*' * (2 * i + 1))
# 0,1,2,3