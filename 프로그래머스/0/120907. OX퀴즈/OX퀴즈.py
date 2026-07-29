def solution(quiz):
    # 연산자는 + or - 중에 1개이다.
    result = []
    for i in range(len(quiz)):
        array = quiz[i].split('=')
        a = array[0].split(' ')
        b = array[1].strip() 
        
        if a[1] == '+' :
            res = int(a[0]) + int(a[2])
        else :
            res = int(a[0]) - int(a[2])
    
        if res == int(b):
            result.append('O')
        else:
            result.append('X')
        
    return result
        
    
    