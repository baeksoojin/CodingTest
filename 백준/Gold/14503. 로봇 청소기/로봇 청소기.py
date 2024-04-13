'''
로봇청소기 : 5시 13분 시작

5시 33분까지 문제 이해----
문제 이해 5시 23분에 피니쉬.

5시 55분까지 예제 이해----
예제 이해 완료.

6시 15분까지 문제 알고리즘 정리----

bfs를 사용

# <초기화>
answer = 1
# 1. 입출력
maps => 초기화 / -> maps 0일때 빈칸, 탐색한 칸은 2(다만, 후진은 가능), 탐색 불가능은 (벽) -> 1
# 2. 현재위치를 current_x, current_y에 저장

# 3. current_direction_index 초기화
directions = [(-1,0), (0,1),(1,0),(0,-1)] # 북, 동, 남, 서

# <while문이 끝날때까지 탐색>

while True:

    # 탐색가능한 곳이 있다면 break해서 while문을 continue
    flag = False
    next_x, next_y = 0,0 # temp값
    # 탐색 위치를 변경하면서 탐색 가능한 곳을 찾았다면? -> continue를 통해서 아래 실행문 중단.
    for i in range(4):
        next_direction_index = (4 - (current_direction_index - i)) % 4
        next_x = current_x + direction[next_direction_index][0]
        next_y = current_y + direction[next_direction_index][1]

        # 탐색 가능하다면? - > 그 위치로 이동
        if 0<=next_x<=n-1 and 0<=next_y<=m-1 and maps[next_x][next_y] == 0:
            flag = True
            current_x, current_y = next_x, next_y
            current_direction_index = next_direction_index
            maps[next_x][next_y] = 2
            break

    if flag == True:
        current_x, current_y = next_x, next_y
        current_direction_index = # 변경

    # 탐색 가능한 곳이 없던 것이기에, 후진가능하면 후진
    temp_direction_index = (4 - (current_direction_index - 2)) % 4
    next_x = current_x + direction[temp_direction_index][0]
    next_y = current_y + direction[temp_direction_index][1]


    if 0<=next_x<=n-1 and 0<=next_y<=m-1 and maps[next_x][next_y] !=1: # 후진이 가능한 경우
        current_x, current_y = next_x, next_y
        # 방향은 바꾸지 않음
        continue

    # 벽인 경우 => stop
    return answer

-----5시 54분 피니쉬---

'''

# # <초기화>
# answer = 1
# # 1. 입출력
# maps => 초기화 / -> maps 0일때 빈칸, 탐색한 칸은 2(다만, 후진은 가능), 탐색 불가능은 (벽) -> 1
# # 2. 현재위치를 current_x, current_y에 저장
#
# # 3. current_direction_index 초기화
# directions = [(-1,0), (0,1),(1,0),(0,-1)] # 북, 동, 남, 서

# 초기화
n, m = map(int, input().split())
current_x, current_y, current_direction_index = map(int, input().split())

# maps 초기화
maps = []
for i in range(n):
    maps.append(list(map(int, input().split())))
maps[current_x][current_y] = 2
# directions 초기화
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북, 동, 남, 서

# while문으로 탐색시작
# print("청소가능")
# print(current_x, current_y)
answer=1
while True:

    # 탐색가능한 곳이 있다면 break해서 while문을 continue
    flag = False
    maps[current_x][current_y] = 2

    for i in range(1,5):
        next_direction_index = (4 + (current_direction_index - i)) % 4
        next_x = current_x + direction[next_direction_index][0]
        next_y = current_y + direction[next_direction_index][1]

        # 탐색 가능하다면? - > 그 위치로 이동
        if 0<=next_x<=n-1 and 0<=next_y<=m-1 and maps[next_x][next_y] == 0:
            answer+=1
            flag = True
            current_x, current_y = next_x, next_y
            # print("청소가능")
            # print(current_x, current_y)
            current_direction_index = next_direction_index
            maps[next_x][next_y] = 2
            # print(maps)
            break

    if flag:
        continue

    # 여기까지 왔다면? 청소 가능한 곳이 없던 것이기에, 후진가능하면 후진
    back_direction_index = (4 + (current_direction_index - 2)) % 4
    next_x = current_x + direction[back_direction_index][0]
    next_y = current_y + direction[back_direction_index][1]
    # 후진 가능한 경우인지 체크
    if 0 <= next_x <= n - 1 and 0 <= next_y <= m - 1 and maps[next_x][next_y] != 1:  # 후진이 가능한 경우
        current_x, current_y = next_x, next_y
        # 방향은 바꾸지 않음
        continue

    # 벽
    print(answer)
    break
