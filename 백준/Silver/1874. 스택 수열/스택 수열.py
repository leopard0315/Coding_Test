# 백준 1874번
# 스택 수열
# append = push / pop = 제거
import sys
input = sys.stdin.readline
from collections import deque
a = deque()

# 입력
N = int(input())
for i in range(1,N+1): # a dequeue 생성 (1~N)
    a.append(i)
b = []  # 스택 리스트
c = [] # +/- 리스트

num = 0
Y = 0
for _ in range(N):
    n = int(input())
    # 경우1 : 
    if n > num:
        while a[0] <= n:
            b.append(a.popleft()) # a 배열의 가장 앞부분 추가 및 제거
            c.append("+")
            if a:
                continue
            else:
                break
        num = b.pop()
        c.append("-")
            
    # 경우2 & 경우3
    elif n < num :
        # 경우2 : b의 마지막 원소가 n인 경우
        if b[-1] == n:
            num = b.pop()
            c.append("-")
        else: # 경우3 : 입력된 수열을 만들수 없는 경우
            Y = 1

# 출력
if Y != 0 :
    print("NO")
else:
    for i in range(len(c)):
        print(c[i])