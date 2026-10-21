def solution(bridge_length, weight, truck_weights):
    # bridge_length : 다리의 길이 = 다리의 올라갈 수 있는 트럭의 수
    # weight: 다리에 올라갈 수 있는 트럭의 무게
    # truck_weights: 트럭의 
    # 한번에 한 트럭만 올라갈 수 있다.
    
    time = 0
    bridge = [0] * bridge_length # 현재 다리에 올라가있는 트럭의 리스트
    current_weight= 0
    
    while bridge:
        # 시간 1초씩 증가
        time += 1
        
        # 매 초마다 다리의 가장 맨 앞의 요소가 다리를 빠져나감
        current_weight -= bridge.pop(0)
        
        if truck_weights:
            # 다음 트럭이 진입해도 무게 제한이 넘지 않는 경우
            if current_weight + truck_weights[0] <= weight:
                next_truck = truck_weights.pop(0)
                bridge.append(next_truck)
                current_weight += next_truck
            else:
                bridge.append(0)
        
    return time
        