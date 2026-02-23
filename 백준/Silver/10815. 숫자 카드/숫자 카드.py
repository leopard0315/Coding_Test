# 백준 10815번
# 숫자 카드
import sys
input = sys.stdin.readline

# 입력
N = int(input())
n = set(map(int,input().split()))
M = int(input())
m = list(map(int,input().split()))

# set안에 해당 리스트 값이 있는지 확인
c = []
for i in range(M):
    if (m[i] in n):
        c.append(1)
    else:
        c.append(0)

# 출력
print(*c)