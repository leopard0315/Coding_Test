def solution(my_string):
    # my_string안의 자연수들의 합을 담을 변수 저장
    total = 0
    
    # 만약 my_string의 원소가 문자라면 ''으로 대체한다. -> replace()함수 사용
    for i in range(len(my_string)):
        if my_string[i].isalpha():
            my_string = my_string.replace(my_string[i],' ')
    
    # 숫자만 남기기 위해서 문자열을 공백을 기준으로 쪼갠다.
    my_string_list = my_string.split()
    
    # 리스트안에 문자열로 된 숫자들의 합을 구하고 반환한다.
    for i in my_string_list:
        total += int(i)    
    return total
    