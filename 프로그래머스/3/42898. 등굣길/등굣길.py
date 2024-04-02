'''
bfs? -> 최단거리 1개를 위한 경로 /(1칸에 1번의 경로만 가능)
dp를 사용해야함.
특정 위치를 기준으로 위,왼쪽을 체크하면 됨
'''

from collections import deque

def solution(m, n, puddles):

    
    puddles = [[q,p] for [p,q] in puddles] 
    dp = [[0]*(m+1) for _ in range(n+1)]
    dp[1][1] = 1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if [i,j] in puddles:
                dp[i][j]=0
                continue
            if i==1 and j==1:
                continue
            else:
                dp[i][j] =  (dp[i][j-1] + dp[i-1][j]) % 1000000007
           
    print(dp)
    return dp[n][m]
