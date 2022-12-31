#heapq를 사용한 다익스트라 적용

import sys
import heapq
input =  sys.stdin.readline

INF = int(1e9) # 최대값 = 가는 경우 없음
n = int(input()) #노드
m = int(input()) #간선

costs = [INF]*(n+1) # 최소 cost를 저장할 result 배열
graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b,cost = map(int, input().split())
    graph[a].append((b,cost)) 

start, end = map(int,input().split())
queue =[]
costs[start] = 0
heapq.heappush(queue, (0,start))

while(queue):
    cost, node = heapq.heappop(queue)

    if costs[node] < cost:
        continue
    
    for g in graph[node]:
        temp_cost = g[1] + cost # start부터 현재노드까지의 거리와 현재노드부터 g[1]노드로 가는 거리의 합
        if temp_cost < costs[g[0]]: # 현재노드를 거치지 않고 그냥 가는 경우와 지금까지 구했던 최소 거리가 저장된 값과 비교
            costs[g[0]] = temp_cost
            heapq.heappush(queue, (temp_cost, g[0]))

print(costs[end])


    

