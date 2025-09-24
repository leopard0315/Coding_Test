T = int(input())
for i in range(T):
    a = int(input())
    b,c = divmod(a,25) # b는 몫, c는 나머지
    if(c == 0):
        print(b,0,0,0)
        continue
    else :
        d,e = divmod(c,10)
        if (e == 0):
            print(b,d,0,0)
            continue
        else :
            f,g = divmod(e,5)
            if (g == 0):
                print(b,d,f,0)
                continue
            else :
                h,i = divmod(g,1)
                print(b,d,f,h)
                continue