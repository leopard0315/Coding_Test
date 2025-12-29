N = int(input())
a = list(input())
sum = 0
# print(ord(a[0])-96)
for i in range(len(a)):
    sum += (ord(a[i])-96) * (31**i)
if(sum < 1234567891):
    print(sum)
else:
    sum = sum // 1234567891
    print(sum)