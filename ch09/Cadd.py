class Cadd:
    def fadd(self, a, b):
        self.x = a
        self.y = b
        self.hap = self.x + self.y

obj = Cadd()
obj.fadd(10,20)
print("객체  obj 내의 인스턴스 변수 x의 값은", obj.x)
print("객체  obj 내의 인스턴스 변수 y의 값은", obj.y)
print("객체  obj 내의 인스턴스 변수 hap의 값은", obj.hap)
