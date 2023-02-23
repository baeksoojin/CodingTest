'''
소년점프 -> bfs응용문제
----
수정)

bfs를 돌 때마다 cnt를 비교할 수 없음. -> cnt를 저장해놓고 이후에 한번에 비교를 해야함.

-----

핵심)
visited[i][j]값이 가장 큰 배열의 값이 세 악당이 모일때 걸린 시간임.



'''

from collections import deque

r,c = map(int, input().split())

maps = []

for i in range(r):
    maps.append(input().rstrip())

visited0 = [[0]*(c) for _ in range(r)]
visited1 = [[0]*(c) for _ in range(r)]
visited2 = [[0]*(c) for _ in range(r)]
visiteds = [visited0,visited1, visited2]

check_list = [(-1,0),(1,0),(0,1),(0,-1),]

def bfs(queue, visited):
    
    while(queue):
        a,b = queue.popleft()
        for check in check_list:
            next_a = a+check[0]
            next_b = b+check[1]

            if next_a>=0 and next_a<=r-1 and next_b >=0 and next_b<=c-1:
                if visited[next_a][next_b]==0 and maps[next_a][next_b] == '0':
                    visited[next_a][next_b] =  visited[a][b] +1
                    queue.append((next_a, next_b))

 

for i in range(3):
    queue = deque([])
    a,b = map(int, input().split())
    a-=1
    b-=1
    queue.append((a,b))
    visited = visiteds[i]
    visited[a][b] = 1
    bfs(queue,visited)

same_list = []

min_temp = 1e9
min_count = 0

# 같은 위치에 가도 되는 것을 처리
# 해당 자리에서 모두 0보다 크기만 하면 일단 -1은 아님 -> 같은자리에서 계속 있을 수도 있으니
# visited[i][j]값이 가장 큰 배열의 값이 세 악당이 모일때 걸린 시간임.
# 각 자리에서 세 악당이 모일 시간이 가장 작을 경우를 계속 업데이트해주고 해당 값일때의 경우의 수를 카운팅
for i in range(r):
    for j in range(c):
        if visited0[i][j]>0 and visited1[i][j]>0 and visited2[i][j]>0:
            temp_max = max(visited0[i][j],visited1[i][j],visited2[i][j] )
            if min_temp > temp_max:
                min_temp = temp_max
                min_count = 1
            elif min_temp == temp_max:
                min_count +=1
if min_temp!=1e9:
    print(min_temp-1)
    print(min_count)
else:
    print("-1")