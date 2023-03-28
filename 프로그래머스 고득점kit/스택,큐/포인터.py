'''
queue를 사용해서 중요도가 높은게 뒤에 존재하는 경우 뒤로 다시 보냄
queue 안에 값이 없을 때까지 반복하고 더 큰게 없다면 -> answer에 저장

'''
from collections import deque

def solution(priorities, location):
    answer = 0
    answer_temp=[]
    
    queue = deque([])
    
    for i in range(len(priorities)):
        queue.append((i, priorities[i]))
        # location과 그 위치의 우선순위를 저장
    
    while(queue):
        
        current, pri = queue.popleft()
        
        is_print=True# 우선순위가 높은 것이 존재하는지 여부
        for loc_temp, pri_temp in queue:
            if pri_temp > pri:# 현재의 우선순위보다 더 높은것이 존재한다면 다시 queue에 저장
                is_print=False
                queue.append((current, pri))
                break
        if is_print==False:
            continue
        else:
            answer_temp.append(current)
        
    
    answer = answer_temp.index(location)+1
    print(answer)
    
        
    return answer