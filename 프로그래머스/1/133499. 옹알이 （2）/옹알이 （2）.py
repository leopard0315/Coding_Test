import re

def solution(babbling):
    regex = re.compile('^(aya|ye|woo|ma)+$')
    cnt = 0
    for babble in babbling:
        if regex.match(babble):
            if 'ayaaya' in babble or 'yeye' in babble or 'woowoo' in babble or 'mama' in babble:
                continue
            else:
                cnt += 1
    return cnt