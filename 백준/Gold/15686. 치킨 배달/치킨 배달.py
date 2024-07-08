import sys
import itertools
from  collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())

ori_graph = []
for _ in range(n):
    ori_graph.append(list(map(int, input().split())))

# 치킨집 리스트
chiken = []
home = []
for i in range(n):
    for j in range(n):
        if ori_graph[i][j] == 2:
            chiken.append([i,j])

        if ori_graph[i][j] == 1:
            home.append([i,j])


# # m개를 뽑음
chiken_index = [i for i in range(len(chiken))]

chiken_m_list = list(map(list,itertools.combinations(chiken_index, m)))

min_city_dis = 10e9

for chikens in chiken_m_list:

    chiken_xy = []
    for c in chikens:
        chiken_xy.append([chiken[c][0], chiken[c][1]])

    # 집에서 선택한 곳의 거리를 구하기
    city_dis = 0
    for h in home:
        min_dis = 10e9
        for c in range(len(chiken_xy)):
            min_dis = min(min_dis,abs(h[0]-chiken_xy[c][0]) + abs(h[1] - chiken_xy[c][1])) # 갈 수 있는 곳중에 가장 짧은 곳을 가야함 -> 최단거리
        city_dis+= min_dis
    min_city_dis = min(city_dis, min_city_dis)


print(min_city_dis)



# directions = [(-1,0), (1,0), (0,-1), (0,1)]

# def bfs(queue, visited, chiken_xy):
#     while queue:
#         current = queue.popleft()
#         current_x, current_y, current_dis =  current[0], current[1], current[2]

#         if ori_graph[current_x][current_y] == 2 and (current_x, current_y) in chiken_xy: # 철거되지 않은 치킨집
#             return current_dis


#         for d in directions:
#             next_x = current_x + d[0]
#             next_y = current_y + d[1]

#             if 0<=next_x<=n-1 and 0<=next_y<=n-1 and visited[next_x][next_y] !=1:
#                 queue.append([next_x, next_y, current_dis+1])
#                 visited[next_x][next_y]=1


# if len(chiken) == m:
#     print(0)
# else:

#     # chiken_m_list만 2로 남기고 나머지를 0으로 변경
#     answer = 10e9
#     for chikens in chiken_m_list:

#         chiken_xy = []
#         for c in chikens:
#             chiken_xy.append((chiken[c][0], chiken[c][1]))
        
#         city_dis = 0
#         for i in range(n):
#             for j in range(n):
#                 if ori_graph[i][j] == 1: # 집
#                     visited = [[0] * n for _ in range(n)]
#                     queue = deque([])
#                     visited[i][j] = 1
#                     queue.append([i,j,0])
#                     city_dis+=bfs(queue, visited, chiken_xy)
        
#         answer = min(city_dis,answer)

#     print(answer)


