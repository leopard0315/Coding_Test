# 백준 30088번
# 공포의 면담실
# a.remove를 사용해서 원하는 요소를 지운다.

# 입력 & 맨 앞 요소 제거
N = int(input())
b = []
for _ in range(N):
    a = list(map(int,input().split()))
    a.remove(a[0])
    b.append(sum(a))

# 정렬
b.sort()
total = 0
c = set()

# 누적합 배열 생성
for i in range(len(b)):
    total += b[i]
    c.add(total)

# 출력
print(sum(c))