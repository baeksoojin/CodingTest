'''
제일 큰 값을 찾고 before에 행의 index를 저장
다음에서 제일 큰 값을 찾고 제일 큰 값을 찾음(1번 탐색하기 위해서 before행을 제외)

2차원 dp를 사용해야한다.
왜냐하면? 같은 행에서 가장 큰 수라고 해도 결국 최종으로 누적값이 제일 커야하는데 같은 행에서 최댓값이 그것을 보장하지는 않기 때문.
-> 왜? 바로 다음에는 같은 열을 선택할 수 없다는 제약사항이 존재하기때문이다.

따라서, 4가지 경우를 모두 따져줘야하기에, 2차원 dp를 사용해야한다.

두번째 행의 첫번째 -> 이전 행에서 자기자신을 제외한 나머지 열 중에서 가장 큰 값을 선택

https://school.programmers.co.kr/learn/courses/30/lessons/12913

'''


def solution():

    land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
    
    n = len(land)
    m = 4

    dp = [[0]*4 for _ in range(n)]

    for i in range(n):
        if i==0: # 첫행은 누적값이 모든 열에서 자기자신이 가장 크다. (이전 값이 없으니,,)
            for j in range(m):
                dp[i][j] = land[i][j]
        for j in range(m):

            # 이전 행에서 자기자신을 제외한 나머지 열 중에서 가장 큰 값을 선택

            for k in range(m):
                if j==k:
                    continue
                
                dp[i][j] = max(dp[i][j], land[i][j] + dp[i-1][k])# 나머지 열 중에서 큰 값을 dp[i][j]로 계속 업데이트시키며 결국 해당 행까지의 해당 열의 가장 큰 값을 저장

    print(max(dp[n-1]))

solution()