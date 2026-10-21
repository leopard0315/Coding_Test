def solution(arr, query): # 정수배열
    answer = []
    for i in range(len(query)):
        # 짝수 인덱스
        if i % 2 == 0:
            del arr[query[i]+1:]
        # 홀수 인덱스
        else:
            del arr[:query[i]]
    return arr