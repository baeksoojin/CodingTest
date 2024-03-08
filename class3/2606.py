'''
https://www.acmicpc.net/problem/2606

3월 8일. 10시50분~11시4분


한 컴퓨터가 걸리면 연결된 곳에 퍼지는 바이러스.

bfs를 통해서 집합의 묶음을 찾아내면 될듯?
1번 컴퓨터를 통해서 웜 바이러스에 감염되는 것을 찾기

'''

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())

# 인접 행렬을 사용 -> n=100

graph = [[0]*101 for _ in range(101)]
visited = [0]*101

for i in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

start_node = 1
visited[1] = 1

queue = deque([])
queue.append(start_node)

def bfs(queue, visited):

    while(queue):
        current_node = queue.popleft()

        for i in range(n+1):
            if graph[current_node][i] ==1 and visited[i]!=1 : # 연결된 노드가 방문하지 않았던 곳이라면 바이러스 전염
                visited[i]=1
                queue.append(i)

bfs(queue, visited)

check_count_list = visited[2:n+1]
print(sum(check_count_list))




