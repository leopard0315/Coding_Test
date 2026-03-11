# 백준 18258번
# 요세푸스 문제 0

a = []
b = []

N,K = map(int,input().split())
n = K-1
for i in range(1,N+1):
    a.append(i)

while len(a) > 0:
    n = n % len(a)
    k = a.pop(n)
    b.append(k)
    n = n + K - 1

print('<' + ', '.join(map(str,b)) + '>')