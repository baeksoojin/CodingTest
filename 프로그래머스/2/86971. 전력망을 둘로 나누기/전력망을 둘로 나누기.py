from collections import deque

def bfs(node, graph):
    
    
    queue = deque()
    visited = [False] * 101
    queue.append(node)
    visited[node] = True
    
    linked_node_count = 0
    
    while queue:
        current_node = queue.popleft()
        linked_node_count +=1
        
        for next in graph[current_node]:
            if visited[next] != True:
                visited[next] = True
                queue.append(next)
                
    return linked_node_count
                


def solution(n, wires):
    answer = -1

    graph = [[] for i in range(101)]
    
    for wire in wires:
        a = wire[0]
        b = wire[1]
        graph[a].append(b)
        graph[b].append(a)
        
    min_temp = 10000
    
    for wire in wires:
        
        # 끊기
        a = wire[0]
        b = wire[1]
        graph[a].remove(b)
        graph[b].remove(a)
        
    
        a_linked_node = bfs(a, graph)
        b_linked_node = bfs(b, graph)
        
        min_temp = min(min_temp, abs(a_linked_node - b_linked_node))
        
        graph[a].append(b)
        graph[b].append(a)
        
    
    return min_temp