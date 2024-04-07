'''
1을 아래로 내리는 코드
'''

arr = [[0, 1, 0], [1, 0, 1], [0, 1, 0], [0, 0, 1], [0, 1, 0]]

print("기존")
for i in range(len(arr)):
    print(arr[i])

n = len(arr)
m = len(arr[0])
for i in range(n - 1):
    for j in range(m):
        print(i,j,"-----")
        p = i
        # 현재칸이 아래로 내려갈 수 있다면 그 윗줄도 한 칸 씩 연쇄적으로 내려와야함
        while 0 <= p and arr[p][j] == 1 and arr[p + 1][j] == 0:
            print(p,j)

            arr[p][j], arr[p + 1][j] = arr[p + 1][j], arr[p][j]
            for k in range(len(arr)):
                print(arr[k])
            p -= 1 # 그 위도 1이 연결되어있는지 탐색하며 0이랑 게속 변경
for i in range(len(arr)):
    print(arr[i])

'''
예를 들어서, 
2 0
[0, 0, 0]
[0, 1, 0]
[0, 1, 1]
[1, 0, 1]
[0, 1, 0]
해당 상태에서 다음 탐색의 대상이 2,1위치일때, 
2 1
[0, 0, 0]
[0, 1, 0]
[0, 0, 1]
[1, 1, 1]
[0, 1, 0]
1 1
[0, 0, 0]
[0, 0, 0]
[0, 1, 1]
[1, 1, 1]
[0, 1, 0]
'''

'''
비슷하게 장애물이 나오기 전까지 기울여서 (4가지 방향으로 중력)
다른게 있다면? 위에서는 움직이는 1이 1줄에 여러개라면 아래에서는 1줄에 움직이는게 1개임.!
'''
# 상,하,좌,우 -> 중력의 방향
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

board = [[0, 0, 0], [0, 1, 0], [0, 1, 0], [0, 2, 0], [0, 0, 0]]

def moving(x, y, move):
    while board[x + move[0]][y + move[1]] != 0:
        x += move[0]
        y += move[1]
        if board[x][y] == 2:
            return True
    return False

for m in move:
    print(m ,"->",moving(1,1, m))