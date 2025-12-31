L = int(input())
A = int(input()) # 국어 총 양
B = int(input()) # 수학 총 양
C = int(input()) # 국어 하루치 양
D = int(input()) # 수학 하루치 양
day1 = 0
day2 = 0
k = []
for i in range(1,A+1):
    if((A - C*i) > 0):
        day1 += 1
        continue
    else:
        day1 += 1
        k.append(int(day1))
        break
for j in range(1,B+1):
    if((B - D*j) > 0):
        day2 += 1
        continue
    else:
        day2 += 1
        k.append(int(day2))
        break
day = max(k)
print(L-day)