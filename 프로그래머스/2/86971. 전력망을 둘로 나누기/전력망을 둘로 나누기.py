'''
solve 2
'''

from collections import deque

def bfs(linked_list, current, not_go):
    
    queue = deque()
    visited = [0]*len(linked_list)
    queue.append((current, 1))
    visited[current]=1
    
    max_cnt = 1
    
    while queue:
        
        current_node , current_cnt = queue.popleft()
        # print(current_node)
        # max_cnt = current_cnt if current_cnt > max_cnt else max_cnt
        
        next_list = linked_list[current_node]
        for next in next_list:
            if visited[next]==0 and next != not_go:
                queue.append((next, current_cnt+1))
                visited[next]=1
                max_cnt +=1
    return max_cnt

def solution(n, wires):
    answer = -1
    
    linked_list = [ [] for _ in range(n+1)]
    
    for wire in wires:
        linked_list[wire[0]].append(wire[1])
        linked_list[wire[1]].append(wire[0])
    
    diff_min = 100
    for wire in wires:
        # print(wire[0], wire[1])
        a = bfs(linked_list, wire[0], wire[1])
        b = bfs(linked_list, wire[1], wire[0])
        # print(a,b)
        diff_min = abs(a-b) if diff_min > abs(a-b) else diff_min
        
    return diff_min

