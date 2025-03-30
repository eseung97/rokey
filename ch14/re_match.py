import re

# a-z 중 하나의 문자가 한번 이상 반복되는 패턴
p = re.compile('[a-z]+')
m = p.match("python")       # match
print(m)

m = p.match("3 python")     # None
print(m)

# p = re.compile('정규표현식')
# m = p.match('조사할 문자열') 
# if m:
#     print('Match found', m.group())
# else:
#     print('No match')
print('------------')
# match() 함수
p = re.compile('[a-z]+')
m = p.match('python')      # match
if m:
    print('Match found', m.group())
else:
    print('No match')

print('------------')
# search() 함수
p = re.compile('[a-z]+')
m = p.search('3 python')      # match
if m:
    print('Match found', m.group())
else:
    print('No match')

print('------------')
# findall() 함수
p = re.compile('[a-z]+')
m = p.findall('life is too short')      # match
print(m)

print('------------')
# finditer() 함수
# 리턴: 반복 가능한 객체 -> for문 사용 확인
p = re.compile('[a-z]+')
result = p.finditer('life is too short')      # match
for m in result:
    # print(m)
    print(m.group())

print('------------')
# match 객체 활용
p = re.compile('[a-z]+')
result = p.finditer('life is too short')      # match
for m in result:
    # print(m)
    print(m.group())
    print(m.span())
    print(m.start())
    print(m.end())
    print('------------')


print('------------')
# p = re.compile('정규표현식')
# m = p.match('조사할 문자열')
p = re.compile('[a-z]+')
m = p.match('python') 
m = re.match('[a-z]+', 'python')
print(m)

print('축약 형태 코드------------')
m = re.match('[a-z]+', 'python')
print(m)