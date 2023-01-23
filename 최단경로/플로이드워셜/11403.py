'''
모든 정점에 대해서 인접행렬이 주어질때 경로가 이어져있는지 모든 정점마다 확인해야해서 플로이드 워셜을 사용
'''

import sys
input = sys.stdin.readline

n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split()))) # 방향 그래프

# 플로이드워셜
for k in range(n):
    for i in range(n):
        #각 지점마다 체크
        for j in range(n):
            if graph[i][j] ==1 or (graph[i][k] == 1 and graph[k][j] == 1):
                graph[i][j]=1
    
for i in range(n):
    for j in range(n):
        print(graph[i][j], end=" ")
    print()
