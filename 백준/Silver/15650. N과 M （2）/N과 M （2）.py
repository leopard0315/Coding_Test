from itertools import combinations

N,M = map(int,input().split())
n = []
for i in range(1,N+1):
    n.append(i)

a = list(combinations(n,M))
for j in range(len(a)):
    if M == 1:
        print(n[j])
    else:
        print(*a[j], sep=' ')

