a = input()
h = 0 # h = height
for i in range(len(a)):
    if(i == 0):
        h = h + 10
    elif (a[i-1] == a[i]):
        h = h + 5
    else:
        h = h + 10
print(h)