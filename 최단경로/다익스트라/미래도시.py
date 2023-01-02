# start node가 1일때와 k일때 두개를 하고 1-> k, k-> x의 각 경우의 최소 cost를 구해서 더하여 최소 시간을 계산하도록 함.
# start -> end : dijkstra

# 다익스트라도 가능하지만 플로이드워셜도 가능 -> 모든 정점에서의 다른 정점까지의 최솟값을 구하는 문제로도 풀 수 있음.

import heapq

INF = int(1e9)

n, m = map(int,input().split()) #전체 회사의 개수, 경로의 개수

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    # 양방향 그래프

x,k = map(int, input().split())

def dijkstra(start, end):
    costs = [INF]*(n+1)
    queue =[]
    heapq.heappush(queue, (0,start))

    while(queue):
        cost,current_node = heapq.heappop(queue)

        if cost > costs[current_node]:
            continue
        
        for next_node in graph[current_node]:
            if 1 + cost < costs[next_node]:
                # print("next node", next_node)
                costs[next_node] = 1 + cost
                heapq.heappush(queue, (costs[next_node], next_node))
    
    # print(costs)
    return costs[end]

if dijkstra(1,k)+dijkstra(k,x) >= INF:
    print("-1")
else:
    print(dijkstra(1,k)+dijkstra(k,x))


# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5
# answer : 3

# 4 2
# 1 3
# 2 4
# 3 4
# answer : -1