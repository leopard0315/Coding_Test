def solution(common):
    # 등차인 경우 / 등비인경우
    # 1. 등차인 경우
    if (common[0] + common[2]) == (2 * common[1]) :
        diff = common[1] - common[0]
        return common[-1] + diff
    # 2. 등비인 경우
    else :
        diff = common[1] // common[0]
        return common[-1] * diff