N,K = map(int,input().split())
# 분자 a - N!
a,b,c = 1,1,1

for i in range(1,N+1):
    a = a * i

# 분모 b - K!
for j in range(1,K+1):
    b = b * j

# 분모 c - (N-k)!
for k in range(1,N-K + 1):
    c = c * k

print(a // (b*c))