S = int(input())
count = 0
i = 0

while(1):
    if (S > i):
        i  = i + 1
        S = S - i
        count = count + 1 
    else:
        print(count)
        break 