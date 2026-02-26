# 백준 25206번
# 너의 평점은
# 학점 X 과목평점의 합
num = 0.0
score = 0

# 총점의 합
total = 0

# 입력
for i in range(20):
    name, credit, grade = map(str,input().split())
    if(grade == "A+"):
        num = 4.5
    elif(grade == "A0"):
        num = 4.0
    elif(grade == "B+"):
        num = 3.5
    elif(grade == "B0"):
        num = 3.0
    elif(grade == "C+"):
        num = 2.5
    elif(grade == "C0"):
        num = 2.0
    elif(grade == "D+"):
        num = 1.5
    elif(grade == "D0"):
        num = 1.0
    elif(grade == "F"):
        num = 0.0
    else :
        continue

    # 학점의 총합
    total += float(credit)
    # 학점 X 과목평점의 합
    score = score + float(credit) * num
        
# 출력
result = score / total
print(result)