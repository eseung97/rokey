class Phone:
    def __init__(self, number, color):
        self.number = number
        self.color = color
    def showInfo(self):
        print(f"전화번호: {self.number}")
        print(f"색상: {self.color}")


phone = Phone("010-1234-5678", "검정")
phone.showInfo()

class SmartPhone(Phone):
    def __init__(self, number, color, company):
        self.number = number
        self.color = color 
        self.company = company
    def showInfo(self):
        print(f"전화번호: {self.number}")
        print(f"색상: {self.color}")
        print(f"회사: {self.company}")

apple = SmartPhone("010-1234-5678", "검정", "애플")
apple.showInfo()