'''
처음 경로가 ICN 마지막 경로가 정해진 문제가 아니라서 다익스트라는 제외
bfs를 사용해서 탐색을 진행

'''
from collections import deque

def solution(tickets):
    answer = []
    
    #알파벳 순서가 앞서는 경로가 return 되어야한다.
    tickets.sort()
    
    level = len(tickets)
    
    # ICN가 가장 먼저 출발
    queue = deque()
    for i in range(len(tickets)):
        start, end = tickets[i][0], tickets[i][1]
        if start =="ICN":
            queue.append((end,[end],[i]))
    
    answer.append("ICN")
    # bfs
    
    while(queue):
        
        start,before_list,visited = queue.popleft()
        
        if len(visited) == level:
            # print(visited)
            for before in before_list:
                answer.append(before)
            return answer
        
        for i in range(len(tickets)):
            ts, te = tickets[i][0], tickets[i][1]
            
            if start == ts:
                if i not in visited:
                    # print(before_list, te)
                    visited_temp = visited + [i]
                    before_list_temp = before_list + [te]
                    queue.append((te,before_list_temp,visited_temp))
        
    
    return answer

answer = solution([["ICN", "AAA"], ["ICN", "CCC"], ["CCC", "DDD"], ["AAA", "BBB"], ["AAA", "BBB"], ["DDD", "ICN"], ["BBB", "AAA"]])
print(answer)
