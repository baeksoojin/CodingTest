'''
4시45분시작 
1. 시추관을 옮겨가며 각 위치마다(한칸마다) 석유 덩어리가 있는 곳일때 bfs를 시도 -> 3차원 loop의 개념
ex) for m -> for n -> bfs ==> 500*500*500 -> 125*100^6 -> 1초는 안 넘길듯?

2. 메모리제이션을 활용. 
bfs를 우선하고 각 위치마다 bfs의 결과의 저장(석유 덩어리) (이중 for, bfs) -> 석유 공간마다 그 공간에 연결된 총 덩어리 수를 저장해야함.
다음으로 for m -> for n하면서 합치기 ( 이중 for)
그룹별 값을 unique값을 저장하는 land_group 이중 배열을 생성

2번방법이 더 효율적

'''


from collections import deque

direct_diff = [(-1, 0), (1, 0), (0,-1), (0,1)] #상,하,좌,우
unique_group = [[0]*500 for _ in range(500)] #group의 id값을 저장
visited = [[0]*500 for _ in range(500)] # visited -> 1, non visitied -> 0

def bfs(land, queue, cnt_queue, group_index):
    total_cnt = 0
    n = len(land)
    m = len(land[0])
    print(n, m)
    
    while queue:
        
        current = queue.popleft()
        current_x, current_y = current[0], current[1]
        unique_group[current_x][current_y] = group_index
        total_cnt+=1
    
        current_cnt = cnt_queue.popleft()
        
        for d in direct_diff:
            next_x =  current_x + d[0]
            next_y = current_y + d[1]
         
            if 0<=next_x and next_x<=n-1 and next_y >=0 and next_y<=m-1:
                if visited[next_x][next_y]==0 and land[next_x][next_y]==1:
                    cnt_queue.append(current_cnt+1)
                    visited[next_x][next_y] = 1
                    queue.append((next_x, next_y))
                
    return total_cnt
        

def solution(land):
    
    n = len(land)
    m = len(land[0])
    
    queue = deque([])
    cnt_queue = deque([])
    total_cnt_by_group_index = dict()
    
    group_index = 1
    for i in range(n):
        for j in range(m):    
            if land[i][j] ==1 and visited[i][j] ==0 :

                queue.append((i,j))
                cnt_queue.append(0)
                visited[i][j] = 1
                total_cnt = bfs(land ,queue, cnt_queue, group_index)
                total_cnt_by_group_index[str(group_index)] = total_cnt
                group_index+=1
    
    # find

    max_count = 0
    for i in range(m):
        count = 0
        visited2 = [0]*(group_index) # 그룹별로 체크하기 위해 생성
        for j in range(n):
            if unique_group[j][i] !=0 and visited2[unique_group[j][i]]!=1:
                visited2[unique_group[j][i]]=1
                count+=total_cnt_by_group_index[str(unique_group[j][i])]
                
        max_count = max(max_count, count)
    
    return max_count
