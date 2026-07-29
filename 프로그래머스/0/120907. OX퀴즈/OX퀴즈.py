def solution(quiz):
    # 연산자는 + or - 중에 1개이다.
    result = []
    for i in range(len(quiz)):
        array = quiz[i].split('=')
        array1 = array[0].split(' ')
        if array1[1] == '+' :
            res = int(array1[0]) + int(array1[2])
        else :
            res = int(array1[0]) - int(array1[2])
        b = array[1].strip() 
        
        if res == int(b):
            result.append('O')
        else:
            result.append('X')
        
    return result
        
    
    