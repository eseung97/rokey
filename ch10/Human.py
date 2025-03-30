class Human:
    eyes = 2
    nose = 1
    mouth = 1

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def introduce(self):
        print(f"이름:{self.name}")
        print(f"나이:{self.age}")

    def eat(self):
        print("먹다")
    
    def sleep(self):
        print("자다")
    
    def talk(self):
        print("말하다")

class Human2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def draw(self):
        print("그리다")

# 여러 부모 클래스 상속 가능 (다중 상속)
class Student(Human, Human2):
    def __init__(self, name, age, studentNum):
        self.name = name
        self.age = age
        self.studentNum = studentNum
    def study(self):
        print("공부하다")
    def draw(self):
        print("잘~ 그리다")

kim = Student('김수미', 56, 20250321)
kim.eat()                  # 부모 기능
kim.study()                 # 자식 기능
print(kim.eyes)             # 부모 속성
print(kim.age)              # 부모 속성
print(kim.studentNum)      # 자식 속성

lee = Human('이수근', 49)
lee.eat()

choi = Human2('최배달', 69)
choi.draw()

park = Student('박남정', 25, 20250320)
park.introduce()
park.study()
park.draw()
print(park.studentNum)

