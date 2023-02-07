'''
10시 1분 시작 -> 10시 33분: cost[3]을 계산하는 과정에서 2칸 전의 계단과 3번째 계단을 선택해도 되는데 그 경우를 생각하지 않았음.
마지막 도착 계단은 반드시 밟아야하기에 마지막을 기준으로 2칸 이전이 직전인 경우와 1칸 이전이 직전인 경우를 나눠서 계산을 해준다.
다만 중요한 것은 연속된 세개의 계단을 모두 밟으면 안 되니까 1칸 이전인 경우, 그 직전의 계단이 아닌 -2칸을 밟아야한다.
1. [마지막 -2칸]까지의 점수 + 마지막칸의 점수
2. [마지막 -1칸]의 점수 + [마지막 -3칸]까지의 점수 + 마지막 칸의 점수
'''

import sys
input = sys.stdin.readline

n = int(input())

cost = [0]*301
n_list = [0]*301

for i in range(n):
    n_list[i+1] = int(input())

cost[0] = 0
cost[1] = n_list[1] #1층
cost[2] = n_list[1]+n_list[2] #1층과 2층을 모두 밟아야 최댓값임
cost[3] = max(n_list[3] + n_list[3-2], n_list[3-1]+n_list[3]) # 1,3칸을 밟거나 2,3칸을 밟는 경우중 큰 값을 선택한다.

for current in range(4,n+1):
    cost[current] = max(n_list[current] + n_list[current-1] + cost[current-3], n_list[current] + cost[current-2])

print(cost[n])

