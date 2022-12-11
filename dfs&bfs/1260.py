n, m, v = map(int, input().split())

visited_dfs = []
visited_bfs = []
# 1줄씩 더 만들어서 0 index는 사용하지 않음
graph = [[0]*(n+1) for _ in range(n+1)]

#인접행렬 만들기
for i in range(0, m):
    v1, v2 = map(int, input().split())
    #양방향
    graph[v1][v2] = 1
    graph[v2][v1] = 1 

#dfs -> stack or 재귀를 사용.
list_dfs = []

def dfs(start):
    
    visited_dfs.append(start)
    print(start, end=" ")
    
    for i in range(0,n+1):
        if graph[start][i]==1 and (i not in visited_dfs):
            dfs(i)

#bfs -> queue 
from  collections import deque
def bfs(start):
    print("")
    visited_bfs.append(start)
    queue = deque([start])
    
    while(queue):
        v = queue.popleft()
        print(v, end=" ")
        for i in range(0,n+1):
            if graph[v][i]==1 and (i not in visited_bfs):
                queue.append(i)
                visited_bfs.append(i)

        

dfs(v)
bfs(v)