def solution(my_string):
    answer = [int(c) for c in my_string if c.isdigit()]
    answer.sort() # 정렬
    return answer

# 숫자만 뽑기
# a.isdigit() 사용
# 문자만 뽑기
# a.isalpha() 사용