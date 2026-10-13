def solution(myStr):
    array = []
    array_1 = []
    answer = myStr.split('a')
    for i in answer:
        if 'b' in i:
            array1 = i.split('b')
            array.extend(array1)
        else:
            array.append(i)
            
    for j in array:
        if 'c' in j:
            array2 = j.split('c')
            array_1.extend(array2)
        else:
            array_1.append(j)
    
    while(1):
        if '' in array_1:
            array_1.remove('')
        else:
            break
    if len(array_1) == 0 :
        array_1.append('EMPTY')
    return array_1