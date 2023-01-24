'''
4번의 깊이우선 탐색을 진행하면서 만들 수 있는 테트로미노는 5개 중에서 ㅜ 를 제외한 4개이고 ㅜ는 직접 구현을 통해서 체크해야함(대칭, 회전도 고려해야함)

ㅜ의 경우 탐색방법

1 2 3
  4
라고 할때 1번을 기준으로 회전하면 총 4가지

최대 4*500의 좌표 =>  ( 2000개의 좌표를 4번씩 체크하니까 8,000의 연산이 발생) 최대 8000번의 연산

'''

'''

import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())

paper = []

for i in range(n):
    paper.append(list(map(int, input().split())))

check_list = [(-1,0),(1,0),(0,-1),(0,1)] #선끼리 인접하도록 4방향만 탐색
check_list2 = [(-1,0),(1,0),(0,-1),(0,1),(-1,0),(1,0)] # ㅜ체크할때 사용

max_temp = 0


def dfs(stack, visited):

    global max_temp

    x,y,cnt,sum = stack.pop()
    sum += paper[x][y]
    if cnt==4:
        # print(sum)
        if max_temp < sum:
            max_temp = sum
            # print("max",max_temp)
        return

    for check in check_list:
        next_x = check[0] + x
        next_y = check[1] + y

        if 0<=next_x<=n-1 and 0<=next_y<=m-1 and visited[next_x][next_y]==False:
            # dfs를 통해서 다음칸으로 이동
            visited[next_x][next_y]= True
            stack.append((next_x, next_y, cnt+1, sum))
            dfs(stack, visited)


def another(x,y):

    global max_temp

    for i in range(4): # 총 4번 체크
        sum_temp = paper[x][y]
        for j in range(i, i+3):
            next_x = check_list2[j][0] + x
            next_y = check_list2[j][1] + y

            if 0<=next_x<=n-1 and 0<=next_y<=m-1:
                sum_temp += paper[next_x][next_y]
            else:
                break
                
        max_temp = max(sum_temp, sum_temp)
        # print("another", max_temp)


for i in range(n):
    for j in range(m):
        #4개의 테트로미노에 대해 dfs진행
        visited=[[False] * m for _ in range(n)]
        stack = deque()
        stack.append((i,j,1,0))
        visited[i][j] = True
        dfs(stack, visited)

        #ㅜ모양

        another(i,j)


print(max_temp)
        

시간초과나옴.,.!!!


'''

import sys
input = sys.stdin.readline

n,m = map(int,input().split())

paper = []

for i in range(n):
    paper.append(list(map(int, input().split())))

check_list = [(-1,0),(1,0),(0,-1),(0,1)] #선끼리 인접하도록 4방향만 탐색
check_list2 = [(-1,0),(1,0),(0,-1),(0,1),(-1,0),(1,0)] # ㅜ체크할때 사용

max_temp = 0

visited=[[False] * m for _ in range(n)]

def dfs(x, y, cnt, sum):

    global max_temp

    sum += paper[x][y]
    if cnt==4:
        # print(sum)
        if max_temp < sum:
            max_temp = sum
            # print("max",max_temp)
        return

    for check in check_list:
        next_x = check[0] + x
        next_y = check[1] + y

        if 0<=next_x<=n-1 and 0<=next_y<=m-1 and visited[next_x][next_y]==False:
            # dfs를 통해서 다음칸으로 이동
            visited[next_x][next_y]= True
            dfs(next_x, next_y, cnt+1, sum)
            visited[next_x][next_y]= False


def another(x,y):

    global max_temp

    for i in range(4): # 총 4번 체크
        sum_temp = paper[x][y]
        for j in range(i, i+3):
            next_x = check_list2[j][0] + x
            next_y = check_list2[j][1] + y

            if 0<=next_x<=n-1 and 0<=next_y<=m-1:
                sum_temp += paper[next_x][next_y]
            else:
                break
                
        max_temp = max(max_temp, sum_temp)


for i in range(n):
    for j in range(m):
        #4개의 테트로미노에 대해 dfs진행
        visited[i][j] = True
        dfs(i,j, 1,0)
        visited[i][j] = False

        #ㅜ모양
        another(i,j)


print(max_temp)