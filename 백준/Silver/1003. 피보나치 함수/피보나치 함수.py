T = int(input())
# 입력 값들의 배열
c = []
for i in range(T):
    N = int(input())
    c.append(int(N))
d = max(c)

# 0 배열
a = [1,0]
# 1 개수 배열
b = [0,1]

for i in range(2,d+1):
    A = a[i-1] + a[i-2]
    B = b[i-1] + b[i-2]
    a.append(int(A))
    b.append(int(B))
for j in range(len(c)):
    print(a[c[j]] , b[c[j]])