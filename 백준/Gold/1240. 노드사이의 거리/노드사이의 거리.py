'''
노드 사이의 거리 2초
1000*1000*1000 -> 10의 12승 시간초과 -> for for X
1,2 사이의 거리 => 
3,2 사이의 거리 => 

거리를 이분탐색을 통해서 찾도록? 3 2일때 3과 2사이의 거리를 이분탐색으로 찾기 (시작점을 3 -> 시작점 탐색)
'''

from collections import deque
n, m = map(int, input().split())
graph = [[] for _ in range(1001)]

for _ in range(n-1):
    a,b,d = map(int, input().split())
    graph[a].append((b,d))
    graph[b].append((a,d))

# bfs
for i in range(m):
    a,b = map(int, input().split())

    queue = deque([])
    visited = [0]*1001
    visited[a] = 1
    queue.append((a, 0))
    while queue:

        current, current_dis = queue.pop()
        current_list = graph[current]

        for next,next_cost in current_list:
            if visited[next]==0:
                if next == b:
                    print(next_cost + current_dis)
                queue.append((next,next_cost + current_dis) )
                visited[next] =1
                
