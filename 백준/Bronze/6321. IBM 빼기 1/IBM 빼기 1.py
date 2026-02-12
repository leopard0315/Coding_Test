# 백준 6321번

n = int(input())
num = 0

for _ in range(n):
    s = list(input())
    string = ""
    for i in range(len(s)):
        if(ord(s[i]) == 90):
            k = 65
        else:
            k = ord(s[i]) + 1
        s[i] = chr(k)
        string = string + s[i]
    num += 1
    print("String #" + str(num))
    print(string)
    print()