import re

# class 클래스명:
#     멤버변수
#     메서드
# 객체 = 클래스명()
# 객체.메서드명()

# 정규표현식 모듈 사용 방법
# 인자로 주어진 문자열을 번역하여 패턴 객체 생성

# p = re.compile(메타문자를 활용한 정규표현식)
# m = match(패턴과 일치 여부를확인할 문자열)
# p : 컴파일된 패턴 객체
# 반환 : 매치객체 = 문자열 패턴 일치
# 반환 : None = 문자열과 패턴 불일치

p = re.compile('ab*')   # 비매치
m = p.match('python')
print(m)

# [] 문자
p = re.compile('[p]')   # 매치
m = p.match('python')
print(m)

p = re.compile('[a-z]')   # 비매치
m = p.match('1python')
print(m)

p = re.compile('[b]')   # 매치
m = p.match('b')
print(m)

p = re.compile('[ab]')   # 매치
m = p.match('b')
print(m)

p = re.compile('[ab]')   # 매치
m = p.match('bac')
print(m)

p = re.compile('[ab]')   # 비매치
m = p.match('cba')
print(m)

# [] 문자 여러개 사용하는 경우
p = re.compile('[b][a]')   # 비매치
m = p.match('abc')
print(m)

p = re.compile('[ba][ab]')   # 매치
m = p.match('abc')
print(m)

p = re.compile('[ba][a]')   # 비매치
m = p.match('abc')
print(m)

p = re.compile('[0-9]')   # 매치
m = p.match('1bc')
print(m)

p = re.compile('[1][0-9]')  
m = p.match('13c')          # 매치
print(m)
m = p.match('23c')          # 비매치
print(m)    

p = re.compile('[0-9][A-Z][a-z]')   
m = p.match('13c')           # 비매치
print(m)
m = p.match('2k')            # 비매치
print(m)
m = p.match('2Ka')            # 매치
print(m)

print('------------')

p = re.compile('[0-9][A-Za-z]')   
m = p.match('2k')           # 매치
print(m)

p = re.compile('[^0-9][A-Za-z]')   
m = p.match('2k')           # 비매치
print(m)

p = re.compile('[0-9][^A-Za-z]')   
m = p.match('2_k')           # 매치
print(m)

p = re.compile('[0-9][_]')   
m = p.match('2_k')           # 매치
print(m)

p = re.compile('[0-9][^_]')   
m = p.match('2_k')           # 비매치
print(m)

# p = re.compile('[0-9][^A-Za-z]') 
p = re.compile('\d[^A-Za-z]')   
m = p.match('2_k')           # 매치
print(m)

# p = re.compile('\d[0-9A-Za-z_]')
p = re.compile('\d\w')
m = p.match('2_k')           # 매치
print(m)

# p = re.compile('\d[^0-9A-Za-z_]')
p = re.compile('\d\W')
m = p.match('2_k')           # 비매치
print(m)

print('------------')

p = re.compile('\s')
m = p.match(" 3c")          # 매치
print(m)
m = p.match("     3c")      # 매치
print(m)
m = p.match("\n3c")         # 매치
print(m)
m = p.match("\t3c")         # 매치
print(m)

print('------------')
# . 문자
p = re.compile('a.b')
print(p.match("aab"))       # 매치
print(p.match("a0b"))       # 매치
print(p.match("abc"))       # 비매치
print(p.match("a bc"))      # 매치
print(p.match("a\nbc"))     # 비매치
print(p.match("a\tbc"))     # 매치

print('------------')
p = re.compile('a[.]b')
print(p.match("aab"))       # 비매치
print(p.match("a.b"))       # 매치

print('------------')
# * 문자
p = re.compile('ca*t')
print(p.match("ct"))       # 매치
print(p.match("cat"))      # 매치
print(p.match("caaaat"))    # 매치
print(p.match("cbt"))       # 비매치
print(p.match("c t"))       # 비매치

print('------------')
# + 문자
p = re.compile('ca+t')
print(p.match("ct"))       # 비매치
print(p.match("cat"))      # 매치
print(p.match("caaaat"))    # 매치
print(p.match("cbt"))       # 비매치
print(p.match("c t"))       # 비매치

print('------------')
# {} 문자 : {m} {m,n} {m,} {,n}
p = re.compile('ca{2,5}t')
print(p.match("ct"))       # 비매치
print(p.match("cat"))      # 비매치
print(p.match("caat"))      # 매치
print(p.match("caaat"))      # 매치
print(p.match("caaaat"))      # 매치
print(p.match("caaaaat"))      # 매치
print(p.match("caaaaaat"))      # 비매치

p = re.compile('ca{2}t')
print(p.match("cat"))      # 비매치
print(p.match("caat"))      # 매치
print(p.match("caaat"))      # 비매치

# 중괄호 내부에 정규표현식은 공백 없이 작성
p = re.compile('ca{2 ,5}t')
p = re.compile('ca{2,  }t')
print(p.match("cat"))      # 비매치
print(p.match("caat"))      # 비매치
print(p.match("caaat"))      # 비매치

print('------------')
# ? 문자 : {0,1}
# p = re.compile('ca{0,1}t')
p = re.compile('ca?t')
print(p.match("ct"))       # 매치
print(p.match("cat"))      # 매치
print(p.match("caat"))      # 비매치
print(p.match("c t"))      # 비매치

print('------------')
# ^ 문자
p = re.compile('^hello')
print(p.match("hello world"))       # 매치
print(p.match(" hello world"))       # 비매치
print(p.match("\nhello world"))       # 비매치
print(p.match("pello world"))       # 비매치

print('------------')
# $ 문자
p = re.compile('world$')
print(p.match("hello world!"))       # 비매치
print(p.match("hello world "))       # 비매치
print(p.match("hello world\n"))       # 비매치
print(p.match("hello world"))       # 비매치
# p.match() : 문자열의 시작 부분부터 패턴과 일치하는지 확인

print(p.search("hello world"))       # 매치
# p.search() : 문자열의 전체를 검색하여 패턴과 일치하는지 확인
p = re.compile('^hello world$')
# 정규식에 ^과 $를 같이 사용하는 경우, 해당 문자열과 정확히 동일한 문자열만 매칭됨
print(p.search("hello world"))       # 매치
print(p.search("pello world"))       # 비매치
print(p.search("hello world!"))       # 비매치

p = re.compile('^hello python world$')
print(p.search("hello world"))              # 비매치
print(p.search("hello python world"))       # 매치
print(p.search("hello kython world"))       # 비매치

print('------------')
# re.MULTILINE 옵션을 사용시 각줄은 시작(^)과 끝($)으로 메타문자가 동작함
text = """hello world
python is  hello world
hello goodbye
hello world"""

p = re.compile('world$', re.MULTILINE)
# print(p.search(text))           # 매치
print(p.findall(text))           # 비매치