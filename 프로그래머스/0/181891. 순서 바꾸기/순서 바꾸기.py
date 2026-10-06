def solution(num_list, n):
    # 문자열 슬라이싱을 활용해서 n원소를 기준으로 위치 변경
    return (num_list[n:] + num_list[:n])
