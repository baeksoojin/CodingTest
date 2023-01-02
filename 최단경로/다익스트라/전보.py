# 단방향 그래프 문제. 특정노드에서 전보 전달이 가능한 노드의 개수와 각 도시들이 메시지를 받는데 걸리는 시간 구하기 -> inf가 아닌 노드의 개수 구하기, 그러한 노드들의 cost를 모두 더해서 출력하기
# 특정 지점 c에서 각 도시로 가는 경우로 다익스트라를 사용

import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

n,m,start = map(int, input().split())
times = [INF] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,time = map(int, input().split())
    graph[a].append((b,time)) # 단방향 그래프

queue = []
heapq.heappush(queue,(0, start))
time[start] = 0


while(queue):

    time,current_node = heapq.heappop(queue)
    
    if time > times[current_node]:
        continue

    for i in graph[current_node]:
        temp_time = i[1] + time
        if  temp_time < times[i[0]]:
            times[i[0]] = temp_time
            heapq.heappush(queue,(temp_time,i[0]))

    # print(times)

count = 0
result_time = 0
for time in times:
    if time!=INF:
        count += 1
        result_time = max(time, result_time)

print(count-1 , result_time)
