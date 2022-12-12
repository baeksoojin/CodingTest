# bfs1 -> 오름차순으로 방문, 노드의 방문순서를 차례대로 출력
import sys
from collections import deque
n, m, r = map(int,sys.stdin.readline().split())

#초기화
visited = [0]*(n+1)
graph = [[] for _ in range(n+1)]

#인접리스트로 구현
for _ in range(m):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited[r] = 1
count = 2
queue = deque([r])
while(queue):
    temp = queue.popleft()
    graph[temp].sort(reverse=False)
    for i in graph[temp]:
        if visited[i]==0:
            visited[i] = count
            count += 1
            queue.append(i)

for i in visited[1:]:
    print(i)


