import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 1. 3차원 dp 생성
dp = [ [ [0, 0, 0] for _ in range(n)] for _ in range(n)]
# 2. 초기값 설정
dp[0][1][0] = 1
# 3. dp
for i in range(n) :
    for j in range(n) :
        if not graph[i][j] :
            if j - 1 >= 0 : 
                dp[i][j][0] += dp[i][j-1][0]
                if i - 1 >= 0 : dp[i][j][0] += dp[i][j-1][2]

            if i - 1 >= 0 : 
                dp[i][j][1] += dp[i-1][j][1]
                if j - 1 >= 0 : dp[i][j][1] += dp[i-1][j][2]
    
            if i - 1 >= 0 and j - 1 >= 0  and not graph[i][j-1] and not graph[i-1][j] :
                dp[i][j][2] += sum(dp[i-1][j-1])
# 4. 결과 출력
print(sum(dp[-1][-1]))