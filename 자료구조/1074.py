# # 37분 시작 -> 약 1시간동안 풀기(38분 끝)
# # idea) 2*2에서 가장 왼쪽 위의 숫자만 알면 모두 알 수 있게 됨.
# # 8은 8//2 = 4 -> 4//2 = 2 로 쪼개서 생각하고 (2,2)의 행렬로 분할되었다면 멈춤
# # 위의 과정에서 나눠진 나머지값만큼으로 (0,0)에서 step이 Z 모양의 단계대로 이동하면서 나머지값의 제곱배에 Z의 단계(1,2,3단계 존재)로 곱해지며 2차원 행렬을 채워나가기

# # 위의 아이디어를 22분 동안 생각..

# n,r,c = map(int, input().split())

# n = 2**n # n으로 3이 주어지면 8*8행렬임
# N = n
# steps = [(0,1),(+1, 0),(1,1)] #순서대로 오른쪽, 아래, 대각선
# # graph
# graph = [[0]*n for _ in range(n)]
# graph[0][0] = 0
# visited = [(0,0)]

# while(n>2):
#     temp_n = n//2 # 4
#     step_size = temp_n # 4칸씩 Z로 이동
#     step_plus = temp_n**2 # 4*4의 값만큼 커짐
#     n = n//2
#     #print(step_size, step_plus)
    
#     visited_temp = []
#     for i in visited:
#         count = 1
#         #print("visit",i)
#         for step in steps:
#             # i마다 step별로 이동
#             if (i[0]+step[0]*step_size) <= N-1 and (i[1]+step[1]*step_size)<N-1:
#                 graph[i[0]+step[0]*step_size][i[1]+step[1]*step_size] = graph[i[0]][i[1]] + step_plus * count
#                 #print("step",i[0]+step[0]*step_size,i[1]+step[1]*step_size,graph[i[0]][i[1]] + step_plus * count)
#                 visited_temp.append((i[0]+step[0]*step_size,i[1]+step[1]*step_size))
#                 count+=1
#     visited = visited + visited_temp
    
    
# for t in visited:
#     i,j = t[0], t[1]
#     count = 1
#     for step in steps:
#         graph[i + step[0]][j + step[1]] = graph[i][j] + count
#         count +=1
# # print(graph)
# print(graph[r][c])

N, r, c = map(int,input().split())

def Z(x, y, N):
    global res
    if x == r and y == c:
        print(res)
        exit(0)
    elif N == 1:
        res += 1
        return
    if not (x <= r < x + N) and not (y <= c < y + N):
        res += N ** 2
        return
    Z(x, y, N // 2)
    Z(x, y + N // 2, N // 2)
    Z(x + N // 2, y, N // 2)
    Z(x + N // 2, y + N // 2, N // 2)


global res
res = 0
Z(0, 0, 2 ** N)