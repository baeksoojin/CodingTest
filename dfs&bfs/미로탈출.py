#최단거리-> bfs -> visited를 같이 넘기면서 체크해야하는 문제같음
#0,0에서 n-1,m-1로 가는 것.
#[30분 제한시간]2시 47분 시작 => 16분 끝. (1분 세이브....?)

# import sys
# from collections import deque
# n,m = map(int, sys.stdin.readline().split())
# visited = [[0]*m for _ in range(n)]
# cnt = [[0]*m for _ in range(n)] 

# #인접행렬로구현
# graph = []
# for i in range(n):
#     graph.append(list(map(int, sys.stdin.readline().strip())))

# queue_x = deque([0])
# queue_y = deque([0])
# visited[0][0] = 1
# cnt[0][0] = 1
# def bfs():
    
#     while(queue_x):

#         i = queue_x.popleft()
#         j = queue_y.popleft()
#         if i==n-1 and j==m-1:
#             print(cnt[i][j])
#             return
#         if i-1>=0 and visited[i-1][j] == 0 and graph[i-1][j]!=0:
#             queue_x.append(i-1)
#             queue_y.append(j)
#             cnt[i-1][j] = cnt[i][j]+1
#             visited[i-1][j]=1
#         if i+1<=n-1 and visited[i+1][j]==0 and graph[i+1][j]!=0:
#             queue_x.append(i+1)
#             queue_y.append(j)
#             cnt[i+1][j] = cnt[i][j]+1
#             visited[i+1][j]=1
#         if j-1>=0 and visited[i][j-1]==0 and graph[i][j-1]!=0:
#             queue_x.append(i)
#             queue_y.append(j-1)
#             cnt[i][j-1] = cnt[i][j]+1
#             visited[i][j-1]=1
#         if j+1<=m-1 and visited[i][j+1]==0 and graph[i][j+1]!=0:
#             queue_x.append(i)
#             queue_y.append(j+1)
#             cnt[i][j+1] = cnt[i][j]+1
#             visited[i][j+1]=1
        
                
# bfs()


#다만, visited에 애초에 visited값을 담아서 0일때와 아닐때로 visited를 체크하면 되니까 visited를 따로 만들지 않고 visited를 이용했어도됨.
#아래는 수정 후

import sys
from collections import deque
n,m = map(int, sys.stdin.readline().split())
visited = [[0]*m for _ in range(n)]

#인접행렬로구현
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip())))

queue_x = deque([0])
queue_y = deque([0])
visited[0][0] = 1
def bfs():
    
    while(queue_x):

        i = queue_x.popleft()
        j = queue_y.popleft()
        if i==n-1 and j==m-1:
            print(visited[i][j])
            return
        if i-1>=0 and visited[i-1][j] == 0 and graph[i-1][j]!=0:
            queue_x.append(i-1)
            queue_y.append(j)
            visited[i-1][j] = visited[i][j]+1
        if i+1<=n-1 and visited[i+1][j]==0 and graph[i+1][j]!=0:
            queue_x.append(i+1)
            queue_y.append(j)
            visited[i+1][j] = visited[i][j]+1
        if j-1>=0 and visited[i][j-1]==0 and graph[i][j-1]!=0:
            queue_x.append(i)
            queue_y.append(j-1)
            visited[i][j-1] = visited[i][j]+1
        if j+1<=m-1 and visited[i][j+1]==0 and graph[i][j+1]!=0: 
            queue_x.append(i)
            queue_y.append(j+1)
            visited[i][j+1] = visited[i][j]+1
        
                
bfs()

#풀이 확인
# 1. deque를 하나 만들어서 (,)로 튜플을 사용해서 값을 빼내기
# ex) x, y = queue.popleft()

# 2. if문 네개를 돌지 말고 for문을 4번 돌게하고 그 인자를 다르게 넘겨주기.
# => 그러기 위해서 인자를 담고있는 배열을 만들어줌. 배열을 2개 만들어서 i, j 를 각각 담고 이것으로 상,하,좌,우를 표현
# => 그러면 좋은 점은 for문이 생겨서 0,0에서 길이 없는 경우를 체크할때 continue를 해도 while문을 나가는게 아니라 다음 for문의 다음 index로 가기때문에 더 좋음 -> 어쨌든 4방향을 다 돌게 됨.continue
# =>=> 위에서 코드짤때 한번에 갈 수 없는 경우를 if문으로 먼저 체크했는데 답이 안 나왔던 이유가 0,0에서 처음으로 갈 수 없는 경우에 막혀서 continue하면 4방향중 3방향은 가지 않는 문제가 있어서 visited체크할때 함께 적어주는 줬었음


# import sys
# from collections import deque
# n,m = map(int, sys.stdin.readline().split())
# visited = [[0]*m for _ in range(n)]

# #인접행렬로구현
# graph = []
# for i in range(n):
#     graph.append(list(map(int, sys.stdin.readline().strip())))

# queue = deque([(0,0)])
# visited[0][0] = 1

# di = [-1,1,0,0]
# dj = [0,0,-1,1]

# def bfs():
    
#     while(queue):

#         i ,j = queue.popleft()

#         for temp in range(4):

#             x = i + di[temp]
#             y = j + dj[temp]
        
#             if x==n-1 and y==m-1:
                
#                 print(visited[i][j]+1)
#                 return

#             if x<0 or x>n-1 or y<0 or y>m-1 or graph[x][y]==0:
#                 continue
#             if visited[x][y]==0:
#                 queue.append((x,y))
#                 visited[x][y] = visited[i][j]+1
        
                
# bfs()