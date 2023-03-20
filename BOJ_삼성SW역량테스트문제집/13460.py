'''
구슬탈출2

빨간색공을 구멍에 넣어야하고 파란색 공이 빠지면 안 됨.
최소 몇 번만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 구해야함.
10번 이하로 움직였는데 빨간 구슬을 구멍에서 뺄 수 없다면 -1을 출력.

'''

'''

idea) bfs를 통해서 상,하,좌,우로 가는 모든 경우를 체크해야함

상하좌우로 움직일 수 있을 때 1칸씩 움직이는 것이 아니라 #을 만나기 직전까지 움직임
만약에 red 구슬이 visited체크를 할 때 더이상 갈 곳이 없을 경우, -1, cnt로 depth를 체크할 때 depthrk 10이상이 되었다면 stop
'''

from collections import deque

n,m = map(int, input().split())

b_queue = deque([])
r_queue = deque([]) 

visited = [[[[False]*(m) for _ in range(n)] for _ in range(m)] for _ in range(m)]

# 상,하,좌,우
move = [(-1,0),(1,0),(0,-1),(0,1)]

first = [0]*4
board = []

for i in range(n):
    board.append(input().strip())

for i in range(n):
    for j in range(m):
        if board[i][j]=="R":
            first[0], first[1] = i,j
            r_queue.append((i,j,1))
        if board[i][j]=="B":
            first[2], first[3] = i,j
            b_queue.append((i,j,1))

visited[first[0]][first[1]][first[2]][first[3]] = True

def moving(x, y, move):

    cnt=0
    is_out = False

    while board[x+move[0]][y+move[1]]!="#":
        
        cnt+=1
        x += move[0]
        y += move[1]
        if board[x][y]=="O":
            is_out=True


    return (x,y,cnt,is_out)

def bfs():

    result = -1
    
    while(r_queue):
        
        rx,ry,rcnt = r_queue.popleft()
        bx,by,bcnt = b_queue.popleft()
        
        if rcnt>10: # 10번 체크를 했는데 구멍이 없었을 때라면 -1을 리턴
            return result
        else:
            
            for m in move:
                # 빨간 구슬이 다음으로 갈 수 있는 위치를 계산 
                next_rx, next_ry, rstep, is_rout = moving(rx, ry, m)
                # 파란 구슬이 다음으로 갈 수 있는 위치를 계산
                next_bx, next_by, bstep ,is_bout = moving(bx,by,m)

                #빨간색 구슬과 파란색 구슬이 같은 위치에 존재할때
                # 많이 움직인 것을 뒤로 빼줌
                if next_rx==next_bx and next_ry==next_by:
                    if rstep> bstep: # 빨간색을 옮겨줘야하는 경우
                        next_rx -= m[0]
                        next_ry -=m[1]
                        
                    else:# 파란색 구슬을 옮겨주는 경우
                        next_bx -= m[0]
                        next_by -=m[1]
                
                # 파란색 공이 이동중에 빠지는 경우
                if is_bout:
                    continue
                
                if is_rout:
                    return rcnt

                if visited[next_rx][ next_ry][ next_bx][ next_by]!=True:
                    visited[next_rx][ next_ry][ next_bx][ next_by]=True
                    r_queue.append((next_rx, next_ry,rcnt+1))
                    b_queue.append((next_bx, next_by,bcnt+1))
            
    return result



result = bfs()
print(result)