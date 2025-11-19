N = int(input()) # 도시 개수
a = list(map(int,input().split())) # 도시~도시 사이의 거리
b = list(map(int,input().split())) # 도시별 리터당 가격 (거리 = 리터)
min = b[0]
sum = b[0] * a[0] 
for i in range(1,N-1):
    if(min <= b[i]):
        sum = sum + min * a[i]
    elif(min > b[i]) :
        min = b[i]
        sum = sum + min * a[i]
print(sum)