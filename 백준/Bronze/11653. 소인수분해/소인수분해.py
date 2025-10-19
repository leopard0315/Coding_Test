# 11653번

N = int(input())
n = int(N)
for j in range(1, N+1):
    if (n == 1) :
        break
    else : 
        for i in range(2,N+1):
            if(n % i == 0):
                print(i)
                n = n // i
                break
        else:
            continue