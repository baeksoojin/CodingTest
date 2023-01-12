'''

visited : 방문했다면 True, 아니라면 False
노드가 1000일때 간선이 500개까지 받아지고 꽤나 많이 받아질 수 있기에 연결list를 사용하여 풀이진행.

for문으로 node를 돌면서 visited가 False일때 bfs를 동작시키고 counting 변수값을 증가 시킴.
'''

import sys
from collections import deque
input = sys.stdin.readline
two_input = lambda : map(int, input().split())

n,m = two_input()

linked_list = [[0]*(n+1) for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(m):
    a,b = two_input()
    linked_list[a][b]=1
    linked_list[b][a]=1

count = 0

def bfs(start):

    global count
    count += 1
    
    queue = deque([])
    queue.append(start)
    visited[start] = True

    while(queue):
        current = queue.popleft()
        linked_node = linked_list[current]

        for node in range(1,len(linked_node)):
            if linked_node[node] == 1 and visited[node]==False:
                visited[node]=True
                queue.append(node)
                
        

for node in range(1, n+1):
    if visited[node]==False:
        bfs(node)

print(count)



