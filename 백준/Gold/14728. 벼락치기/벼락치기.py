
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

result = [[0]*(m+1) for _ in range(n+1)] # 2차원 행렬로 변경
bags = [(0,0)] # for문을 돌릴 때 1부터 Index를 사용

for i in range(n):
    a,b = map(int,input().split())
    bags.append((a,b))

for i in range(1,n+1):
    for j in range(1,m+1):
        if bags[i][0]>j:
            result[i][j] = result[i-1][j]
        else:
            result[i][j] = max(result[i-1][j], bags[i][1]+ result[i-1][j-bags[i][0]])
        

print(result[n][m])
