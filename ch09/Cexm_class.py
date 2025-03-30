class Cexm:
    def fsam(self):
        print("멤버 함수(메소드)")
    def fsbm(self, pa):
        self.x = pa
        print("멤버 변수 x는", self.x)

ca = Cexm()     # 생성자 함수로 객체 생성
ca.fsam()
ca.fsbm(10)