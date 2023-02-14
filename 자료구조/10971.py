'''
백트래킹을 통해서 마지막 level에 시작지점을 가지는지 체크하고 그럴때 costs 배열에 append
append한 것들중 최소비용을 출력한다.
'''
import sys
input = sys.stdin.readline

n = int(input())

visited = [False]*(n+1)#1~n까지를 체크하는데 사용
cost = []
for i in range(n):
    cost.append(list(map(int, input().split())))

n_list = [0]*20
level = 0

min = 9e10

def tsp(level, n, be, sum):
    global min
    
    if level == n:
        if(cost[be][n_list[0]]!=0) and min>sum + cost[be][n_list[0]]:
            min = sum + cost[be][n_list[0]]
            return
    else:
        for i in range(n):
            if visited[i]==False and cost[be][i]!=0:
                visited[i]=True
                tsp(level+1, n, i, sum + cost[be][i])
                visited[i]=False               

for i in range(n):
    n_list[level] = i
    visited[i] = True
    tsp(level+1, n, i, 0)
    visited[i]=False

print(min)