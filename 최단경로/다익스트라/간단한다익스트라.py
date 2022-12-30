from dis import dis
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
start  = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def get_smallest_node(): # 방문하지 않은 노드중에서 가장 작은 값을 가지는 것을 선택
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):

    # 시작노드관련 초기화 및 최단거리 세팅
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1] #시작노드로부터 연결된 노드들에 대해서 입력받은 가중치를 저장

    #나머지에 노드(시작노드 제외)들에 대해서 최단거리 세팅
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("INFIINTY")
    else:
        print(dis[i])
