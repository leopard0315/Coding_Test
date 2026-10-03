def solution(myString):
    # 'x'를 기준으로 문자열 잘라내기 -> split()사용
    new_list = myString.split('x')
    
    # 생성한 배열 사전순으로 정렬하기
    new_list.sort()
    
    while(1):
        if new_list[0] == '':
            new_list.pop(0)
        else:
            break
    
    # 배열 반환
    return new_list