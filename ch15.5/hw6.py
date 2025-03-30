# 6. 주어진 문자열에서 python으로 시작하는 모든 단어를 찾아 출력하는 프로그램을 작성하세요.

# data = """python one
# life is too short
# python two
# you need python
# python three"""

import  re

pattern = re.compile('python')

data = """python one
life is too short
python two
you need python
python three"""

match  = pattern.findall(data)
print(match)