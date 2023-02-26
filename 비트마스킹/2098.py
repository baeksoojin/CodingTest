'''

외판원 순회

TSP이라는 문제로 computer science에서 가장 중요하게 취급되는 문제중 하나.

1~n까지의 번호가 매겨진 도시들이있고 도시들 사이의 길이 존재.(없을 수도 있음)
한 도시에서 출발해서 N개의 도시를 모두 거쳐 다시 원래의 도시로 돌아오는 순회 여행 경로를 계획하려고한다.
한번갔던 도시로는 다시 갈 수 없음.

가장 적은 비용을 들이는 외판원 순회 여행 경로를 구해야함

'''

n = int(input())
INF = int(1e9)

graph =[]
for i in range(n):
    graph.append(list(map(int, input().split())))

dp =[[None]*(1<<n) for _ in range(n)]

visited_all = (1<<n)-1
def dfs(x,visited):

    if visited==visited_all:#마지막 depth에서 체크
        if graph[x][0]!=0:
            return graph[x][0]
        else:
            return INF
    
    if dp[x][visited]!=None:#이미 최솟값이 존재하는 경우
        return dp[x][visited]

    temp =INF
    for i in range(1,n):

        if not graph[x][i]:
            continue
        if visited & (1<<i):
            continue

        temp = min(temp, dfs(i,visited | (1<<i))+graph[x][i])
    
    dp[x][visited] = temp

    return dp[x][visited]


print(dfs(0,1))


