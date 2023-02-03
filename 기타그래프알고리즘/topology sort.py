from collections import deque

v,e = map(int, input().split())
indegree = [0] *(v+1) #진입차수
graph = [[] for i in range(v+1)]#연결리스트 초기화 : 간선 정보 담기

for _ in range(e):
    a,b = map(int, input().split())
    graph[a].append(b) # a->b : b로 진입
    indegree[b] +=1 #진입차수 1증가

def topology_sort():
    result =[]
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -=1 # 연결된 노드를 없애는 과정(연결된 노드의 진입차수 줄이기)
            if indegree[i] == 0:
                q.append(i)

    for i in result[:-1]:
        print(i, end="->")
    print(result[-1])

topology_sort()


'''

7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4

'''