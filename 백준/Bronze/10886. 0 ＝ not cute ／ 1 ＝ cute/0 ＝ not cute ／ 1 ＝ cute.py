N = int(input())
b = []
for i in range(N):
    a = int(input())
    b.append(a)
if(b.count(1)> b.count(0)):
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")