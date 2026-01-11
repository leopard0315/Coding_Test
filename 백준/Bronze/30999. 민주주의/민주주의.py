N,M = map(int,input().split())
cnt = 0
for i in range(N):
    s = input()
    count = 0
    for j in range(M):
        if(s[j] == 'O'):
            count += 1
        else:
            continue
    if(count >= M/2):
        cnt += 1
print(cnt)