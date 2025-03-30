# score.py

score = 90      #초기화
score = 79      #재할당
score = 69      #재할당
score = 59      #재할당

if score > 80:
    print('합격입니다.')
elif score > 70:
    print('합격 1차 대기 입니다.')
elif score > 60:
    print('합격 2차 대기 입니다.')
else:
    print('불합격입니다.')

print('-------------')
# if score > 80:
#     print('합격입니다.')
# if score > 70:
#     print('합격 대기 입니다.')
# else:
#     print('불합격입니다.')

print('-------------')
# # 1. if 문
# if 조건식:
#     코드블록(어떤 명령이든 모두 가능)

# # 2. if-else 문
# if 조건식:
#     코드블록
# else:
#     코드블록

# # 3. if-elif-else 문 (elif 문 여러개 사용 가능)
# if 조건식:
#     코드블록
# elif 조건식2:
#     코드블록
# else:
#     코드블록

# # 4. if-elif 문
# if 조건식:
#     코드블록
# elif 조건식2:
#     코드블록

# # 5. 중첩된 if 문
# if 조건식1:
#     코드블록1
#     if 조건식2:
#         코드블록3
#     코드블록2

# if 조건식1:
#     코드블록1

#     if 조건식2:
#         코드블록3

#     else:
#         코드블록
#         if 조건식4:
#             코드블록5
#     코드블록2
# elif 조건식3:
#     코드블록4

na = 21
if na % 2==0:
    print(na,"짝수")
else:
    print(na, "홀수")
print("if 문 종료됨")