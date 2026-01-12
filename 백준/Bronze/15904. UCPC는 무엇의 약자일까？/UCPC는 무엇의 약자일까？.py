a = list(map(str,input().split()))
b = []
string = ""
for i in range(len(a)): # A~Z
    for j in range(len(a[i])):
        if(ord(a[i][j:j+1]) >= 65 and ord(a[i][j:j+1])<= 90):
            string += (a[i][j:j+1])

target = "UCPC"
idx = 0
for ch in string:
    if ch == target[idx]:
        idx += 1
        if idx == 4:
            break

if(idx == 4):
    print("I love UCPC")
else:
    print("I hate UCPC")