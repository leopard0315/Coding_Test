N = int(input())
a = []
count = 0
for i in range(N):
    a.append(input())
b = sorted(list(set(a)))
b.sort(key=len)
for j in range(len(b)):
    print(b[j])