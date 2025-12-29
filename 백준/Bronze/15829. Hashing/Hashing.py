N = int(input())
a = list(input())
sum = 0
mod = 1234567891
# print(ord(a[0])-96)
for i in range(len(a)):
    sum = (sum + (ord(a[i])-96) * (31**i)) % mod
print(sum)