'''
1시50분 시작 -> 2시 48분 제출시 런타임에러 -> 변경 후 틀렸습니다. -> get_tail을 수정해서 성공

벽 또는 자기자신의 몸과 부딪히면 게임 끝

맨위, 맨 좌측에서 시작 -> 처음 길이는 1, 오른쪽을 향함

초를 증가시키면서 몸길이를 늘려서 사과가 있는지 없는지 판단
if)사과(이동한 위치의 board값에 2가 존재한다다면)가있다면 
=> 꼬리를 고정시키고 머리를 해당 위치로 이동 -> 뱀이 위치한 곳을 모두 1로 처리하기
if) 사과가 없다면 -> 이동한 칸만 뱀의 위치를 표시(1로 표시)한다.

'''

from collections import deque


n= int(input())# 보드의 크기

board = [[0]*(120) for _ in range(120)]

k = int(input()) #사과의 개수
for i in range(k):
    a,b = map(int, input().split())
    board[a][b] = 2 # 사과가 있는 곳을 2라고함

l = int(input())# 뱀의 방향 변환 횟수
l_list = [False]*(10020) # 뱀이 방향을 변하는 정보를 담음

for i in range(l):
    time,dir = input().split()
    l_list[int(time)+1]= dir


time = 1
hx,hy = 1,1 # 뱀의 머리 위치
# 꼬리를 모두 queue에 저장하고 하나 없앨때마다 popleft()를 진행
tail = deque()
tail.append((hx,hy))
board[1][1]=1 # 뱀의 위치를 기록


dirs = [(-1,0), (0,1),(1,0),(0,-1)] # 차례대로 위(index 0)/오른쪽(index 1)/아래/왼쪽을 의미함
dir_index = 1 # 처음에는 오른쪽으로 이동하는 것이 고정 

def get_dir(time): # return dirs의 index

    global dir_index

    is_turn = l_list[time]
    
    if is_turn!=False:
        if is_turn=='D':
            dir_index = dir_index+1
            if dir_index==4:
                dir_index = 0
        else: #'L'일때
            dir_index = dir_index-1
            if dir_index==-1:
                dir_index = 3
    return dir_index

'''
만약에 오른쪽으로 90도 회전('D')한다면?

=> 다음에는 dirs의 index가+1
--> 왼쪽일때 오른쪽으로 회전한다면? +4인 index를 0으로 변경

만약에 왼쪽으로 90도 회전('L')한다면?
=> 다음에는 dirs의 index가 -1

--> 위일때 왼쪽으로 회전한다면? -1인 index가 됐다면 3으로 변경

'''

# 이동한 경로를 모두 저장해줘야함 -> 머리가 이동한 경로를 저장하고 앞의 것을 꺼내며니서 tail을 변경
def get_tail():

    tail.popleft()
    return tail[0]
    
while(1):

    # 다음으로 이동할 방향을 구함
    dir = dirs[get_dir(time)]
    hx, hy = hx+ dir[0], hy+dir[1]
    tx, ty = tail[0]


    # 멈추는 조건 적용
    # 머리가 위치한 곳이 이미 뱀이 있던 곳이라면(board의 값이 1일때) 혹은 borad를 벗어나 벽인 경우
    if hx<=0 or hx>n or hy<=0 or hy>n:# 벽
        answer = time
        break
    if board[hx][hy] ==1: # 이동한 곳이 뱀이 있던 곳
        answer = time
        break

    # 사과 여부에 따른 로직적용
    if board[hx][hy] ==2:# 사과가 존재
        # 사과를 먹고 1로 만들기(뱀의 자리로)
        board[hx][hy] = 1
        tail.append((hx,hy))
    else: # 사과가 없었다면 꼬리의 가장 마지막 부분을 0으로 변경
        board[hx][hy] = 1
        board[tx][ty] = 0
        tail.append((hx,hy))
        # 꼬리를 이동시켜줘야함
        tx,ty = get_tail()
        

    # time+1
    time+=1

     

print(answer)