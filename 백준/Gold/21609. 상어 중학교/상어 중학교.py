'''
상어 중학교 4월 9일 10시 시작

10시 20분까지 문제정리 --- 10시 15분까지 문제 이해완료.

10시 40분까지 예제 정리  & 알고리즘 구성 생각.


최소 11까지 알고리즘 정리 -> 완벽하게 되면 코드 작성 시작

----------

# tile 입력 초기화

# bfs(tile, queue, visited):

    group_temp = []
    rainbow_count = 0

    while
        탐색진행 -> group_temp에 pop한거 저장.
        queue에서 나온 좌표의 값이 0일때 -> rainbow_count +=1

    return group_temp, rainbow_count, visited

def find_group_block(tile):

    # rainbow_count =[]
    # group_list = [] -> 묶음의 (x,y)를 하나의 list에 저장해서 group_list에 저장

    # bfs
    # visited -> 전부 false로 초기화 -> 2차원
    for i in range(n):
        for j in range(n):
            if visited하지 않았거나, 양수일때(0일때도 안 됨. 0에서 시작할 수는 없음 -> 최소 1개의 일반 블록이 있어야함)
                queue -> x,y,cnt(1)로 해서 집어넣기
                group_temp, rainbow_temp, visited = bfs(tile, queue, visited) # visited update


    return group_list, rainbow_count

def gravity(tile):
    for i in range(n-1): # 마지막줄은 이동 불필요
        for j in n:
            temp_i = i
            while (temp_i >=0 and tile[temp_i+1]가 공백 -> -2인지 체크 and tile[temp_i] >=0 # 검정색 이동 불가):
                tile[temp_i+1] , tile[temp_i] =tile[temp_i],tile[temp_i+1]
                temp_i-=1
    return tile

while True:
    # 졷료조건
    # 1. 그룹을 찾는 bfs()실행. -> (음수일때는 안 됨 -> -1일때불가능 & -2일때는 공백이라 불가능) -> group_list를 return 하는데, group_list의 size가 0이라면? 종료
    group_list, rainbow_count = find_group_block(tile)
    if len(group_list) == 0 :
        return answer

    # 2. 그룹 중에서 최대그룹을 찾기.
    # group_list의 index와 동일한 위치에 sort_list []에 정렬조건들을 넣기 => group_count의 개수, 무지개블록수, 행, 열
    # sort_list를 sort하고 가장 앞에 있는 것의 index를 found
    # 찾은 Index를 가지고 group_list에서 뽑기
    # 배열에 저장된 좌표를 전부 -2 -> 공백처리 -> tile update
    # 그 크기만큼 제곱해서 -> answer에 업데이트

    # 3. 중력코드 작성
    tile = gravity(tile)

    # 4. 왼쪽 90도 회전을 3번
    for i in range(3):
        # 오른쪽 90도 회전
        tile = list(map(list, zip(*tile[::-1])))

    # 5. 중력코드 작성
    tile = gravity(tile)

------11시 4분에 작성 완료.
'''


# tile 입력 초기화

import sys
from collections import deque

input = sys.stdin.readline
n,m = map(int, input().split())

answer = 0
tile = []
for i in range(n):
    tile.append(list(map(int, input().split())))


# print(tile)

direction = [(-1,0), (1,0), (0,-1), (0,1)] # 상하좌우 차례대로

def bfs(tile, queue, visited):
    global n
    # print("bfs-----")

    group_temp = []
    rainbow_count = 0
    main_block = (100,100) #inf로 설정
    min_column= 100
    count = 0
    first = True
    color = 100 #temp

    while queue:
        # 탐색진행 -> group_temp에 pop한거 저장.
        # queue에서 나온 좌표의 값이 0일때 -> rainbow_count +=1

        current_x, current_y = queue.popleft()
        # print(current_x, current_y)
        count+=1
        if first:
            color = tile[current_x][current_y]
            first = False
        group_temp.append((current_x, current_y))
        if tile[current_x][current_y] == 0:
            rainbow_count +=1
        if current_x == main_block[0] and current_y < main_block[1] and tile[current_x][current_y]!=0: # 기준블록이 같다면 열의 번호가 가장 작은 블록으로 Update
            main_block = current_x, current_y
        if current_x < main_block[0] and tile[current_x][current_y]!=0: # 행이 작으면 그걸로 메인 블록
            main_block = current_x, current_y
        for dir in direction:
            next_x = current_x+dir[0]
            next_y = current_y + dir[1]
            if 0<=next_x<=n-1 and 0<=next_y<=n-1 and (tile[next_x][next_y]==0 or tile[next_x][next_y]==color) and visited[next_x][next_y]==False:
                visited[next_x][next_y] = True
                queue.append((next_x, next_y))
    flag = False
    if count >=2:
        flag = True
    return group_temp, rainbow_count, visited, main_block, flag

