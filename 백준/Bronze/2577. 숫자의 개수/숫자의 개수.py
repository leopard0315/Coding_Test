A = int(input())
B = int(input())
C = int(input())
total = str(A * B * C)
total_list = list(total)
total_list.sort()
b = [0,1,2,3,4,5,6,7,8,9]
c = [0,0,0,0,0,0,0,0,0,0]
num = 0
count = 0
for i in range(0,len(total_list),1):
    for j in range(0,10,1):
        if(int(total_list[i]) == b[j]):
            c[j] += 1
            break
for k in range(len(c)):
    print(c[k])