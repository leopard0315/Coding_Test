# 2581번
M = int(input())
N = int(input()) # M <= N

prime = [True for i in range(N+1)]
answer = []
for i in range(2,N+1):
    if prime[i] == True:
        j = 2
        while i * j <= N:
            prime[i*j] = 0
            j += 1

for i in range(M,N+1):
    if i == 1:
        continue
    if prime[i] == True:
        answer.append(i)

# 출력
if answer:
    print(sum(answer))
    print(answer[0])
else:
    print(-1)
