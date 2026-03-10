# 백준 9063번
# 대지

# 입력
N = int(input())
a = []
for _ in range(N):
    b = list(map(int,input().split()))
    a.append(b)

# 정렬
# x값기준
a.sort(key= lambda k : k[0])
# 밑변의 길이 구하기
w = a[-1][0] - a[0][0]

# y값 기준 정렬
a.sort(key= lambda k : k[1])
# 높이 구하기
h = a[-1][1] -a[0][1]

# 출력
print(w * h)