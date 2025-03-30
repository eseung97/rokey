class Phone():
    print("휴대폰 생성")

    def info(self, product, year, color):
        self.product = product
        self.year = year
        self.color = color
        print(product, year ,color)
    def set_info(self, product, year, color):
        self.product = product
        self.year = year
        self.color = color
        print(product, year ,color)

my_phone = Phone()
my_phone.info("애플", "2020", "white")
my_phone.set_info("삼성", "2018", "black")