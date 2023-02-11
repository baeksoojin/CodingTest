'''
(i>1)
i번째에서는 i-1을 고려해서 가능한 경우를 구해야하는데 이전에 나온 색이 되면 안 되니까 2가지 경우가 존재한다.<br>
이전 경우를 넘기고 그것을 제외한 경우 발생가능한 최솟값을 사용

처음에는 빨파초중에서 가장 저렴한 것을 선택해야함
-> testcase 5에러 에러
'''

# import sys
# input = sys.stdin.readline

# n = int(input())

# costs = []
# for i in range(n):
#     costs.append(list(map(int, input().split())))

# cost=[0]*(1000)
# before = 0
# cost[0] = min(costs[0][0], costs[0][1],costs[0][2])

# sum_list = []
# for start in range(3):
#     cost[0] = costs[0][start]
#     before = start

#     for i in range(1,n):

#         temp_list = []
#         for j in range(3):
#             if before != j:
#                 temp_list.append((costs[i][j], j))
#         cost[i], before = min(temp_list, key=lambda x: x[0])
#     print(cost[:n])
#     print(sum(cost))
#     sum_list.append(sum(cost))

# print(min(sum_list))

'''

dp문제로, 
위의 코드는 고려하지 않은 경우들이 많음
현재 위치가 3가지 경우가 되고 이전 경우 중에서 min을 선택해야지 모든 경우를 다 고려할 수 있음.
타일문제처럼 지금을 기준으로 하고 이전값들중에서 Min을 찾아내는 방법으로 다시 작성

'''


import sys
input = sys.stdin.readline

n = int(input())
rgb = []
for _ in range(n):
    rgb.append(list(map(int, input().split())))

for i in range(1,n):
    rgb[i][0] = min(rgb[i-1][1], rgb[i-1][2]) + rgb[i][0] #빨
    rgb[i][1] = min(rgb[i-1][0], rgb[i-1][2]) + rgb[i][1] #초
    rgb[i][2] = min(rgb[i-1][1], rgb[i-1][0]) + rgb[i][2] #파

print(min(rgb[n-1])) #가장 마지막이 빨초파가 되는 경우중 min을 선택




            




    

