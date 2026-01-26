# 10811번 백준
# 1월 26일

N, M = map(int,input().split())
n = []
for i in range(1,N+1):
    n.append(int(i))
for _ in range(M):
    a,b = map(int,input().split())
    if(a == b):
        continue
    else:
        n[a-1:b] = n[a-1:b][::-1]
print(*n)