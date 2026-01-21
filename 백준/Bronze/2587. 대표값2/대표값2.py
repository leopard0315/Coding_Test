a = []
# 입력
for i in range(5):
    n = int(input())
    a.append(int(n))

# 평균 구하기
average = sum(a) // 5
print(average)

# 중앙값 구하기
a.sort()
print(a[2])