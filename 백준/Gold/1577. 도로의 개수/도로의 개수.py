n,m = map(int, input().split())

construct_num = int(input())

con_list = [[[] for _ in range(m+1)] for _ in range(n+1)]
for _ in range(construct_num) :
    a, b, c, d = map(int, input().split())
    con_list[a][b].append((c, d))
    con_list[c][d].append((a, b))

# 0,0 부터 m,n까지 존재해야함
dp = [ [0] * (m+1) for _ in range(n+1)]

dp[0][0] = 1

for i in range(n+1):
    for j in range(m+1):

        # 위에서 올 수 있다면? 위에서 오는 경우의 수를 더한다.
        if i-1>=0 and (i-1,j) not in con_list[i][j]:
            dp[i][j] += dp[i-1][j]
        
        # 아래
        if j-1>=0 and (i, j-1) not in con_list[i][j] :
            dp[i][j] += dp[i][j-1]

print(dp[-1][-1])