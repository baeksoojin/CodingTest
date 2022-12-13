# 0과 1로 틀이 나눠져있을 때 0으로 이루어진 부분이 아이스크림 틀. 0 그룹의 개수를 찾기

# 53분 시작 -> 30분 끝 -> 약 10분 초과) 중간에 막힌 부분 : 상하좌우 다 갈 수 있어야하는데 elif로 만들어서 한 곳만 탐색함.
#cnt 정의
# for문으로 틀 하나씩 다 돌면서 1이 아닐때 queue를 통해서 그 영역을 체크 (bfs, dfs 무엇으로 해도 될듯.)
# If 0일 경우 cnt를 하나 증가시키고 bfs를 사용하고 이때 지나온 곳은 0으로 돌기

#for문을 나와서 cnt를 출력

# import sys
# from collections import deque
# n,m = map(int,sys.stdin.readline().split())

# graph =[]
# for i in range(n):
#     graph.append(list(map(int, input())))

# visited = [[0]*m for _ in range(n)]
# queue_x = deque()
# queue_y = deque()

# def bfs(i, j):
#     queue_x.append(i)
#     queue_y.append(j)
#     visited[i][j]=1
#     while(queue_x):
#         i = queue_x.popleft()
#         j = queue_y.popleft()

#         # 상하좌우 순서
#         if  i-1>=0 and graph[i-1][j]==0 and visited[i-1][j]!=1:
#             visited[i-1][j]=1
#             queue_x.append(i-1)
#             queue_y.append(j)
#         if i+1<n and graph[i+1][j] == 0 and visited[i+1][j]!=1:
#             visited[i+1][j]=1
#             queue_x.append(i+1)
#             queue_y.append(j)
#         if j-1>=0 and graph[i][j-1]==0 and  visited[i][j-1]!=1:
#             visited[i][j-1]=1
#             queue_x.append(i)
#             queue_y.append(j-1)
#         if j+1<m and graph[i][j+1]==0 and  visited[i][j+1]!=1:
#             visited[i][j+1]=1
#             queue_x.append(i)
#             queue_y.append(j+1)

# cnt=0
# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 0 and visited[i][j]==0:
#             print(i,j)
#             cnt += 1
#             bfs(i,j)
            
# print(cnt)

# 현재 bfs로 짰지만 dfs로 짜야 시간을 절약할 수 있는문제.


import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())

graph =[]
for i in range(n):
    graph.append(list(map(int, input())))

visited = [[0]*m for _ in range(n)]

def dfs(i,j):
    
    #갈 곳이 없는 경우를 처음에 미리 제거 -> 4가지 경우.
    if i+1>n-1 or i-1<0 or j-1<0 or j+1>m-1:
        return
    else:
        if visited[i+1][j]==0:
            visited[i+1][j]=1
            dfs(i+1, j)
        if visited[i-1][j]==0:
            visited[i-1][j]=1
            dfs(i-1,1)
        if visited[i][j-1]==0:
            visited[i][j-1] =1
            dfs(i, j-1)
        if visited[i][j+1]==0:
            visited[i][j-1]=1
            dfs(i, j+1)

cnt=0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and visited[i][j]==0:
            # print(i,j)
            cnt += 1
            dfs(i,j)
            
print(cnt)
