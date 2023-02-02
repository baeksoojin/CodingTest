'''
nqueen문제

크기가 n*n인 체스판이 있을 때 퀸 n개를 서로 공격할 수 없게 만드는 문제이다.

현재시간 : 9시 분28 -> 30분 안으로 풀어야함.

<문제를 이해못해서 해설을 봄!!>
퀸을 기준으로 일직선상과 대각선에는 아무것도 놓여있으면 안 된다.

1. 일직선상을 고려 : 하나의 퀸이 놓여졌다면 다음퀸은 일직선상에 놓이지 못하기에 무조건 열이 달라야한다.
2. 대각선을 고려 : 행번호차이와 열 번호 차이에 있다면 같은 대각선상에 있다는 것을 의미한다.

'''


n  = int(input())

queen = [-1]*n
count=0

def N_queen(level):

    global count

    if level==n:
        count +=1
        return

    for i in range(n):
        queen[level] = i
        flag = True
        for j in range(level):
            if queen[level] == queen[j] or abs(level-j) == abs(queen[level] - queen[j]):
                flag = False
                break

        if flag ==True:
            N_queen(level+1)
        
N_queen(0)
print(count)