R,C = map(int,input().split())
A,B = map(int,input().split())
for h in range(1,R+1):
    if(h%2 == 1):
        for k in range(A):
            string = ""
            for i in range(1,C+1):
                for j in range(B):
                    if(i%2 == 1):
                        string += "X"
                    else:
                        string += "."
            print(string)
    else:
        for k in range(A):
            string = ""
            for i in range(1,C+1):
                for j in range(B):
                    if(i%2 == 1):
                        string += "."
                    else:
                        string += "X"
            print(string)