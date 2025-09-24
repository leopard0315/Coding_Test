X = int(input())
Y = X
count_X = 0
if (X == 1):
    print(f"{1}/{1}")
for i in range(1,X,1) :
    if(Y-i > i+1):
        Y = Y - i
        count_X += 1
        continue
    else :
        count_X = count_X
        if(count_X %2 == 1): #홀수
            print(f"{2-Y + 2*i}/{Y-i}")
        else :
            print(f"{Y-i}/{2-Y + 2*i}")
        break