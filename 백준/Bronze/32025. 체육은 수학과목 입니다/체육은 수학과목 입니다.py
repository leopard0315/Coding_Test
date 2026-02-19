# 백준 32025번
# 체육은 수학과목입니다.

# 입력 m단위
H = int(input())
W = int(input())
r = 0

# 반지름의 길이 구하기
if (H > W):
    r = W * 100 // 2
else :
    r = H * 100 // 2

# 출력 
print(r)