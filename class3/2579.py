'''
https://www.acmicpc.net/problem/2579

9시 15분 시작

1계단 혹은 2계단 오르기 가능.
연속된 세게의 계단을 밟으면 안 됨.
마지막 도착 계단은 반드시 밟아야함

총 점의 최댓값. -> DP?

dp를 사용해서 각 계단마다 가질 수 있는 경우으이 수를 구하기
각각 당장의 최댓값을 구하기

--정리--
dp 비교조건에 제약조건을 걸어주면 쉬움.

비교대상 -> 현재칸 + 1칸전+3칸전 / 현재칸 + 2칸전 + 1칸전

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
cost[3] = max(n_list[3] + n_list[3-2], n_list[3-1]+n_list[3]) # 2칸 이전의 계단을 밟는 경우

for current in range(4,n+1):
    cost[current] = max(n_list[current] + n_list[current-1] + cost[current-3], n_list[current] + cost[current-2])

print(cost[n])