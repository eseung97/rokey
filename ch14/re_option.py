import re

# . 문자는 모든 문자와 매칭(단, \n은 제외)
p = re.compile('a.b')
m = p.match('a\nb')     # None
print(m)

print('-------------')
p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')     # match
print(m)

print('-------------')
p = re.compile('[a-z]+')
m = p.match('Python')     # None
print(m)

print('-------------')
# p = re.compile('[a-z]+', re.IGNORECASE)
p = re.compile('[a-z]+', re.I)
m = p.match('Python')     # match
print(m)

print('-------------')
# p = re.compile("^python\s\w+")
p = re.compile("^python\s\w+", re.M)

data = """python one
life is too short
python two
you need python
python three"""
print(p.findall(data))