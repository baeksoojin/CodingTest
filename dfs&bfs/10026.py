'''
적록색약이 아닌 사람이 봤을 때의 bfs결과와 적록색약인 사람이 봤을 때의 bfs 결과를 모두 출력
4시 8분 시작 -> 36분 풀이완료

---
tuple에 색맹이 아닌 사람, 색맹인 사람이 느끼는 색을 차례로 저장

'''

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

colors1, colors2 = [],[]
visited1, visited2 = [[False]*n for _ in range(n)], [[False]*n for _ in range(n)]

for _ in range(n):
    color=input()
    colors1.append(color)
    color = list(map(lambda x : "R" if x=="G" else x, color))
    colors2.append(color)

checks = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs(queue, visited, colors):
    
    while(queue):
        
        x,y = queue.popleft()

        for check in checks:
            next_x = x+check[0]
            next_y = y+check[1]

            if next_x<0 or next_x>n-1  or next_y <0 or next_y>n-1:
                continue
            else:
                if colors[next_x][next_y] == colors[x][y] and visited[next_x][next_y]==False:
                    queue.append((next_x, next_y))
                    visited[next_x][next_y] = True

    return visited




queue1 = deque()
queue2 = deque()
cnt1, cnt2 = 0,0
for i in range(n):
    for j in range(n):
        if visited1[i][j]==False:
            queue1.append((i,j))
            visited1[i][j] = True
            cnt1 += 1
            visited1=bfs(queue1, visited1, colors1)
        if visited2[i][j]==False:
            queue2.append((i,j))
            visited2[i][j] = True
            cnt2 += 1
            visited2 = bfs(queue2, visited2, colors2)

print(cnt1, cnt2)