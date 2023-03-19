'''

한번의 시간을 기준으로 3개의 action이 가능

1. 다리위에 올라가기
2. 다리를 건너기
3. 다리를 빠져나가기

시간당 한칸씩 움직여야하니까 만약에 트럭이 못 올라오는 경우라면 queue에 0을 넣어주기
queue에 값 하나씩 넣으면서 왼쪽으로 옮기기 -> 만약 큐의 길이가 w가 된다면 가장 가까운 것을 제거

'''

# 모든 트럭들이 다리를 건너는 최단시간을 출력

from collections import deque

n,w,L = map(int, input().split())

trucks = list(map(int, input().split()))
queue1 = deque(trucks)
bridge = deque([])
time=0

while(queue1 or bridge):

    time+=1
    flag=True

    # 다리 위의 있는 트럭들을 움직이기
    if trucks:
        # 나갈 수 있다면 내보내기
        if len(bridge)==w:
            bridge.popleft()

        # 다리 위로 올릴 수 있다면 올리기
        if queue1:
            if sum(bridge)+queue1[0]<=L and len(bridge)+1<=w:
                bridge.append(queue1.popleft())
                
            else: # 올릴 수 없는 경우라면 다리 위의 트럭들만 옮겨주기
                bridge.append(0)
        else: # 트럭이 다리위에만 존재해서 한칸씩 움직이는 경우
            bridge.append(0)
            if sum(bridge)==0: # 다리 위에있던 트럭들이 다 빠져나간 경우
                flag=False
            
    if flag==False:
        break

print(time)
        