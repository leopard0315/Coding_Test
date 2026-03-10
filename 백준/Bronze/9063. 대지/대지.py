# 백준 9063번
# 대지

# 입력
N = int(input())
x = []
y = []
for _ in range(N):
    a,b = list(map(int,input().split()))
    x.append(a)
    y.append(b)

# 밑변의 길이 구하기
w = max(x) - min(x)

# 높이 구하기
h = max(y) - min(y)

# 출력
print(w * h)