from collections import deque

def solution(progresses, speeds):
    answer = []
    
    # cnt를 1씩 증가해가면서 speed를 곱하고 100이상이 된다면 더이상 queue에 넣지않음..
    
    # 아니면 그냥 구현으로 일수를 우선 계산
    cnts=[0]*(len(progresses))
    
    while(True):
        flag = 0
        for i in range(len(progresses)):
            if progresses[i]>=100:
                flag +=1
                continue
            else: 
                cnts[i] +=1
                progresses[i]+=speeds[i]
                
        if flag == len(progresses): break
    print(cnts)
    
    queue = deque(cnts)
    
    i=0
    before = queue.popleft()
    answer.append(1)
    while(queue):
        current = queue.popleft()
        if current > before:
            i+=1
            answer.append(1)
            before = current
        else:
            answer[i] +=1
    print(answer)
    return answer