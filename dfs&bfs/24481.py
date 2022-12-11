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
    graph[i].sort(reverse = False)
    for j in graph[i]:
        if visited[j]==-1:
            dfs(j,cnt+1)

dfs(r,0)

for i in visited[1:]:
    print(i)

# 깊이 우선 탐색으로 모든 노드의 깊이를 출력.
# 오름차순으로 탐색 -> reverse = False
#재귀 런타임에러 방지 : set recursion limit!!
# 시간단축 -> 배열 초기화 for문을 다 돌리지 말고 [-1 for i _ in range(배열 사이즈)]를 통해서 -1로 1차원 배열 초기화. -> 100ms 이상 차이남