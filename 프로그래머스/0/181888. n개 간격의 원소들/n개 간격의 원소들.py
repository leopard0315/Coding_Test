def solution(num_list, n):
    # 정답을 담을 빈 배열 생성
    answer = []
    
    # for문을 사용 -> 간격이 n이 되도록 함
    for i in range(0,len(num_list),n):
        answer.append(num_list[i])
        
    # 정답 출력
    return answer

# 다른 사람 풀이
# def solution(num_list, n):
#     return num_list[::n]