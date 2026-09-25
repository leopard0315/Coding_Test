def solution(str1, str2):
    # str1이 str2의 부분문자열인지 확인
    if str1 in str2:
        return 1
    else:
        return 0