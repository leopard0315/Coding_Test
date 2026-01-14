n = int(input())
k = (n-1) % 8
if (k == 0):
    print(1)
elif (k == 1 or k == 7):
    print(2)
elif(k == 2 or k == 6):
    print(3)
elif(k== 3 or k == 5):
    print(4)
else:
    print(5)