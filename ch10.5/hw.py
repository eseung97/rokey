# 5번
# list = [10,25,5,12,33]
# mina = list[0]

# for i in range(1,4,1):
#     if mina > list[i]:
#         mina = list[i]
# print(mina)


# 8번
# from math import factorial
# print(factorial(5))


# 9번
# class Animal:
#     def speak(self):
#         return "Animal speaks"

# class Dog(Animal):
#     def speak(self):
#         return "Woof!"

# dog1 = Dog()
# print(dog1.speak())


# 10번
class Person:
    def __init__(self, name):
        self.name = name
    
    def introduce(self):
        return f"My name is {self.name}"
    
class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

lee = Student("이예승", 205)
print(lee.introduce())