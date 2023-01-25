'''

아기상어는 bfs를 통해서 먹이를 체크
상어의 몸무게가 체크하는 동선의 물고기들의 무게ㅂ다 클 때만 먹을 수 있고 만약 먹은 물고기의 몸무기에의 총합이 아기 상어의 무게와 같을 때 상어의 몸무게는 크기가 1증가.

가장 가까운 것을 먹으면 돼서 근처의 상하좌우부터 탐색하면 되는데 같은거리에 먹을 수 있는 물고기가 여러마리라면 가장 위의 물고가를 먹는데 이것도 여려마리라면 가장 왼쪽의 물고기를 먹음

상어는 9 자리에 위치하고 첫 무게는 2로 시작.
자기보다 큰 무게의 물고기는지나가지못함

먹으면 vistied reset(풀기)가 필요


---- 
먹이로 이동하고 다시 bfs를 시작하게끔 한다. bfs과정에서는 더 큰 무게의 물고기쪽으로는 가지 못하는 것을 체크해야함.

9가있는 위치에서 bfs를 시작 -> 가장 가까이 있는 자기보다 몸무게가 적게 나가는 물고기가 있는 좌표로 이동 -> 그 위치에서 bfs를 재시작. (bfs는 더이상 queue에 값이 없다면 끝나게되고 엄마를 호출함)
이때 가장 가까이 있는 물고기들이 여러마리일때 위쪽방향으로 이동하는데 현재에서 x좌표가 더 큰 쪽으로 이동함. 다만 이게 여러개일때 가장 왼쪽의 물고기를 먹음(y가 -방향) => x가 작은 것 먼저 이후 y가 작은 것을 선택
bfs를 통해서 4방향체크하는 단계를 거칠때마다 1초가 증가됨.


---
처음에 

6
5 4 3 2 3 4
4 3 2 3 4 5
3 2 9 5 6 6
2 1 2 3 4 5
3 2 1 6 5 4
6 6 6 6 6 6
case에서 정답이 58이 나옴 -> 상하좌우로 돌다가 발견되면 같은 단계(같은 level에 해당하는 연산)가 queue에 남아있어도 "상"쪽에서 나오면 바로 bfs 재귀를 시작해서 "하좌우"는 돌지 않음.
=> 같은 cnt(level)까지는 모두 돌게 해줘야함

--->> 20분 더 씀

---

'''

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
sea =[]


x,y = 0,0 #상어의 처음 위치를 저장

for i in range(n):
    temp = list(map(int, input().split()))
    sea.append(temp)
    if 9 in temp:
        j = temp.index(9)
        x=i
        y=j
        sea[x][y]=0



checks =[(-1,0),(0,-1),(1,0),(0,1)] #상좌하우
shark = 2
cnt =0 
prey_sum = 0

def bfs(x,y):

    # print("start ", x,y)

    global prey_sum
    global shark
    global cnt
    cnt_temp=0

    prey =[]
    visited =[[False]*n for _ in range(n)]

    queue = deque()
    queue.append((x,y,0))
    visited[x][y]=True

    if prey_sum==shark:
        shark += 1
        prey_sum =0

    stop = 1e9
    while(queue):
        x,y,cnt_temp = queue.popleft()
        if cnt_temp > stop:
            break
        
        for check in checks:
            next_x = x + check[0]
            next_y = y + check[1]

            if next_x<0 or next_x>n-1 or next_y<0 or next_y > n-1:
                continue
            if sea[next_x][next_y]>shark:
                continue
            if visited[next_x][next_y]==False:
                if sea[next_x][next_y]==0 or sea[next_x][next_y]==shark: #먹이를 먹지는 못하지만 지나갈 수 있는 경우
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y, cnt_temp+1))
                else:#먹이를 먹을 수 있는 경우
                    prey.append((next_x,next_y))
                    # print("prey list",(next_x,next_y),cnt_temp)
                    stop = cnt_temp

    if prey:
        temp_prey = sorted(prey, key=lambda x : (x[0],x[1]))[0]
        cnt += stop+1
        # print("get prey",temp_prey, cnt)
        prey_sum += 1
        sea[temp_prey[0]][temp_prey[1]]=0
        bfs(temp_prey[0],temp_prey[1])

            
bfs(x,y)
print(cnt)