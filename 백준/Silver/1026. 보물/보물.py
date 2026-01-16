# <b안에 수를 재배열할때>
# 입력값 받기
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

# A,B 정렬
A.sort()
B.sort()

# S의 최솟값 구하기
S = 0
for i in range(N):
    S = S + A[i] * B[N-i-1]
print(S) 