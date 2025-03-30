# 10. 1부터 n까지의 숫자의 제곱을 생성하는 제너레이터 함수를 작성하세요.
def square_generator(n):
    for i in range(1, n + 1):  
        yield i ** 2 

n = int(input("n을 입력하세요: "))  

for square in square_generator(n):  
    print(square)  
