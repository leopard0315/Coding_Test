N = int(input())
sum = 1
if(N == 0):
    print(sum)
elif(N > 0):
    for i in range(2,N+1):
        sum *= i
    print(sum)