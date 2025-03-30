# 7. 다음 조건을 만족하는 이터레이터 클래스를 구현하세요.
# 리스트를 인자로 받아 요소를 하나씩 반환합니다.
# StopIteration 예외를 적절히 처리합니다

class Myiterator:
    def __init__(self, data):
        self.data = data
        self.position = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.position >= len(self.data):
            raise StopIteration
        result = self.data[self.position]
        self.position += 1
        return result

if __name__ == "__main__":
    i = Myiterator([1,2,3])
    for item in i:
        print(item)