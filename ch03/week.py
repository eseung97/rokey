text ="월요일부터 일요일 중 영어로 번역하고 싶은 요일을 입력하세요(예시:월요일): "
yoil = input(text)
if yoil == "월요일":
    print("monday")
elif yoil == "화요일":
    print("tuesday")
elif yoil == "수요일":
    print("wednesday")
elif yoil == "목요일":
    print("thursday")
elif yoil == "금요일":
    print("friday")
elif yoil == "토요일":
    print("saturday")
elif yoil == "일요일":
    print("sunday")
else:
    print("한글 요일을 잘못 입력했습니다.")