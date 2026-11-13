# 이용료 price -> n번 이용시 price * n
# 일종의 누적합

def solution(price, money, count):
    num = 0
    cost = 0
    for i in range(count):
        num += 1
        cost += num * price

    return abs(money - cost) if money - cost < 0 else 0
        