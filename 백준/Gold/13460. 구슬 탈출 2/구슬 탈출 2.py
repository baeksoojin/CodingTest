'''
구슬탈출2
4월 7일 3시 30분 시작

3시 50분까지 문제 이해. -> 구슬을 구멍에 탈출시켜야하는데 판을 상하좌우 기울여서 가능. 파란색이 빠지면 안 됨. (동시에 빠져도 안됨)
빈캄 -> '.'
이동 불가 -> "#"
구멍 위치 -> '0'
빨간 구슬 위치 -> 'R'
파란 구슬 의치 -> 'B'

3시 42분 문제 이해 완료.
----
4시 10까지 알고리즘 생각.

backtracking을 사용하는 것으로 판단 . 인자에 board를 넘겨주기!, depth(count)랑!

4시 2분에 생각이 끝났으니..구현 하기 전에 디테일 잡기! -> 최소 4시 10분에 시작

4시 22분에 알고리즘 작성 도식화 끝. 이제 시작
5시 30분 시간초과

11시 이전 풀이체크
11시 20분 끝.

느낀점 ) 배열을 queue에 저장했던 방법은 빨 파 구슬이 1개 이상일수도 있다고 생각해서 였는데,,,,,^^ 문제조건을 잘 읽자,..!
'''
# import copy
#
# # 초기화
#
# n, m = map(int, input().split())
#
# depth = 0
# board = [list(input()) for _ in range(n)]
# # print(board)
#
# direction = [(-1, 0), (1, 0), (0, -1), (0 ,1)] # 상하좌우
#
# from collections import deque
#
# # queue
# def bfs(board, depth):
#     queue = deque([])
#     queue.append(board)
#     cnt_queue = deque()
#     cnt_queue.append(depth)
#     while queue:
#
#         current_depth = cnt_queue.popleft()
#         current_board = queue.popleft()
#         # print(depth,board)
#
#         if current_depth > 10:
#             return -1
#
#         for dir in direction:
#             diff_x = dir[0]
#             diff_y = dir[1]
#             # print("dir -> ", diff_x, diff_y)
#
#             change_board = copy.deepcopy(current_board)
#
#             # dir 방향으로 기울였을 때, next_depth로 갈 수 있는지체크. -> 파란구슬이 빠지지 않을 때
#             next_depth = False
#             out_R = False # 빠져나갈 수 있는지 체크
#             out_B = False # 빠져나갈 수 있는지 체크
#
#             for i in range(n):
#                 for j in range(m):
#                     other_count = 0 # 움직이는 중에, 다른 구슬이 있다면 최종 위치에서 그만큼 빼줘야함.
#                     if current_board[i][j] == 'R' or current_board[i][j] =='B':
#                         # print("befoe ->>", current_board)
#                         current_i = i
#                         current_j = j
#
#                         while current_board[current_i+diff_x][current_j+diff_y] != "#":
#
#                             current_i += diff_x
#                             current_j += diff_y
#
#                             # 움직이는 중에, 다른 구슬이 있다면 최종 위치에서 그만큼 빼줘야함.
#                             if current_board[current_i][current_j] == 'R' or current_board[current_i][current_j] == 'B':
#                                 other_count +=1
#
#                             # 구멍에 들어간다.
#                             if current_board[current_i][current_j] == 'O':
#                                 if current_board[i][j] == "R": # 이동중, 빨간구슬이 빠지는 경우
#                                     # print("red")
#                                     out_R = True
#                                 if current_board[i][j] == "B":
#                                     # print("blue")
#                                     out_B = True
#
#                         # print(current_i + (-1)*(diff_x)*other_count)
#                         # print(current_j + (-1)*(diff_y)*other_count)
#                         if not((current_i + (-1)*(diff_x)*other_count)==i and (current_j + (-1)*(diff_y)*other_count)==j):
#                             next_depth = True
#                             change_board[i][j] = '.'
#                             # board를 변경 -> 변경되는 과정에서 파란 구슬이 빠졌거나 빨간구슬만 빠진 경우에 대해서는 밑에서 체크
#                             change_board[current_i + (-1)*(diff_x)*other_count][current_j + (-1)*(diff_y)*other_count] = current_board[i][j]
#                             # print("after->",change_board)
#
#                     if out_B == True:
#                         break
#
#                 if out_B == True:
#                     break
#
#             if out_B == True:
#                 continue # 해당 방향으로는 백트래킹 불가능.
#             if out_R == True:
#                 # print("answer")
#                 return current_depth+1
#             else: # 이동중에 구멍에 B랑 R가 모두 빠지지 않은 경우.
#                 if next_depth:
#                     # print("next 이동 ---->>",current_depth+1,"--- ", change_board)
#                     cnt_queue.append(current_depth+1)
#                     queue.append(change_board)
#
#
#     return -1
#
# print(bfs(board, 0))
#

'''
visited처리-> 시간초과방지
'''

from collections import deque

n, m = map(int, input().split())

b_queue = deque([])
r_queue = deque([])

visited = [[[[False] * (m) for _ in range(n)] for _ in range(m)] for _ in range(n)]

# 상,하,좌,우
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

first = [0] * 4
board = []

for i in range(n):
    board.append(input().strip())

for i in range(n):
    for j in range(m):
        if board[i][j] == "R":
            first[0], first[1] = i, j
            r_queue.append((i, j, 1))
        if board[i][j] == "B":
            first[2], first[3] = i, j
            b_queue.append((i, j, 1))

visited[first[0]][first[1]][first[2]][first[3]] = True


def moving(x, y, move):
    cnt = 0
    is_out = False

    while board[x + move[0]][y + move[1]] != "#":

        cnt += 1
        x += move[0]
        y += move[1]
        if board[x][y] == "O":
            is_out = True

    return (x, y, cnt, is_out)


def bfs():
    result = -1

    while (r_queue):

        rx, ry, rcnt = r_queue.popleft()
        bx, by, bcnt = b_queue.popleft()

        if rcnt > 10:  # 10번 체크를 했는데 구멍이 없었을 때라면 -1을 리턴
            return result
        else:

            for m in move:
                # 빨간 구슬이 다음으로 갈 수 있는 위치를 계산
                next_rx, next_ry, rstep, is_rout = moving(rx, ry, m)
                # 파란 구슬이 다음으로 갈 수 있는 위치를 계산
                next_bx, next_by, bstep, is_bout = moving(bx, by, m)

                # 빨간색 구슬과 파란색 구슬이 같은 위치에 존재할때
                # 많이 움직인 것을 뒤로 빼줌
                if next_rx == next_bx and next_ry == next_by:
                    if rstep > bstep:  # 빨간색을 옮겨줘야하는 경우
                        next_rx -= m[0]
                        next_ry -= m[1]

                    else:  # 파란색 구슬을 옮겨주는 경우
                        next_bx -= m[0]
                        next_by -= m[1]

                # 파란색 공이 이동중에 빠지는 경우
                if is_bout:
                    continue

                if is_rout:
                    return rcnt

                if visited[next_rx][next_ry][next_bx][next_by] != True:
                    visited[next_rx][next_ry][next_bx][next_by] = True
                    r_queue.append((next_rx, next_ry, rcnt + 1))
                    b_queue.append((next_bx, next_by, bcnt + 1))

    return result


result = bfs()
print(result)