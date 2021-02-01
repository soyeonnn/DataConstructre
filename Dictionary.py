grades = {}

# key - value 데이터 삽입
grades["현승"] = 80
grades["태호"] = 60
grades["영훈"] = 90
grades["지웅"] = 70
grades["동욱"] = 96

print(grades)  # 딕셔너리 출력

# 한 key 에 여러 value 저장 시도
grades["태호"] = 100

print(grades)  # 딕셔너리 출력

# key 를 이용해서 value 탐색
print(grades["동욱"])
print(grades["현승"])

# key 를 이용한 삭제
grades.pop("태호")
grades.pop("지웅")

print(grades)  # 딕셔너리 출력