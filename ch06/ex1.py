# def draw_stars(num):
#     print('*' * num)

# draw_stars(3)
# draw_stars(2)
# draw_stars(1)

# print('----------')
# def fadd(num1, num2):
#     return num1 + num2

# print('----------')
# def fsub(num1, num2):
#     return num1 - num2

# print('----------')
# def fmul(num1, num2):
#     return num1 * num2

# print('----------')
# def fdiv(num1, num2):
#     return num1 / num2

# na = float(input("첫 번째 값을 입력하시오.: "))
# nb = float(input("두 번째 값을 입력하시오.: "))

# # na = 100
# # nb = 3

# nc = fadd(na,nb)
# print(na, "+", nb, "=", nc)
# nc = fsub(na,nb)
# print(na, "-", nb, "=", nc)
# nc = fmul(na,nb)
# print(na, "*", nb, "=", nc)
# nc = fdiv(na,nb)
# print(na, "/", nb, "=", nc)

# print('-------------')
# sta = "python example"
# def string_length(stb):
#     count = 0
#     for chara in stb:
#         count += 1
#     return count
# lena = string_length(sta)
# print(lena)

# print('-------------')
# def fdiv(num1, num2):
#     if num2 == 0:
#         # print('0으로는 나눌 수 없다.')
#         return '0으로 나눌 수 없다.'
#     else:
#         return num1 / num2

# na = float(input("첫 번째 값을 입력하시오.: "))
# nb = float(input("두 번째 값을 입력하시오.: "))

# nc = fdiv(na,nb)
# print(na, "/", nb, "=", nc)

# def get_teacher(class_num):
#     # if my_class == 1:
#     #     return '김려은'
#     # elif my_class == 2:
#     #     return '황지수'
#     # elif my_class == 3:
#     #     return '이수열'
#     # elif my_class == 4:
#     #     return '이용욱'
#     # elif my_class == 5:
#     #     return '하송미'
#     def get_teacher(class_num):
#         if class_num == 1:
#             return "김려은"
#         elif class_num == 2:
#             return "황지수"
#         elif class_num == 3:
#             return "이수열"
#         elif class_num == 4:
#             return "이용욱"
#         elif class_num == 5:
#             return "하송미"
#         else:
#             return "반은 1반부터 5반까지 있습니다"
# # 예시 실행
# my_class = 5
# print(f"{my_class}반 담임은 {get_teacher(my_class)} 선생님입니다.")

def multiple(num):
    sum = 0

    for n in range(1,101):
        if n % num == 0:
            sum += n
    return sum

num = int(input("1~9까지 정수 중 1개 입력:"))
sum = multiple(num)
print(sum)


