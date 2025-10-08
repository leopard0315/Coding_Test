A,B = input().split()
A = int(A)
a,b = divmod(A, 100) # a : 100의 자리
c,d = divmod(b, 10) # c : 10의 자리, d : 1의 자리

B = int(B)
e,f = divmod(B, 100) # e : 100의 자리
g,h = divmod(f, 10) # g : 10의 자리, h : 1의 자리

# 상수식으로 숫자 변경
A = d * 100 + c * 10 + a
B = h * 100 + g * 10 + e

# 백의 자리 비교
if(d > h): 
    print(A)
elif(d < h): 
    print(B)
else : # 백의 자리 숫자가 같은 경우, 십의 자리 비교
    if(c > g) :
        print(A)
    elif(c < g) : 
        print(B)
    else : # 백의 자리 같고, 십의 자리 같을때, 일의 자리 비교
        if(a > e) :
            print(A)
        else :
            print(B)