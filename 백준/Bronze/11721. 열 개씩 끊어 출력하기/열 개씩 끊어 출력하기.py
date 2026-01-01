N = list(input())
ans = ""
for i in range(len(N)):
    ans += N[i]
    if((i+1)%10 == 0):
        print(ans)
        ans = ""
print(ans)