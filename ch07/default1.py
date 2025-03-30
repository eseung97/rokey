def persona(width, height):
    print("함수디폴트값없음, width =", width, "height=", height)

def personb(width = 4, height = 3):
    print("함수디폴트값설정, width =", width, "height=", height)

# 디폴트 값은 매개변수가 여러개인 경우, "뒤"에서부터 설정가능
def personc(width , depth = 4 , height = 3):
    print("함수디폴트값설정, width =", width, "depth", depth, "height=", height)

persona(10,20)
personb()
personb(30,40)
personb(height = 70)
personc(30,40,50)
personc(30,40)
personc(30)
personc(40, depth =50)
personc(width=40, depth=30)

def persona(width =11, height =21):
    print("함수디폴트값없음, width =", width, "height=", height)

# def persona():
#     print("매개변수 없는 함수")

persona(10,20)
persona()
