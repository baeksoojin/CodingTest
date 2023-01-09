from collections import deque
from itertools import count

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

queue = deque([])

for _ in range(m):
    a,b= map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    count=0
    queue.append(start)
    visited[start]=True
    while(queue):
        temp = queue.popleft()
        count +=1
        
        for g in graph[temp]:
            if visited[g]==False:
                queue.append(g)
                visited[g]= True
    print(count-1)

bfs(1)
