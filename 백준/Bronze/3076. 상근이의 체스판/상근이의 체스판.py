R,C = map(int,input().split())
A,B = map(int,input().split())
for h in range(1,R+1):
    if(h%2 == 1):
        for k in range(A):
            string = ""
            for i in range(1,C+1):
                if(i%2 == 1):
                    string += "X" * B
                else:
                    string += "." * B
            print(string)
    else:
        for k in range(A):
            string = ""
            for i in range(1,C+1):
                if(i%2 == 1):
                    string += "." * B
                else:
                    string += "X" * B
            print(string)