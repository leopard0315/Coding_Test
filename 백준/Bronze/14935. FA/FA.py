N = int(input())
while(1):
    N1 = N
    count = 0
    while(1):
        if(N1 < 1):
            break
        N1 = N1 // 10
        count += 1
    k = (N // 10 ** (count-1)) * count
    if(N == k):
        print("FA")
        break
    else:
        N = k
