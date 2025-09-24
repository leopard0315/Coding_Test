X = int(input())
Y = X
count_X = 0
if (X == 1): # 1인 경우 
    print(f"{1}/{1}")
for i in range(1,X,1) : # 1이 아닌 경우
    if(Y-i > i+1):
        Y = Y - i
        count_X += 1
        continue
    else :
        if(count_X %2 == 1): # 라인이 홀수일때
            print(f"{2-Y + 2*i}/{Y-i}")
        else : # 라인이 짝수일때
            print(f"{Y-i}/{2-Y + 2*i}")
        break