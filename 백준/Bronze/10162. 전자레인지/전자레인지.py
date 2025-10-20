T = int(input())
A = 300
B = 60
C = 10
A_c = 0
B_c = 0
C_c = 0

a,b = divmod(T,A)
c,d = divmod(b,B)
e,f = divmod(d,C)
if(f != 0):
    print(-1)
else :
    print(a,c,e)