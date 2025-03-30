# 9. 사용자로부터 이메일 주소를 입력받고, 올바른 이메일 형식인지 검증하는 프로그램을 작성하세요. 이메일 형식은 다음을 따릅니다:
# - 이메일을 입력하세요: user@example.com
import re
def valid_email(email):
    pattern = re.compile(r"[\w.-]+@[\w.-]+[.]\w+")

    return re.search(pattern, email) is not None

email = input("이메일을 입력하세요: ")

if valid_email(email):
    print("올바른 이메일 형식입니다.")
else:
    print("잘못된 이메일 형식입니다.")