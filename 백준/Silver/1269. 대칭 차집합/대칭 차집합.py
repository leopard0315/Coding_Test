# 백준 1269번
# 대칭 차집합
# import sys
# input = sys.stdin.readline

# 입력
a,b = map(int,input().split())
# A - set, B - list
A = set(map(int,input().split()))
B = list(map(int,input().split()))
C = set()

# 교집합 구하기
for i in range(b):
    # 교집합인경우
    if(B[i] in A):
        C.add(B[i])

# A,B,교집합 길이 구하기
# print(len(A))
# print(len(B))
# print(len(C))
minus1 = len(A) - len(C)
minus2 = len(B) - len(C)
print(minus1 + minus2)