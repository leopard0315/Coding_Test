n = int(input())
sum_a = 100
sum_b = 100
for i in range(n):
    a, b = map(int, input().split())
    if(a > b) :
        sum_b = sum_b - a
    elif (a < b):
        sum_a = sum_a - b
    else :
        continue
print(sum_a)
print(sum_b)