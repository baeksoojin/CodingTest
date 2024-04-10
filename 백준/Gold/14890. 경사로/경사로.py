'''
4월 10일 수요일 5시 35분 시작

------5시 55분까지 문제 이해---
문제이해 5시 44분 완료.

-----6시 15분까지 예제 이해----
5시 56분까지 예제 이해 완료.

-----6시 35분까지 알고리즘 도식화---

import math
count = 2*n # answer
# 지도초기화 필요
maps = [[]]

# 넘어온 시작점에서 시작해서 directin방향으로 사다리를 놓을 수 있는지 체크하는 함수
dev check_ladder((x,y), (diff_x, diff_y), L, visited):
    global maps
    # 시작점인 x,y에서 시작
    current_x = x
    current_y = y
    visited_temp = copy.deepcopy(visited)
    if L==1:
        visited[current_x][current_y] = 1
        return (True, visited)
    else:
        for i in range(L-1): # 1을빼는 이유는 이미 1차이가 나는 곳부터 시작하는 중이기에 1개는 이미 놓여진 상태.
            next_x = current_x + diff_x
            next_y = current_y + diff_y
            # 사다리를 놓을 수 있는 경우
            if maps[next_x][next_y] == maps[current_x][current_y] and 0<=next_x<=n-1 and 0<=next_y<=n-1 and visited[next_x][next_y]==0:
                visited_temp[next_x][next_y] = 1
            else: # 사다리를 놓을 수 없는 경우
                return (False, visited)
        return (True, visited_temp)



# 행에서 찾기 -> 사다리는 좌, 우로만 놓을 수 있다.
Ladder_direction = [(0,-1),(0,1), (-1, 0),(1,0)] # 좌, 우로 이동 / 상,하로 이동
for i in range(n):
    # i번째 길에 대해 초기화
    flag = True # flag가 false일때 그 길은 지나갈 수 없는 곳.
    before = maps[0][i]
    visited = [0]*(n) # 각 길마다 사다리가 놓여져있는지 체크.
    for j in range(1, n): # 행을 i로 고정하고 열 1칸1칸 탐색
        current = maps[i][j]
        # current와 다른지 체크하고 다르다면 둘중 작은쪽을 체크. -> 작은 쪽에서 연속된 L개가 존재하는지 체크. visited 처리가 안 되어있는지 체크
        # 1. 다른데 , 높이 차이가 2이상나는 경우 -> break
        if math.abs(before - current) >= 2:
            flag = False
            break
        if math.abs(before - current)==1 :
            if before < current: # 좌쪽에 사다리를 놓아야함.
                flag, visited = check_ladder((i, j-1)), L_direction[0], L, visited)
            else: # 현재쪽에서부터 사다리를 놓아야함
                flag,visited = check_ladder((i, j)), L_direction[1], L, visited)
            if flag == False:
                break
        # 높이차이가 2이상이 아니고 1차이나는게 아니라면 0차이 -> 다음 for문으로 진행 -> 아무것도 필요없음.

    if flag == False:
        count -=1

# 열에서 찾기 -> 사다리는 상, 하로만 놓을 수 있다.
for i in range(n):
    # i번째 길에 대해 초기화
    flag = True # flag가 false일때 그 길은 지나갈 수 없는 곳.
    before = maps[i][0]
    visited = [0]*(n) # 각 길마다 사다리가 놓여져있는지 체크.
    for j in range(1, n): # 열을 i로 고정하고 행을 1칸1칸 늘려가며 탐색
        current = maps[j][i]
        # current와 다른지 체크하고 다르다면 둘중 작은쪽을 체크. -> 작은 쪽에서 연속된 L개가 존재하는지 체크. visited 처리가 안 되어있는지 체크
        # 1. 다른데 , 높이 차이가 2이상나는 경우 -> break
        if math.abs(before - current) >= 2:
            flag = False
            break
        if math.abs(before - current)==1 :
            if before < current: # 좌쪽에 사다리를 놓아야함.
                flag, visited = check_ladder((j-1, i)), Ladder_direction[2], L, visited)
            else: # 현재쪽에서부터 사다리를 놓아야함
                flag,visited = check_ladder((j, i)), Ladder_direction[3], L, visited)
            if flag == False:
                break
        # 높이차이가 2이상이 아니고 1차이나는게 아니라면 0차이 -> 다음 for문으로 진행 -> 아무것도 필요없음.

    if flag == False:
        count -=1

----6시 35분까지 알고리즘 개요 도식화 완료-----
'''


# import math
# count = 2*n # answer
# # 지도초기화 필요
# maps = [[]]

# 1. 초기화

import sys, copy
input = sys.stdin.readline

n, L = map(int, input().split())
maps = []
for i in range(n):
    maps.append(list(map(int, input().split())))

Ladder_direction = [(0,-1),(0,1), (-1, 0),(1,0)] # 좌, 우로 이동 / 상,하로 이동
if n==1:
    count = 1
