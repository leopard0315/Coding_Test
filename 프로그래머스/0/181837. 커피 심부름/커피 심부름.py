def solution(order):
    # 접근: 아메리카노, 카페라떼, 아무거나 - 총 3가지 경우로 나눈다. (hot/ice는 구별 안하기 때문)
    total_money = 0 # 총금액 합산
    
    for i in order:
        # '아메리카노'인 경우
        if 'americano' in i:
            total_money += 4500
        # '카페 라떼'인 경우
        elif 'cafelatte' in i:
            total_money += 5000
        # '아무거나'인 경우
        else:
            total_money += 4500
    # 최종 금액 반환        
    return total_money