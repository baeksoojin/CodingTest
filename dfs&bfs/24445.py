#너비우선탐색 내림차순 순서대로 방문하고 i번째 줄에는 정점 i의 방문 순서를 출력

import sys
from collections import deque
n,m,r = map(int,sys.stdin.readline().split())

visited = [0]*(n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited[r] = 1
count = 2
queue = deque([r])

while(queue):
    temp = queue.popleft()
    graph[temp].sort(reverse=True)
    for i in graph[temp]:
        if visited[i] ==0:
            visited[i] = count
            count += 1
            queue.append(i)

for i in visited[1:]:
    print(i)