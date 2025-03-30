class Car:
    # 클래스 변수
    wheel = 4
    def __init__(self, pnum, pspeed):
        # 인스턴스 변수
        self.num = pnum
        self.speed = pspeed

new_car = Car(2023, 90)
print("차량 번호", new_car.num)
print("속도는", new_car.speed)
print(new_car.wheel)

new_car2 = Car(2024, 100)
print("차량 번호", new_car2.num)
print("속도는", new_car2.speed)
print(new_car2.wheel)

print(Car.wheel)
