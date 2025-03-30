# class 클래스명:
#     멤버변수
#     def 멤버함수(self, 매개변수1):
#         self.멤버변수 = 값
#         return 반환값

# Pizza(피자) class 생성
# 치즈피자, 하와이안피자, 콤보피자, 고구마피자, 포테이토피자
class Pizza:
    shape = "circle"
    def taste(self):
        print('맛을 내다')   
        self.flavor = '피자맛'
        return self.flavor

# Pizza(피자) class  객체 생성 => 사용
comboPizza = Pizza()        #객체(인스턴스) 생성
print(comboPizza.taste())   #메소드
print(Pizza.shape)          # 클래스 변수