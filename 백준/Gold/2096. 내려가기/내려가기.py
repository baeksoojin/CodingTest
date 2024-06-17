n = int(input())
n_list = list(map(int, input().split()))
max_dp = n_list[:]
min_dp = n_list[:]

for i in range(1,n):
    n_list = list(map(int, input().split()))
    max_dp[0],max_dp[1],max_dp[2]= max(max_dp[0], max_dp[1]) + n_list[0], max(max_dp) + n_list[1], max(max_dp[2], max_dp[1]) + n_list[2]
    min_dp[0],min_dp[1],min_dp[2] = min(min_dp[0], min_dp[1]) + n_list[0], min(min_dp) + n_list[1], min(min_dp[2], min_dp[1]) + n_list[2]

print(max(max_dp), min(min_dp))
