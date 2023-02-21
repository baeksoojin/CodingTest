# 동전문제로 동전의 가치가 주어지면 해당 가치를 가진 동전을 조합해서
# 가치가 k가 되도록 만들 수 있는 경우의 수 

'''
1,2,5가 주어지면

만들고 싶은 수가 k라면,
k에서 1이 부족한 경우 -> k가 크거나 같을 클경우, k-1의 가치를 만드는 경우를 더해줌
k에서 2가 부족한 경우 -> k가 2보다 크거나 같을 경우, k-2의 가치를 만드는 경우를 더해줌
k에서 5이 부족한 경우 -> k가 3보다 크거나 같을 경우, k-5의 가치를 더해줌.


=> 만들고 싶은 수를 입력받은 동전의 가치가 되는 모든 경우를 다 고려해줌

'''
import sys
input = sys.stdin.readline

n,k = map(int, input().split())

dp = [0]*(10001)
dp[0]=1 # 입력받은 coin값이 나올 경우를 체크하기 위해서 

coins = []

for i in range(n):
    coins.append(int(input()))

for coin in coins:
    for i in range(1, k+1):
        if i-coin >=0:
            dp[i]+=dp[i-coin]

print(dp[:k+1])
print(dp[k])


