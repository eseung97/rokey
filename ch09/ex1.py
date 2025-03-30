class Animal:
    # name  = '고양이'
    def __init__(self,name):
        self.name  = name

    def sound(self):
        print('야옹~')

cat = Animal('고양이')
print(cat.name)
cat.sound()


class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def taste(self):
        print("새콤하다")

orange = Fruit("오렌지", "노란색")
print(orange.name, orange.color)
orange.taste()