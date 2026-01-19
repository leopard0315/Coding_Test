N = list(map(int,input()))
N.sort(reverse = True)
string = ""
for i in range(len(N)):
    string += str(N[i])
print(string)