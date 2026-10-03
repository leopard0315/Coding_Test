def solution(myString):
    # 'x'를 기준으로 문자열 잘라내기 -> split()사용
    new_list = myString.split('x')
    
    # 생성한 배열 사전순으로 정렬하기
    new_list.sort()
    
    # 오름차순 정렬시에 ''가 앞에 오기 때문에 배열의 첫원소가 ''면 제거하고
    # 아니라면 반복문 중단
    while(1):
        if new_list[0] == '':
            new_list.pop(0)
        else:
            break
    
    # 배열 반환
    return new_list