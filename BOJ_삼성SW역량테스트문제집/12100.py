'''
최대 5번의 경우를 체크하면 됨.

level이 5로 정해져있음

'''

import pandas as pd
n = int(input())

board = []

for i in range(n):
    board.append(list(map(int, input().split())))

limit = 5
answer_temp = 0

def move(next,before_board):

    # 위,아래,오른쪽,왼쪽으로 이동한 결과를 next_board에 담아서 넘기기
    # 이동한 그래프를 결과로 return
    

def recursive(level, before_board):
    
    if limit == level:
        
        for b in before_board:
            answer_temp = max(answer_temp,max(b))
    
    # 4가지 방향으로 재귀호출을 하면서 dfs를 실행

    for i in range(4):
        # 해당하는 방향으로 움직였을 때 나올 수 있는 배열을 구하기
        board_temp = move(i, before_board)
        # 재귀호출을 진행
        recursive(level+1, board_temp)
    