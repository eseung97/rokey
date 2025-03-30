# 900점 이상 : 상위권
# 900 미만~ 600 이상 : 중상위권
# 600미만~ 300 이상 : 중위권
# 300미만 : 하위권

tscore = 899
if tscore >= 900:
    print("당신의 토익 점수는", tscore, "상위권 점수입니다.")
elif tscore >= 600:
    print("당신의 토익 점수는", tscore, "중상위권 점수입니다.")
elif tscore >= 300:
    print("당신의 토익 점수는", tscore, "중위권 점수입니다.")
else:
    print("당신의 토익 점수는", tscore, "하위권 점수입니다.")
print("if 문 종료됨")