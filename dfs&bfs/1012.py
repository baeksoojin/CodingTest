# 40분시작 -> 25분 끝 -> 45분 걸림 =>[시간초과 원인] bfs로 풀었는데 문제에서 줄의 개수를 먼저 입력받는줄 착각해서 n,m을 반대로 입력받고 풀고있었음 & 갈 수 없는 길일때 처리를 while밖에서 해버렸었음..
# 서로 인접한 배추의 영역의 개수가 흰지렁이가 놓여야할 개수 -> 인접한 배추묶음의 개수를 찾는 문제로 bfs로 접근하도록한다.
# 2500까지의 배추가 심어진 개수가 주어지고 50*50의행렬이니까 배추의 입력이 많이 들어올 수 있으니 인접행렬을 사용하도록한다.

import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

next = [(-1,0),(1,0),(0,+1),(0,-1)] # 상하좌우 이동

def bfs(n,m,k):
    count = 0
    graph = [[0]*m for _ in range(n)] # 인접행렬을 구현하여 배추가 있는 위치를 1로 체크하여 저장
    visited = [[False]*m for _ in range(n)] # 이미 접근한 곳은 visitied 2차원 행렬을 True로 변경

    for i in range(k):
        a,b = map(int, input().split())
        graph[b][a] = 1

    queue = deque([])
    
    # 인접행렬 graph를 한칸씩 돌면서 1인곳이면서(배추가존재) visited가 아닐때 묶음을 찾기 시작(dfs를 시작)
    for i in range(n):
        for j in range(m):
            if graph[i][j]==1 and visited[i][j]==False:
                
                queue.append((i,j))
                visited[i][j]=True
                count += 1

                while(queue):
                    a,b = queue.popleft()
                    for k in next:
                        if a+k[0]<0 or a+k[0] > n-1 or b+k[1] <0 or b+k[1] > m-1:
                            continue
                        if visited[a+k[0]][b+k[1]] == False and graph[a+k[0]][b+k[1]]==1 :
                        
                            visited[a+k[0]][b+k[1]] = True                            
                            queue.append((a+k[0],b+k[1]))


    print(count)

for i in range(t):
    a,b,c = map(int, input().split())
    bfs(b,a,c)
    


