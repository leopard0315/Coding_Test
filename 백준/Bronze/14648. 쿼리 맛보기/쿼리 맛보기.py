n , q = map(int,input().split())
N = list(map(int,input().split()))
for k in range(q):
    result = 0
    result1 = 0
    result2 = 0
    res = 0
    a = list(map(int,input().split()))
    if(a[0] == 1):
        # [a,b] 사이의 합
        for i in range(a[2]-a[1]+1):
            result += N[a[1]-1 + i]
        # a 와 b swap
        res = N[a[1]-1]
        N[a[1]-1] = N[a[2]-1]
        N[a[2]-1] = res

    elif(a[0] == 2):
        # [a,b] 사이의 합
        for i in range(a[2]-a[1]+1):
            result1 += N[a[1]-1 + i]
        # [c,d] 사이의 합
        for j in range(a[4]-a[3] + 1):
            result2 += N[a[3]-1 + j]
        # [a,b]합 - [c,d]합 빼기
        result = result1 - result2
        
    print(result)   