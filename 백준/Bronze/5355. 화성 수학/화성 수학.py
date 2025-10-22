T = int(input())
for i in range(T):
    a = list(input().split())
    sum = float(a[0]) 
    for j in range(1,len(a)):
        if(a[j] == '@'):
            sum = sum * 3
        elif(a[j] == '%'):
            sum = sum + 5
        elif(a[j] == '#'):
            sum = sum -7
    print('%.2f'%sum)