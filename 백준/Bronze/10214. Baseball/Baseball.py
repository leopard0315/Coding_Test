T = int(input())
A = 0
B = 0
for j in range(T):
    for i in range(9):
        a,b = input().split() # 문자열로 받음
        A = A + int(a)
        B = B + int(b)

    if(A > B):
        print("Yonsei")
    elif (A < B):
        print("Korea")
    else :
        print("Draw")