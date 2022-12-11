# 깊이우선 탐색에서 탐색하는 정점 노드를 순서대로 출력
import sys

sys.setrecursionlimit(10 ** 8)

def dfs(start):
    global cnt
    visited[start] = cnt 
    graph[start].sort(reverse = True)
    for i in graph[start]:
        if visited[i]==0:
            cnt += 1
            dfs(i)

n, m, r = map(int, sys.stdin.readline().split())

visited = [0]*(n+1)
graph = [[] for _ in range(n+1)]
cnt=1

#인접 리스트 만들기
for i in range(0,m):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
dfs(r)

for i in visited[1:]:
    print(i)

# 주의 할 점
# python 재귀 깊이는 1000으로 최대치가 잡혀있음
# 늘리기 위해서는? sys를 사용 -> sys.setrecursionlimit(10**8)
# 시간을 줄이기 위해서  -> sys.stdin.readline().split()으로 사용
