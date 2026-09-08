def solution(before, after):
    b_list = list(before)
    a_list = list(after)
    b_list.sort()
    a_list.sort()
    b_str = ','.join(b_list)
    a_str = ','.join(a_list)
    if b_str == a_str:
        return 1
    else:
        return 0