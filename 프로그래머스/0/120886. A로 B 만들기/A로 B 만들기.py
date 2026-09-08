def solution(before, after):
    # 문자열을 리스트로 쪼갠후에 오름차순 정렬
    b_list = sorted(before)
    a_list = sorted(after)

    # 재조합된 문자열이 일치하는지 확인
    if b_list == a_list:
        return 1
    else:
        return 0