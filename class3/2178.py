'''
https://www.acmicpc.net/problem/2178

8시 50분 시작

시작위치, 도착위치를 포함해서 특정 위치로 도착할 때 지나야하는 최소 칸수.
bfs를 사용

1 -> 이동 O
0 - > 이동 X
시작위치  1,1

9시 14분 종료.

'''

import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())


# 모든 노드의 정점에서 배열 index 특성을 적용하여 -1을 적용하여 생성한다.
# 메모리 초과 방지 -> visited
graph = []
visited = [[0] * m for _ in range(n)]

for i in range(n):
    graph.append(input())
    
current_x, current_y = 0,0
current_cnt = 0 
visited[current_x][current_y] = 1

x_queue = deque([])
y_queue = deque([])
cnt_queue = deque([])

x_queue.append(current_x)
y_queue.append(current_y)
cnt_queue.append(1)

# 4가지 방향 정의
direct = [(-1,0), (1,0), (0,-1), (0, 1)] # 상, 하, 좌, 우

# bfs 시도
def bfs(x_queue, y_queue, cnt_queue):
    
    while(x_queue):
        
        current_x = x_queue.popleft()
        current_y = y_queue.popleft()
        current_cnt= cnt_queue.popleft()

        if current_x == n-1 and current_y == m-1:
            print(current_cnt)
            break
    
        # 4가지 방향으로 탐색시작

        for next_diff in direct:
            next_x = current_x + next_diff[0]
            next_y = current_y + next_diff[1]

            if (n-1 >= next_x >= 0) and (m-1 >= next_y >=0 ):
                if visited[next_x][next_y] !=1 and graph[next_x][next_y] == '1':
                    x_queue.append(next_x)
                    y_queue.append(next_y)
                    cnt_queue.append(current_cnt + 1)
                    visited[next_x][next_y] = 1

bfs(x_queue, y_queue, cnt_queue)