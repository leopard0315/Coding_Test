# 백준 2754번
a = input()
output = 0.0
if (a[0] == 'A'):
    if(a[1] == '+'):
        output = 4.3
    elif(a[1] == '-'):
        output = 3.7
    else : 
        output = 4.0
elif (a[0] == 'B'):
    if(a[1] == '+'):
        output = 3.3
    elif(a[1] == '-'):
        output = 2.7
    else : 
        output = 3.0
elif (a[0] == 'C'):
    if(a[1] == '+'):
        output = 2.3
    elif(a[1] == '-'):
        output = 1.7
    else : 
        output = 2.0
elif (a[0] == 'D'):
    if(a[1] == '+'):
        output = 1.3
    elif(a[1] == '-'):
        output = 0.7
    else : 
        output = 1.0
else :
    output = 0.0

print(output)