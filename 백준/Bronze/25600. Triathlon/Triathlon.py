N = int(input())
b = []
score = 0

for i in range(N):
    a,d,g = map(int,input().split())
    score = a * (d+g)
    if (a == (d+g)):
        score = score * 2
    b.append(int(score))
print(max(b))