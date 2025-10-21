a = []
i = 0
for i in range(5):
    n = int(input())
    if(n < 40):
        n = 40
    a.append(n)
print(sum(a)//5)