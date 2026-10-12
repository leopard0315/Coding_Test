def solution(myString, pat):
    # count 변수 선언 및 초기화
    count = 0
    # for문 범위설정
    for i in range(len(myString) - len(pat)+1):
        # 잘라낸 문자열이랑 pat이 일치하는지 확인
        # 맞으면 count값 1씩 증가하기
        if myString[i:i+len(pat)] == pat:
            count += 1
    # 정답 반환
    return count