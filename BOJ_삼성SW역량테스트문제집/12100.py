'''
최대 5번의 경우를 체크하면 됨.

level이 5로 정해져있음

# move함수
1. 각 방향에 맞게 이동시켜야함
2. 각 방향에 맞게 하나씩 비교했을 때 값이 일치한다면 합쳐주고 -> 방향에 맞게 다시 밀어줘야함

'''
import copy
n = int(input())

board = []

for i in range(n):
    board.append(list(map(int, input().split())))

limit = 5
answer = -1

def turn_90(dir, board):

    # (board)print

    new_board = [[0]*n for _ in range(n)]

    if dir=="right":#오른쪽으로 90도 회전
        # next 행 -> 이전의 열과 같음
        # next 열 -> (n-1)- (이전의 행) 의 연산결과와 같음
        for i in range(n):
            for j in range(n):
                new_board[j][n-1-i] = board[i][j]
        # print("new_board/right",new_board)
        return new_board
    
    if dir=="left":
        # next 행 -> (n-1)-(이전의 열)
        # next 열 -> 이전의 행과 같음
        for i in range(n):
            for j in range(n):
                new_board[n-1-j][i] = board[i][j]
        # print("new_board/left",new_board)
        return new_board


def move(next,board):

    # print("next, board", next, board)

    # 위,아래,오른쪽,왼쪽으로 이동한 결과를 next_board에 담아서 넘기기

    # 왼쪽으로 옮기는 경우 -> 1. 다 왼쪽으로 몰기(0을제거) -> 2. 왼쪽수와 오른쪽수를 비교해서 값이 같은지 체크하고 같다면 왼쪽수를 *2 오른쪽은 더 오른쪽에 있던 값들로 채워주기 -> 2. 0인 것을 제거하고 다 왼쪽으로 몰아버림

    if next==0 or next==1:#왼쪽 # 위쪽

        if next==1: # 위쪽으로 이동시키는 경우는 왼쪽으로 90도 회전한 보드를 가지고 왼쪽으로 이동시키는 로직을 적용
            board = turn_90("left",board)

        # 0. 다 왼쪽으로 밀기
        for i in range(n):
            # for j in range(n):
            #     if board[i][j]==0:#0을 없애고 오른쪽에 넣기
            #         board[i].pop(j)
            #         cnt+=1
                    # print("pop board",board[i])
                    # board[i].append(0)
                    # print("board append",board) 
            # 11% 에러 -> 00같은 경우를제대로 판단 못함
            temp=[]
            for j in range(n):
               if board[i][j] != 0:
                   temp.append(board[i][j])
            for _ in range(n-len(temp)):
                temp.append(0)
            board[i] = temp

        # 1. 왼쪽수와 오른쪽수를 비교해서 같다면 합치기
        for i in range(n):
            for j in range(n-1):
                if board[i][j] == board[i][j+1]:
                    board[i][j] = board[i][j]*2
                    # 2. 더 오른쪽에 있던 값을 한칸씩 옮기기
                    temp1 = board[i][:j+1]
                    temp2 = board[i][j+2:]+[0]
                    board[i] = temp1+ temp2

        if next==0:
            # print("moved/ direction : left",board)
            pass
        else:
            # 다시 오른쪽으로 회전
            board = turn_90("right",board)
            # print("moved/ direction : up",board)

    if next==2 or next==3: # 오른쪽으로 옮기는 경우(그리고 아래로 옮기는 경우)  -> 1. 다 오른쪽으로 붙이기 -> 2. 같은 숫자가 있다면 오른쪽숫자를 *2를 해주고 왼쪽 숫자를 없앤다음 1칸씩 오른쪽으로 밀고 마지막에 0을 추가

        if next==3:
            board = turn_90("left",board)

        #1. 오른쪽으로 붙이기 -> 0을 제거
        for i in range(n):
            # for j in range(n):
            #     if board[i][j]==0:# 0을 가지는 index로 pop을 하고 앞에 0을 추가
            #         board[i].pop(j)
            #         board[i] = [0] + board[i]
            temp = []
            for j in range(n):
                if board[i][j] !=0:
                    temp.append(board[i][j])
            for _ in range(n-len(temp)):
                temp = [0] + temp
            board[i] = temp
            # print(board[i])
        
        #2. 값이 같다면 합치고 위치를 오른쪽으로 이동
        for i in range(n):
            for j in range(n-1,0,-1):# 규칙상 오른쪽부터 비교를 해야함.
                if board[i][j] == board[i][j-1]:
                    # 오른쪽수를 *2
                    board[i][j] = board[i][j]*2
                    # 오른쪽으로 옮기기
                    temp1 = [0]+ board[i][:j-1] 
                    temp2 = board[i][j:]
                    board[i] = temp1 + temp2

        if next==2:
            # print("moved/ direction : right",board)
            pass
        else:
            # 다시 왼쪽으로 회전
            # print("down check ", board)
            board = turn_90("right",board)
            # print("moved/ direction : down",board)

    
    return board
    # 이동한 그래프를 결과로 return


def recursive(level, board):

    global answer

    # if level==1:
    #     return # test용 코드

    if limit == level:
        
        for b in board:
            # print("max(b)",max(b))
            answer = max(answer,max(b))
    if limit < level:
        return
    
    # 4가지 방향으로 재귀호출을 하면서 dfs를 실행
    # print("another")
    for i in range(4):
        # 해당하는 방향으로 움직였을 때 나올 수 있는 배열을 구하기
        board_temp = copy.deepcopy(board) 
        board_temp = move(i, board_temp) 
        # board를 넘겨버리면 그 값자체가 변경되어 반환됨 -> recursive이후 다시 원래의 board로 변경하던가 아님 값 자체를 변경하지 못하게 deepcopy를 사요해야함
        # 재귀호출을 진행
        recursive(level+1, board_temp)

recursive(0,board)
print(answer)