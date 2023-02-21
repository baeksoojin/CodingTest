# 사이즈가 크지 않기 때문에 인접리스트로 구현한다.

from collections import deque
n,m,v = map(int, input().split())

graph = [[]*(n+1) for _ in range(n+1)]
visited1 = [False]*(n+1) 
visited2 = [False]*(n+1) 

for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


stack = deque([])
stack.append(v)
visited2[v]=True

def dfs():

    node = stack.pop()
    print(node, end=" ")
    graph_temp = sorted(graph[node])

    for temp in graph_temp:
        if visited2[temp]!=True:
            visited2[temp] = True
            stack.append(temp)
            dfs()
dfs()
print()

queue = deque([])
queue.append(v)
visited1[v] = True

def bfs():

    while(queue):
        
        node = queue.popleft()
        print(node, end=" ")
        
        graph_temp = sorted(graph[node])
        for temp in graph_temp:
            if visited1[temp]!=True:
                visited1[temp]=True
                queue.append(temp)
                

bfs()
