print("첫 번째 정수를 입력하세요") # 20을 입력
ra = input()
rb = input("두 번째 정수를 입력하세요\n")
print(type(ra))
print(type(rb))
rc = ra + rb
print(ra, "+", rb, "값은", rc, "이다")
# rc = ra - rb
# print(ra, "", rb, "값은", rc, "이다")

print("---------------")
ra = int(ra)
rb = int(rb)
print(type(ra))
print(type(rb))
rc = ra + rb
print(ra, "+", rb, "값은", rc, "이다")
rc = ra - rb
print(ra, "", rb, "값은", rc, "이다")
