def solution(order):
    order = str(order)
    answer = 0
    return order.count('3') + order.count('6') + order.count('9')