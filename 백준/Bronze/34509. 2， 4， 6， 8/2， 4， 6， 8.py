# 입력은 없다
a = []
# 10의 자리수와 1의 자리수
A = 0
B = 0
C = ""
j = 0
for i in range(10,100):
    A = i // 10
    B = i % 10
    if((A+B)%6 == 0):
        if(A != 8 and B != 8):
            C = str(i)
            j = int(C[::-1])
            if(j%4 == 0):
                a.append(int(i))
print(a[0])