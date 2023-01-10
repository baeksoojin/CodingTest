'''
토마토가 며칠이면 다 익게 되는지 최소 일수를 구해야한다.
bfs를 1인 위치에서 start 지점으로하여 -1이 아닐때 +1씩 더해가면서 채워나간다.
이때 1보다 큰 값이 이미 존재했다면 현재 업데이트 하려는 값과 비교하여 더 작은 값을 선택하면 된다.
'''
import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())

tomato = []*(m)
for i in range(m):
    tomato.append(list(map(int, input().split())))

map_list = [(-1,0),(+1,0),(0,-1),(0,+1)] # 상하좌우 이동

def tomato_bfs(x,y,count_list):

    visited =[[False]*(n) for _ in range(m)]
        
    queue = deque([])
    queue.append((x,y))

    count = deque([])
    count.append(0)

    visited[x][y]=False
    count_list[x][y] = 0

    while(queue):
        
        x,y = queue.popleft()
        c = count.popleft()

        for map in map_list:
            a,b = map
            next_x = x +a
            next_y = y +b
            
            if next_x >m-1 or next_x<0 or next_y > n-1 or next_y<0:
                continue
            elif tomato[next_x][next_y] == -1:
                continue
            else: #갈 수 있을 경우 min값을 비교하는 조건고려
                if visited[next_x][next_y]==False and c+1 < count_list[next_x][next_y]:
                    #print(next_x,next_y)
                    count_list[next_x][next_y] = c+1
                    queue.append((next_x, next_y))
                    count.append(c+1)
    return count_list

INF = int(1e10)
count_list =[[INF]*(n) for _ in range(m)]
for i in range(m):
    for j in range(n):
        if tomato[i][j]==1:
            count_list = tomato_bfs(i,j,count_list)

# min값으로 비교하는 것을 추가해야함

# 다 익을 수 없는 경우
if 0 in tomato:
    print("-1")
else:
    result = []
    for i in range(m):
        result += count_list[i]
    result = list(set(result))
    result.remove(INF)
    print(max(result))


# count_list의 초기값을 크게 해놔야 처음에업데이트됨

# test case의 경우 모두 정답으로 나오는 것을 확인함. 그러나 시간초과.