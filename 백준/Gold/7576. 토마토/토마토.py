
import sys
from collections import deque
from tabnanny import check

input = sys.stdin.readline

n,m = map(int, input().split())

tomato = []*(m)
for i in range(m):
    tomato.append(list(map(int, input().split())))

map_list = [(-1,0),(+1,0),(0,-1),(0,+1)] # 상하좌우 이동

visited =[[False]*(n) for _ in range(m)]
queue = deque([])
counting = deque([])
def tomato_bfs(queue, counting):
    count = 0
    while(queue):
        
        x,y = queue.popleft()
        count = counting.popleft()

        for map in map_list:
            a,b = map
            next_x = x +a
            next_y = y +b
            
            if next_x >m-1 or next_x<0 or next_y > n-1 or next_y<0:
                continue
            else: 
                if visited[next_x][next_y]==False:
                    visited[next_x][next_y]=True
                    queue.append((next_x, next_y))
                    counting.append(count + 1)
    return count


INF = int(1e10)
for i in range(m):
    for j in range(n):
        if tomato[i][j]==1:
            queue.append((i,j))
            counting.append(0)
            visited[i][j]=True
        if tomato[i][j]==-1:
            visited[i][j] = True
result = tomato_bfs(queue,counting)

def check_minus():
    for v in visited:
        if False in v:
            return 1
    return 0

if check_minus():
    print("-1")
else:
    print(result)