'''

dfs를 사용하여 start값과 연결된 친구를 발견할때 깊이를 저장하게 됨.

start를 모든 유저로 하여서 유저마다의 bfs 사용해 얻은 값을 비교하여 min값을 updqte를 진행. > min값이 담긴 배열에서 제일 Min값을 가진 사람을 count하도록하여 결과를 출력한다.
유저수가 최대 100까지 가능한데 사이 관계수가 100*100인 100000의 절반 5000까지 가능하니 인접행렬을 사용하도록 한다.


bfs -> popleft써야하는데 pop쓰고 계속 헤맴...주의!! popleft를 써야 가장 먼저 들어간 것이 우선으로 꺼내짐!!

'''

import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

relation = [[0]*(n+1) for _ in range(n+1)] # 0일때는 사용하지 않음

for i in range(m):
    a,b = map(int, input().split())
    relation[a][b] = 1 # 연결
    relation[b][a] =1

total_count = 0
def bfs(queue, visited):

    global total_count

    while(queue):
        node, count = queue.popleft()
        total_count += count
        for i in range(1,n+1):
            if relation[node][i]==1 and visited[i]==False:
                visited[i]=True
                # print("i count",i,count+1)
                queue.append((i,count+1))

result = int(1e10)
result_node = 1

for node in range(1,n+1):
    visited = [False]*(n+1)
    queue = deque([])
    queue.append((node,0))
    # print("stat node=====>", node)
    visited[node] = True
    total_count=0
    bfs(queue,visited)

    if total_count < result:
        result = total_count
        result_node = node

print(result_node)
