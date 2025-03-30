class Bag:
    def __init__(self):     # 객체 초기화 함수(객체 생성시 자동 호출)
        self.data = []      # 특정 객체에 변수를 생성하고 빈리스트 할당
    def add(self, x):
        self.data.append(x)
    def addtwice(self, x):
        self.add(x)
        self.add(x)

handbag = Bag()             # 생성자 함수로 객체 생성
print(handbag.data)
handbag.add("손수건")
print(handbag.data)
handbag.addtwice("신용카드")
print(handbag.data)


print("----------------")
backpack = Bag()
backpack.data = []
print(backpack.data)
backpack.add("노트북")
print(backpack.data)
backpack.addtwice("사과")
print(backpack.data)

crossbag = Bag()
# print(crossbag.data)
print(crossbag.data)
crossbag.add("간식")
crossbag.add("휴지")
crossbag.add("보조배터리")
print(crossbag.data)
crossbag.addtwice("사탕")
print(crossbag.data)
