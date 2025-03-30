# 문자열.split(구분자) 메서드
p1 = '김삿갓 597-89-000089'
p2 = '이수근 343-64-000064'
p3 = '박혁거세 136-97-000097'

# p1_1 = p1.split()
p1_1 = p1.split(" ")
print(p1_1[0])
p1_2 = p2.split(" ")
print(p1_2[0])
p1_3 = p3.split(" ")
print(p1_3[0])

print('-------------')

my_string= "    Python is awesome!    "
print(my_string)
stripped_string = my_string.strip()
print(stripped_string)
my_string= "    \tPython is awesome!\n"
print(my_string)
stripped_string = my_string.strip()
print(stripped_string)

print('-------------')

my_list = ["apple", "banana", "cherry"]
joined_string = "-".join(my_list)
print(joined_string)