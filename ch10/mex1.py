# class
class Cvalue:
    def __init__(self):
        self.lista=[]
    def add(self, num):
        self.lista.append(num)
    def fprint(self):
        print(self.lista)

# function
def plus(a,b):
    c = a + b
    return c

# variable
# print(__name__)
if __name__ == "__main__":
    p1 = Cvalue()
    # print(p1.lista)
    p1.add(1)
    p1.add(2)
    p1.add(3)
    p1.fprint()