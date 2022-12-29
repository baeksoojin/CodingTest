# 두개의 변수가 주어지고 그 변수로 만들 수 있는 경우의 수를 구하는 문제로 다이나믹 프로그래밍문제

result = [[1] * 31 for _ in range(31)]

for i in range(31):
    result[1][i] = i

for i in range(2, 31):
    for j in range(i + 1, 31):
        result[i][j] = result[i][j - 1] + result[i - 1][j - 1]

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(result[n][m])