else:
    count = 2*n

# 넘어온 시작점에서 시작해서 directin방향으로 사다리를 놓을 수 있는지 체크하는 함수
def check_ladder(current, diff, L, visited):
    global maps
    # 시작점인 x,y에서 시작
    current_x = current[0]
    current_y = current[1]
    if (0<=current_x<=n-1 and 0<=current_y<=n-1 and diff[0] == 0 and visited[current_y] == 0 ):  # 행은 고정이고 열이 움직일대, 열은 고정이고 행이 움직일때
        visited[current_y] = 1
    elif ( 0<=current_x<=n-1 and 0<=current_y<=n-1 and diff[1] == 0 and visited[current_x] == 0 ):
        visited[current_x] = 1
    else: # 사다리를 놓는 첫 위치에 이미 사다리가 존재
        return (False, [])

    visited_temp = copy.deepcopy(visited)
    for i in range(L-1): # 1을빼는 이유는 이미 1차이가 나는 곳부터 시작하는 중이기에 1개는 이미 놓여진 상태.
        next_x = current_x + diff[0]
        next_y = current_y + diff[1]
        # print("next -> ", next_x, next_y)
        # 사다리를 놓을 수 있는 경우
        if 0<=next_x<=n-1 and 0<=next_y<=n-1 and maps[next_x][next_y] == maps[current_x][current_y]:
            if (diff[0] == 0 and visited[next_y] == 0): # 행은 고정이고 열이 움직일대, 열은 고정이고 행이 움직일때
                visited_temp[next_y] = 1
            elif (diff[1] == 0 and visited[next_x] == 0):
                visited_temp[next_x] = 1
            else:
                return (False, [])
        else: # 사다리를 놓을 수 없는 경우
            return (False, [])
        current_x = next_x
        current_y = next_y
    return (True, visited_temp)

# 행에서 찾기 -> 사다리는 좌, 우로만 놓을 수 있다.
for i in range(n):
    # print("i->", i)
    # i번째 길에 대해 초기화
    flag = True # flag가 false일때 그 길은 지나갈 수 없는 곳.
    before = maps[i][0]
    visited = [0]*n # 각 길마다 사다리가 놓여져있는지 체크.
    for j in range(1, n): # 행을 i로 고정하고 열 1칸1칸 탐색
        # print(i,j)
        current = maps[i][j]
        # current와 다른지 체크하고 다르다면 둘중 작은쪽을 체크. -> 작은 쪽에서 연속된 L개가 존재하는지 체크. visited 처리가 안 되어있는지 체크
        # 1. 다른데 , 높이 차이가 2이상나는 경우 -> break
        if abs(before - current) >= 2:
            flag = False
            break
        if abs(before - current)==1 :
            if before < current: # 좌쪽에 사다리를 놓아야함.
                # print("left")
                flag, visited = check_ladder((i, j-1), Ladder_direction[0], L, visited)
                # print("flag -> ", flag)
            else: # 현재쪽에서부터 사다리를 놓아야함
                # print("right")
                flag,visited = check_ladder((i, j), Ladder_direction[1], L, visited)
                # print("flag -> ", flag)
            if flag == False:
                break
        before = current
        # 높이차이가 2이상이 아니고 1차이나는게 아니라면 0차이 -> 다음 for문으로 진행 -> 아무것도 필요없음.

    if flag == False:
        # print("false-> " , i)
        count -=1

# 열에서 찾기 -> 사다리는 상, 하로만 놓을 수 있다.
for i in range(n):
    # i번째 길에 대해 초기화
    flag = True # flag가 false일때 그 길은 지나갈 수 없는 곳.
    before = maps[0][i]
    visited = [0]*(n) # 각 길마다 사다리가 놓여져있는지 체크.
    for j in range(1, n): # 열을 i로 고정하고 행을 1칸1칸 늘려가며 탐색
        current = maps[j][i]
        # current와 다른지 체크하고 다르다면 둘중 작은쪽을 체크. -> 작은 쪽에서 연속된 L개가 존재하는지 체크. visited 처리가 안 되어있는지 체크
        # 1. 다른데 , 높이 차이가 2이상나는 경우 -> break
        if abs(before - current) >= 2:
            flag = False
            break
        if abs(before - current)==1 :
            if before < current: # 좌쪽에 사다리를 놓아야함.
                flag, visited = check_ladder((j-1, i), Ladder_direction[2], L, visited)
            else: # 현재쪽에서부터 사다리를 놓아야함
                flag,visited = check_ladder((j, i), Ladder_direction[3], L, visited)
            if flag == False:
                break
        before = current
        # 높이차이가 2이상이 아니고 1차이나는게 아니라면 0차이 -> 다음 for문으로 진행 -> 아무것도 필요없음.

    if flag == False:
        # print("false-> ", i)
        count -=1

print(count)

