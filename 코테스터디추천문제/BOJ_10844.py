'''
쉬운 계단수 

길이 n인 계단수를 만들 수 있는 총 개수를 구하는 문제


'''

n = int(input())
mod = 1000000000

dp = [[0]*(10) for _ in range(101)]

for i in range(1,10):
    dp[1][i] = 1

for i in range(2,n+1):
    for j in range(0,10):
        if j==0:
            dp[i][j] = (dp[i-1][j+1])%mod
        elif j==9:
            dp[i][j]= (dp[i-1][j-1])%mod
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1])%mod
sum=0
print(dp[n])
for i in range(10):
    sum =( sum+dp[n][i])%mod
print(sum)






