# 6번
# numbers = [1, 2, 3, 4, 5]
# i = iter(numbers)
# for a in i:
#     print(a)


# 7번
# fruits = ["apple", "banana", "cherry"]
# iter_fruits = iter(fruits)
# try:
#     for i in range(5):
#         print(next(iter_fruits))
# except StopIteration:
#     print('반환할 값이 없습니다')


# 8번
# gen = [i**2 for i in range(10)]
# print(gen)


# 9번
# gen = [i for i in range(11) if i % 2 == 0]
# print(gen)


# 10번
# class MyRange:
#     def __init__(self, start, stop, step=1):
#         self.start = start  
#         self.stop = stop    
#         self.step = step    
#         self.current = start  # 현재 위치를 저장할 변수

#     def __iter__(self):
#         return self  # 자기 자신을 반환 (이터레이터 객체)

#     def __next__(self):
#         if (self.step > 0 and self.current >= self.stop) or (self.step < 0 and self.current <= self.stop):
#             raise StopIteration  # 범위를 벗어나면 종료
        
#         value = self.current  # 현재 값을 저장
#         self.current += self.step  # 다음 값으로 이동
#         return value  # 현재 값 반환


# for num in MyRange(1, 10, 2): 
#     print(num)  

# print("---")

# for num in MyRange(10, 1, -3):  
#     print(num)  


# 연습 문제

# 다음 리스트를 이터레이터로 변환하고 동작을 확인하시오.
# • food = ["김밥", "만두", "양념치킨", "족발", "피자", "쫄면", "라면"]
# food = ["김밥", "만두", "양념치킨", "족발", "피자", "쫄면", "라면"]
# i = iter(food)
# for a in i:
#     print(a)


# 파일을 다음과 같이 생성 후, 파일에서 한 줄씩 읽는 제너레이터를 생성하고
# 사용하시오.
# def write_file(file_path):
# with open(file_path, 'w') as file:
# file.write(data)

file_path = r'C:\rokey\ch15\data.txt'

# 🔹 1. 파일 생성 함수
def write_file(file_path):
    data = """Hello, World!
This is a test file.
Python is great for file handling.
Enjoy coding!"""
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(data)  # 파일에 데이터 쓰기

# 🔹 2. 파일에서 한 줄씩 읽는 제너레이터
def read_file_line_by_line(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:  # 파일을 한 줄씩 읽음
            yield line.strip()  # 공백 제거 후 반환

# 🔥 실행
write_file(file_path)  # 파일 생성

# 🔹 제너레이터 사용
for line in read_file_line_by_line(file_path):
    print(line)  # 한 줄씩 출력

