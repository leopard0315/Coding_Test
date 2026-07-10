def solution(my_string):
    return sorted([int(c) for c in my_string if c.isdigit()])

# 숫자만 뽑기
# a.isdigit() 사용
# 문자만 뽑기
# a.isalpha() 사용