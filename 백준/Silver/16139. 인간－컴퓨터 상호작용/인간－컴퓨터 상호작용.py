# 백준 16139번
# 인간-컴퓨터 상호작용
import sys
input = sys.stdin.readline

# 입력
S = input()
q = int(input())
for i in range(q):
    a,l,r = map(str,input().split())
    l = int(l)
    r = int(r)

    cnt = 0
    for j in range(l,r+1):
        if S[j] == a:
            cnt += 1
        else:
            continue
    print(cnt)