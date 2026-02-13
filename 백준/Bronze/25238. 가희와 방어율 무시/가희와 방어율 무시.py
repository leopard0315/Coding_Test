# 백준 25238번

# 입력
a,b = map(int,input().split())

# 방어무시 계산
k = a - a * b / 100

# 출력
if(k >= 100):
    print(0)
else:
    print(1)