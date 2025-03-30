# import re
# pattern = r'\w+'
# text = "Hello, World!"
# print(re.findall(pattern, text))


# import re
# pattern = r'(ab)+'
# text = "ababab"
# match = re.match(pattern, text)
# print(match.group())


# 6번
# import re
# pattern = re.compile(r'[\w.-]+@[\w.-]+\.\w+')
# text = "이메일 목록: test@example.com, hello@world.net, user123@domain.org"
# match = re.findall(pattern, text)
# print(match)


# 7번
# import re
# pattern = re.compile(r'010-\d{4}-\d{4}')
# text = "연락처: 010-1234-5678, 02-987-6543, 031-456-7890"
# phone_numbers = re.findall(pattern, text)
# print(phone_numbers)


# 8번
# import re
# pattern = re.compile(r'[^.]*?Python[^.]*\.')
# text = "I love Python. Java is also popular. Python is great for AI."
# m = re.findall(pattern, text)
# print(m)


# 9번
# import re
# pattern = r'\d+'
# text = "상품 코드: A123, B456, C789, 가격: 12000원"
# m = re.findall(pattern, text)
# print(m)


# 10번
import re
pattern = r'[A-Z]{2,}'
text = "NASA is working on AI projects with IBM and Google."
m = re.findall(pattern, text)
print(m)