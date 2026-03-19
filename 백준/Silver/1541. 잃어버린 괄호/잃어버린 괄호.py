# 백준 1541번
# 잃어버린 괄호

# -을 기준으로 요소들 분리 및 덩어리 생성
N = input().split('-')
a = []

for i in N:
    sum = 0
    # +을 기준으로 요소들 분리
    tmp = i.split('+')
    # + 으로 분리한 요소들의 합 계산
    for j in tmp:
        sum += int(j)
    a.append(sum)

n = a[0]
for i in range(1,len(a)):
    n = n - a[i]
print(n)  