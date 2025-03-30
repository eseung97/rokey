# 2. 연산자 사용 방식
# %s : 문자열
# %d : 정수
# %f : 실수
name = "홍길동"
age = 700
height = 191.3
# print("이름: %s"%(name))
print("이름: %s, 나이: %d, 신장: %f"%(name, age , height))

data = "%d번째 줄입니다\n"%(2)
print(data)

print('3-------------')

# 3. format() 메서드 사용 방식
# {}와 format() 사용해서 출력
print("이름: {}, 나이: {}, 신장: {}".format(name, age, height))

print('4-------------')

# 4. f.string 사용 방식
print(f"이름: {name}, 나이: {age}, 신장: {height}")