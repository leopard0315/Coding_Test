def solution(n, slicer, num_list):
    answer = []
    # 1. 정수 3개 배정해주기
    a,b,c = slicer
    
    # 2. n값에 따라 리스트 슬라이싱 진행
    if n == 1:
        return num_list[:b+1]
    elif n == 2:
        return num_list[a:]
    elif n == 3:
        return num_list[a:b+1]
    elif n == 4:
        return num_list[a:b+1:c]
    
    # 3. n이 1,2,3,4 이외에 값을 입력시 pass
    else:
        pass