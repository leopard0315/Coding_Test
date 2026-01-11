N = 0
while(1):
    r,rotation,time = map(float,input().split())
    if(rotation == 0):
        break
    distance = r * 3.1415927 / 12 / 5280 * rotation 
    MPH = distance / (time / 60 / 60)
    N += 1
    print(f"Trip #{N}: {distance:.2f} {MPH:.2f}")