def solution(arr, query): # 정수배열
    answer = []
    for i in range(len(query)):
        # 짝수 인덱스 - 기준 인덱스 이후의 부분 제거(del 사용)
        if i % 2 == 0:
            del arr[query[i]+1:]
        # 홀수 인덱스 - 기준 인덱스 이전의 부분 제거(del 사용)
        else:
            del arr[:query[i]]
    return arr