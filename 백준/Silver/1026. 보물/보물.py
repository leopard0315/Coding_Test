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

# b안의 수를 재배열하지 않을때
# -> 새로 리스트를 만들어서 정렬해서 적용하기-> sorted() 이용
# 입력값 받기
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

# A,B 정렬
A.sort()
C = sorted(B)
C.sort(reverse=True)

# S의 최솟값 구하기
S = 0
for i in range(N):
    S = S + A[i] * C[i]
print(S)
