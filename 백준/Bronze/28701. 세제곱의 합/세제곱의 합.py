N = int(input())
sum1 = 0
sum2 = 0
sum3 = 0
# 첫줄
for i in range(1,N+1):
    sum1 = sum1 + i
# 둘째줄
sum2 = sum1 ** 2
# 세번째줄
for j in range(1,N+1):
    sum3 = sum3 + j**3
# 출력
print(sum1)
print(sum2)
print(sum3)