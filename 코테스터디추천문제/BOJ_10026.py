'''
4시2분 시작

적록색약인 사람의 경우, 빨초를 하나의 영역으로 느낌 -> 'R'이나 'G'일때//'B'일때로 나눠서 cnt를 증가시키며 영역을 돌고 최종 cnt가 적록색약인 사람의 구역
적룍색약이 아닌 경우, 빨초파3가지 경우를 나눠서 체크
'''

from collections import deque
n = int(input())

n_list=[]

for i in range(n):
    n_list.append(input().rstrip())

checklist = [(-1,0),(1,0),(0,-1),(0,1)]

def bfs(queue,visited, n_list):
    
    while(queue):
        
        x,y = queue.popleft()

        for check in checklist:
            next_x = x + check[0]
            next_y = y + check[1]

            if next_x>=0 and next_x<=n-1 and next_y>=0 and next_y<=n-1:
                if n_list[x][y] == n_list[next_x][next_y] and visited[next_x][next_y]==False:
                    visited[next_x][next_y] = True
                    queue.append((next_x,next_y))
    

# 적록색약이 아닌 경우
cnt1=0
visited1 = [[False]*(n) for _ in range(n)]
queue1 = deque([])
for i in range(n):
    for j in range(n):
        if visited1[i][j]==False:
            queue1.append((i,j))
            cnt1+=1
            visited1[i][j]=True
            bfs(queue1,visited1,n_list)

#적록색약의 경우
cnt2=0
visited2 = [[False]*(n) for _ in range(n)]
queue2 = deque([])
n_list2 = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if n_list[i][j]=="R": 
            n_list2[i][j]="G"
        else:
            n_list2[i][j] = n_list[i][j]

for i in range(n):
    for j in range(n):
        if visited2[i][j]==False:
            queue2.append((i,j))
            cnt2+=1
            visited2[i][j]=True
            bfs(queue2,visited2,n_list2)

print(cnt1, cnt2)