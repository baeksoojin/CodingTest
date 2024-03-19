'''
규칙 ) 
다리서 트럭은 무게에 상관없이 1초 1칸 앞으로 가는데 칸의 수는 bridge_len과 관련됨
초를 변경해가며 1. on_bridge의 가장 앞의 것을 꺼냄. 2. 같은 시간유지하며, 조건에 맞다면 queue에 트럭을 올리고, 아니라면 0을 넣어서 개수를 맞춰줌. 3. ready_queue의 사이즈가 0일때 on_bridge의 sum이 0이라면? 다리를 전부 건넌거니까 count출력
'''

from collections import deque

def solution(bridge_length, weight, truck_weights):
    count = 0
    
    init_bridge = [0]*bridge_length
    on_bridge = deque(init_bridge)
    ready_queue = deque(truck_weights)
    sum_on_bridge = 0
    
    while True:
        if len(ready_queue)==0 and sum_on_bridge==0: # 끝
            break
        # pop
        out_truck = on_bridge.popleft()
        sum_on_bridge -=out_truck
        #print(count, "초 -> ",on_bridge.popleft(),"가 나감")
        # insert > 무게를 초과하지 않고 최대 허용 트럭 개수를 넘지 않을 때 옮기기
        if ready_queue:
            if sum_on_bridge+ready_queue[0] <= weight and len(on_bridge) < bridge_length:
                in_truck = ready_queue.popleft()
                on_bridge.append(in_truck)
                sum_on_bridge += in_truck
            else: # 0을 넣음
                on_bridge.append(0)
        else:
            on_bridge.append(0)
            
        count +=1
    
    return count

print(solution(100,100,[10]))

'''
처음에 다리 위에 올릴때마다 sum(on_bridge)를 해줌. 매번 해주니까 비효율적임!
memorization을 사용.메모이제이션써서 sum_on_bridge를 저장해놓자!
-> testcase 5 통과.

'''