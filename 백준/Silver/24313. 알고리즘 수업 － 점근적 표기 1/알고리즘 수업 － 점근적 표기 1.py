# 백준 24313번
# 알고리즘 수업 - 점근적 표기1
# 입력
a1, a0 = map(int,input().split())
c = int(input())
N = int(input())

# 점근 함수 계산
f_function = a1 * N + a0
g_function = c * N
result = g_function - f_function

# 빅오의 점근법 표기하기
if(c >= a1) and (result>=0):
    print(1)
else:
    print(0)