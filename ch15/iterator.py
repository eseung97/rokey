# data : iterable
class MyIterator:
    def __init__(self,data):
        self.data = data
        self.position = 0

    # 기능: iterable => iterator
    def __iter__(self):
        return self
    
    # iterator는 next()로 값을 반환 가능
    def __next__(self):
        if self.position >= len(self.data):
            raise StopIteration
        result = self.data[self.position]
        self.position += 1
        return result

if __name__ == "__main__":
    i = MyIterator([1,2,3])
    for item in i:
        print(item)
# print(next(i))