# 2501번

N, K = map(int,input().split())
count = 0
ans = 0
for i in range(1,N+1):
    if N % i == 0:
        count += 1
        if count == K:
            ans = i
            break
if count < K:
    print(0)
else:
    print(ans)
