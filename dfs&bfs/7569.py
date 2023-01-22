'''

익은 토마토 주위를 "동시에"탐색해야 하기에 bfs에 해당 위치를 저장하고 bfs를 돌려야하고 bfs에 값이 없어질때까지 반복하고 끝났을 때의 bfs cnt값이 min값이됨.
=> 동시에 탐색하니까 이미 익은(방문한) 위치는 더 빨리익는게 당연하니까 visited 배열로 리셋되지 않도록 처리해야함
=> cnt를 bfs를 6칸 모두 돌면 그때 cnt+1을 해줘야함

2차원이 아닌 3차원으로 돌려야함.
k,i,j로 체크할 위치를 나타내기!

'''

import sys
from collections import deque
input = sys.stdin.readline

m,n,h = map(int, input().split())

box = []
for k in range(h):
    box_temp =[]
    for i in range(n):
        box_temp.append(list(map(int, input().split())))
    box.append(box_temp)
visited = [[[False]*(m) for _ in range(n)] for _ in range(h)]


queue , count = deque(), deque()

print(box)
print(visited)

#갈수있는곳
checks =[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]

cnt = 0
def bfs(queue):
    global cnt
    
    while(queue):
        k,i,j = queue.popleft()
        cnt = count.popleft()
        print(cnt)
        
        for a,b,c in checks:
            
            next_k = k + a
            next_i = i + b
            next_j = j + c

            if 0<=next_k <=h-1 and 0<=next_i<=n-1 and 0<=next_j<=m-1 and visited[next_k][next_i][next_j] != True:
                queue.append((next_k,next_i,next_j))
                count.append(cnt+1)
                visited[next_k][next_i][next_j] = True
                
    flag = True
    print(visited)
    for k in range(h):
        for i in range(n):
            if False in visited[k][i]:
                flag = False
    
    if flag == True:
        print(cnt)
    else:
        print("-1")

           

for k in range(h):
    for i in range(n):
        for j in range(m):
            if box[k][i][j] == 1:
                queue.append((k,i,j))
                visited[k][i][j]=True
                count.append(0)
            if box[k][i][j]==-1:
                visited[k][i][j] = True

bfs(queue)