import sys

input = sys.stdin.readline

# 시작하는 날짜 이전에 끝낼 수 있는 작업과 끝나는 날짜에서 얻을 수 있는 값을 더했을 때, 기존의 dp value(금액)보다 크다면 update

n = int(input())

dp = [0]*(n+1) # 0일부터 편의상 넣어줌
max_p = -1
for i in range(1,n+1):
    t,p = map(int, input().split())
    # 시작하는 날짜 이전에 끝낼 수 있는 작업의 최댓값
    max_p = max(max_p, dp[i-1])
    finish_date = i+t-1
    if finish_date <= n:
        dp[finish_date] = max(max_p + p, dp[finish_date])
print(max(dp))




