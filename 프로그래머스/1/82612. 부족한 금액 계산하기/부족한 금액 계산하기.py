# 이용료 price -> n번 이용시 price * n
# 일종의 누적합

def solution(price, money, count):
    cost = 0
    for i in range(1,count+1):
        cost += i * price

    return abs(money - cost) if money - cost < 0 else 0
        