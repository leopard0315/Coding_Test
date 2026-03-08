# 백준 2566번
# 최댓값
# 변수 선언
max_value = 0
a = []
X = 0
Y = 0

# 입력
# 행번호 찾기 & 최댓값 찾기
for i in range(9):
    b = list(map(int,input().split()))
    if(max_value <= max(b)):
        max_value = max(b)
        X = i
    a.append(b)

# 최댓값의 열번호 찾기
for j in range(9):
    if (a[X][j] == max_value):
        Y = j

# 출력값
print(max_value)
print(X+1,Y+1)