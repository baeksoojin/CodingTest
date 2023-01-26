'''

1시 5분

queue에 1,2,3,4,5,6을 넣어놓고 cnt를 주어진 조건에 따라서 변경시키고 100번 칸에 딱 도착할 때까지 굴려야하는 횟수의 최솟값을 구하면 됨.

while , queue를 사용. while안에서 이동되는 좌표값이 특정 조건에 의해서 옮겨지는거여서 구현이 추가된 bfs문제라고 보면 될듯

'''

import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split()) #사다리랑 뱀의 수

n_list = {}
m_list = {}

for i in range(n+m):
    a,b = map(int, input().split())
    if i<n:
        n_list[a] = b
    else:
        m_list[a] = b
queue = deque([(1,0)])
visited =[False]*101

def bfs(queue):
    
    while(queue):
    
        current, cnt = queue.popleft()
        # print(current)

        if current==100:
            print(cnt)
            break

        for next_temp in range(1,7):
            next = current + next_temp
            if next<=100 and visited[next]==False:
            
                if next in n_list.keys():
                   next = n_list[next]
                if next in m_list.keys():
                   next = m_list[next]
                
                queue.append((next, cnt+1))
                visited[next]=True


bfs(queue)
        
        




