N = int(input())
sum = []
for i in range(N):
    a,b,c = map(int,input().split())
    if(a == b and b == c):
        sum.append(10000 + a * 1000)
    elif(a == b) :
        sum.append(1000 + a * 100)
    elif(b == c) :
        sum.append(1000 + b * 100)
    elif(c == a) :
        sum.append(1000 + c * 100)
    else : # 모두 다른 수인 경우
        sum.append(max(a,b,c)* 100)
print(max(sum))