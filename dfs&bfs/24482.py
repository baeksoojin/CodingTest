import sys

sys.setrecursionlimit(10 ** 8)

#초기화
n, m, r = map(int, sys.stdin.readline().split())
visited = [-1 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

#인접리스트 생성
for i in range(0,m):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
    
#재귀
def dfs(i,cnt):
    visited[i] = cnt
    graph[i].sort(reverse = True)
    for j in graph[i]:
        if visited[j]==-1:
            dfs(j,cnt+1)

dfs(r,0)

for i in visited[1:]:
    print(i)

