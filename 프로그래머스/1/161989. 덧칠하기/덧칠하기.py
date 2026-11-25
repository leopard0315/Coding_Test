# n 미터 벽
def solution(n, m, section):
    # 횟수를 세는 변수 선언
    count = 0 
    standard = 0
    
    for sect in section:
        if sect > standard:
            count += 1
            standard = sect + m - 1
    
    return count