a = list(map(int,input().split()))
sum = a[2]- a[0]*a[1]
if(sum< 0):
    print(abs(sum))
else:
    print(0)