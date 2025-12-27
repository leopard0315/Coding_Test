N = list(map(int,input().split()))
string = ""
if(N[0] == 1):
    for i in range(1,8):
        if(N[i] == i+1):
            continue
        else :
            string = "mixed"
            break
    if(string == ""):
        string = "ascending"
elif(N[0] == 8):
    for i in range(1,8):
        if(N[i] == 8 - i):
            continue
        else:
            string = "mixed"
            break
    if(string == ""):
        string = "descending"
else :
    string = "mixed"
print(string)