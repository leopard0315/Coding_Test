# 백준 1874번
# 스택 수열

import sys
input = sys.stdin.readline
from collections import deque
a = deque()

# 입력
N = int(input())
for i in range(1,N+1): # a dequeue 생성 (1~N)
    a.append(i)
b = []  # 스택 리스트
ans = [] # +/- 리스트
num = 0
Yes_or_No = False

for _ in range(N):
    n = int(input())

    if n > num:
        while a[0] <= n:
            b.append(a.popleft()) 
            ans.append("+")
            if a:
                continue
            else:
                break
        num = b.pop()
        ans.append("-")
            
    elif n < num :
        # 경우2 : b의 마지막 원소가 n인 경우
        if b[-1] == n:
            num = b.pop()
            ans.append("-")

        else: # 경우3 : 입력된 수열을 만들수 없는 경우
            Yes_or_No = True

# 출력
if Yes_or_No :
    print("NO")
else:
    print("\n".join(ans))