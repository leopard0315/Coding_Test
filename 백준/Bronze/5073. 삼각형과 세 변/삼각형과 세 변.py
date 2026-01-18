# 5073번 백준

# 조건:
# 세변의 길이가 모두 같은 경우
# 두변의 길이만 같은 경우
# 세변의 길이가 모두 다른 경우
### 예외사항 : 가장 긴 변의 길이> 나머지 두변의 길이의 합 => 삼각형 X
while(1):
    a = list(map(int,input().split()))
    a.sort()
    # 마지막 줄 예외처리
    if(a[0] == 0 and a[1] == 0 and a[2] == 0):
        break
    
    # 삼각형의 조건이 아닌 경우
    if(a[2] >= a[1] + a[0]):
        print("Invalid")
    # 삼각형의 조건인 경우
    else :
        if(a[0] == a[1] and a[1] == a[2]):
            print("Equilateral")
        elif(a[0]== a[1] or a[1] == a[2] or a[0] == a[2]):
            print("Isosceles")
        else:
            print("Scalene")