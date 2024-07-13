'''
최소 동전을 사용해서 k원을 만드는 방법
'''

# 입력 받기
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# 초기화
INF = 10001
dp = [INF] * (k + 1)
dp[0] = 0  # 0원을 만들기 위한 동전 개수는 0개

# 동적 계획법으로 dp 테이블 채우기
for coin in coins:
    for j in range(coin, k + 1):
        if dp[j - coin] + 1 < dp[j]:
            dp[j] = dp[j - coin] + 1

# 결과 반환
answer = dp[k] if dp[k] != INF else -1
print(answer)
