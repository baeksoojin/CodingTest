#heapq를 사용해서 가장 작은 거리를 가진 노드를 찾는 과정을 없앰 -> 시간복잡도 감소

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m =map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for i in range(m):
    a,b,cost = int(input().split())
    graph[a].append((b,cost))

def dijkstra(start):

    q =[] # (cost, node) 정보를 담을 list

    heapq.heappush(q, (0,start)) 
    distance[start] = 0

    while q:
        
        dist, now = heapq.heappop(q)
        
        # 이미 처리된 노드라면 무시한다
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]]= cost
                heapq.heappush(q,(cost,i[0]))#다음으로 갈 수 있는 경우를 heap에 넣어줌
            
dijkstra(start)

for i in range(1,n+1):
    if distance[i]==INF:
        print("INFINITY")
    else:
        print(distance[i])

