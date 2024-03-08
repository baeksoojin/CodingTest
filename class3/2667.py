'''
https://www.acmicpc.net/problem/2667



11시 22분 ~

bfs를 통해서 시작점을 바꿔가면서 탐색을 진행.
-> visited를 통해서 방문했는지를 체크

- 각 그룹별로 분류가 되어야 count가 가능하니까 group을 만들어서 숫자를 저장. group이 변경될때마다 (bfs가 재시작 될 때) cnt가 +1
12시 4분

'''

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

base_map = []
visited = [[0]*n for _ in range(n)]

for i in range(n):
    base_map.append(input())


direct = [(-1,0), (1,0), (0,-1), (0,1)] #상하좌우

def bfs(x_queue, y_queue, visited,cnt):

    cnt_temp = 0
    while(x_queue):
        # 4방향으로 이동
        cnt_temp +=1

        x_current = x_queue.popleft()
        y_currnet = y_queue.popleft()

        for d in direct:
            next_x = x_current+d[0]
            next_y = y_currnet+d[1]
            if n-1>=next_x>=0 and n-1>=next_y>=0:
                if visited[next_x][next_y] ==0 and base_map[next_x][next_y] == "1":
                    visited[next_x][next_y] = cnt
                    x_queue.append(next_x)
                    y_queue.append(next_y)

    return cnt_temp


# bfs를 실행할 시작점을 탐색하는 코드를 작성
cnt=0
cnt_temp =[]

for i in range(n):
    for j in range(n):
        if base_map[i][j] == "1" and visited[i][j]==0:
            cnt+=1
            x_queue = deque([i])
            y_queue = deque([j])
            visited[i][j] = cnt
            cnt_temp.append(bfs(x_queue, y_queue, visited, cnt))


print(cnt)
cnt_temp.sort()
for c in cnt_temp:
    print(c)
