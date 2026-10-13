def solution(myStr):
    # 접근 : 차례대로 a를 기준으로 자른 배열의 요소들에서 또 b를 기준으로 배열의 요소들을 자르고, c를 기준으로 배열의 요소들을 또 자르는 식으로 진행하였다. 
    
    # 배열 선언
    array = []
    Array = []
    
    # a를 기준으로 자르기
    answer = myStr.split('a')
    
    # a를 기준으로 자른 원소들을 다시 b를 기준으로 자르기
    for i in answer:
        if 'b' in i:
            array1 = i.split('b')
            array.extend(array1)
        else:
            array.append(i)
    
    # b를 기준으로 자른 원소들을 다시 c를 기준으로 자르기
    for j in array:
        if 'c' in j:
            array2 = j.split('c')
            Array.extend(array2)
        else:
            Array.append(j)
    
    # 만약 배열안에 ''가 있다면 제거해주기
    while(1):
        if '' in Array:
            Array.remove('')
        else:
            break
            
    # 만약 배열의 길이가 0이라면 'EMPTY'추가해주기
    if len(Array) == 0 :
        Array.append('EMPTY')
        
    # 정답 배열 반환하기
    return Array