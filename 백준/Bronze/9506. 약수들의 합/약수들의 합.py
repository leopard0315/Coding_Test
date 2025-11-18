while(True):
    n = int(input())
    a= []
    if(n == -1):
        break;
    else:
        for i in range(1,n):
            if(n%i == 0):
                a.append(i)
    sum = 0
    for j in range(len(a)):
        sum = sum + a[j]
    if (sum == n):
        word = " + ".join(map(str,a))
        print(f"{n} = {word}")
    else :
        print(n,"is NOT perfect.")