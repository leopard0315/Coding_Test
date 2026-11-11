def solution(num, total):
    # num이 홀수인 경우와 짝수인 경우를 나누어서 구한다.
    a = []
    # num이 홀수인 경우
    if num % 2 != 0:
        num1 = total // num
        for i in range(num1-1,num1 - (num-1)//2-1,-1):
            a.append(i)
        print(a)
        for j in range(num1,num1 + (num-1)//2+1 ):
            a.append(j)
        print(a)
            
    # num이 짝수인 경우
    else:
        num1 = total // num # 3
        for i in range(num1,num1 - num//2, -1):
            a.append(i)
        print(a)
        for j in range(num1+1,num1+1 + num //2 ):
            a.append(j)
        print(a)
        
    a.sort()
    return a