def find_group_block(tile):
    rainbow_count =[]
    group_list = [] # -> 묶음의 (x,y)를 하나의 list에 저장해서 group_list에 저장
    main_block_list = []
    min_column_list = []

    visited = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            # 일반 블록일때 시작 가능
            if visited[i][j] != True and (tile[i][j] > 0):
                visited[i][j] = True
                queue = deque([(i,j)])
                group_temp, rainbow_count_temp, visited, main_block ,flag = bfs(tile, queue, visited)

                # 0은 재사용 가능.
                for k in range(n):
                    for l in range(n):
                        if visited[k][l] and tile[k][l] == 0:
                            visited[k][l] = False
                if flag:
                    group_list.append(group_temp)
                    rainbow_count.append(rainbow_count_temp)
                    main_block_list.append(main_block)
    # print(group_list)
    return group_list, rainbow_count, main_block_list, min_column_list

def gravity(tile):
    global n
    for i in range(n-1): # 마지막줄은 이동 불필요
        for j in range(n):
            temp_i = i
            while (temp_i >=0 and tile[temp_i+1][j] == -2 and tile[temp_i][j] >=0): # 검정색 이동 불가):
                tile[temp_i+1][j] , tile[temp_i][j] = tile[temp_i][j],tile[temp_i+1][j]
                temp_i-=1

    # print("g -> ",tile)
    return tile

if n==1:
    if tile[0][0] > 1:
        print(1)
    else:
        print(0)
else:

    while True:
        # print('-----------')

        # for i in range(n):
        #     print(tile[i])

        # 졷료조건
        # 1. 그룹을 찾는 bfs()실행. -> group_list를 return 하는데, group_list의 size가 0이라면? 종료
        group_list, rainbow_count, main_block_list, min_column_list = find_group_block(tile)
        if len(group_list) == 0:
            print(answer)
            break

        # 2. 그룹 중에서 최대그룹을 찾기.
        # group_list의 index와 동일한 위치에 sort_list []에 정렬조건들을 넣기 => group_count의 개수, 무지개블록수, 행, 열

        list_for_sort = []
        for i in range(len(group_list)):
            group_block_count = len(group_list[i])
            group_rainbow_count = rainbow_count[i]
            main_block_i = main_block_list[i][0]
            main_block_j = main_block_list[i][1] #min_column_list[0]
            list_for_sort.append([i,group_block_count,group_rainbow_count, main_block_i,main_block_j])

        list_for_sort.sort(key = lambda x: (-x[1], -x[2], -x[3], -x[4]))

        # sort_list를 sort하고 가장 앞에 있는 것의 index를 found
        biggest_group_index = list_for_sort[0][0] # index 뽑기
        # 찾은 Index를 가지고 group_list에서 뽑기
        biggest_group_list = group_list[biggest_group_index]
        # 배열에 저장된 좌표를 전부 -2 -> 공백처리 -> tile update
        for i,j in biggest_group_list:
            tile[i][j] = -2 # 공백처리
        # 그 크기만큼 제곱해서 -> answer에 업데이트
        size = len(biggest_group_list)
        answer = answer + size**2

        # for i in range(n):
        #     print(tile[i])
        #
        # # 3. 중력코드 작성
        # print("gravity")

        tile = gravity(tile)
        # for i in range(n):
        #     print(tile[i])

        # 4. 왼쪽 90도 회전을 3번

        # print("-90 turn")
        for i in range(3):
            # 오른쪽 90도 회전
            tile = list(map(list,zip(*tile[::-1])))

        # for i in range(n):
        #     print(tile[i])
        #
        # # 5. 중력코드 작성
        # print("gravity")
        tile = gravity(tile)

        # for i in range(n):
        #     print(tile[i])
