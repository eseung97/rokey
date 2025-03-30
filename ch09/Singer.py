class Singer:
    numberOfMouth = 1
    def sing(self):
        print('노래하다.')

# 객체 생성 역할 => 생성자 함수
# 생성자 함수는 클래스명과 동일
iu = Singer()
print(iu.numberOfMouth)
iu.sing()

bts = Singer()
print(bts.numberOfMouth)
bts.sing()