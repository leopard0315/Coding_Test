# 34236번
# 대회의 개수

# 입력
N = int(input())
a = list(map(int,input().split()))

# 공차계산
x = a[1] - a[0]
# 출력
print(a[-1] + x)