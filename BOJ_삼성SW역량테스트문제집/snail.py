'''
안에서 돌아서 0,0으로 가서 끝나는 달팽이 수열만들기
'''

n = int(input())


'''
n=5
[24, 23, 22, 21, 20]
[9, 8, 7, 6, 19]
[10, 1, 0, 5, 18]
[11, 2, 3, 4, 17]
[12, 13, 14, 15, 16]
'''

def snail1(n):
    current_x = (n // 2)
    current_y = (n // 2)

    current_dir_index  = 0
    move_count = num = 0
    cnt_limit = 1

    snail_list = [[0] * n for _ in range(n)]
    direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # 좌, 하, 우, 상

    while True:

        for _ in range(cnt_limit):
            dx, dy = direction[current_dir_index]
            current_x += dx
            current_y += dy
            if current_x == 0 and current_y == -1:
                return snail_list


            num+=1
            snail_list[current_x][current_y] = num

        move_count +=1
        current_dir_index = (current_dir_index + 1)%4
        if move_count == 2:
            cnt_limit +=1
            move_count = 0


temp = snail1(n)
for t in temp:
    print(t)

'''
[16, 15, 14, 13, 12]
[17, 4, 3, 2, 11]
[18, 5, 0, 1, 10]
[19, 6, 7, 8, 9]
[20, 21, 22, 23, 24]
'''
def snail2(n):

    current_x = n//2
    current_y = n//2

    direction = [(0,1), (-1,0), (0,-1), (1,0)] # 우상좌하
    current_dir_index = num = move_count = 0
    cnt_limit = 1

    snail_list = [[0]*n for _ in range(n)]

    while True:
        for i in range(cnt_limit):
            # cnt_limit만큼 방향에 따라서 이동
            num +=1
            dx, dy = direction[current_dir_index]
            current_x += dx
            current_y += dy
            if current_x == n-1 and current_y == n:
                return snail_list

            # snail_list의 값을 변경
            snail_list[current_x][current_y] = num

        move_count +=1
        current_dir_index = (current_dir_index + 1) % 4

        if move_count ==2:
            move_count = 0
            cnt_limit +=1


temp = snail2(n)
for t in temp:
    print(t)


'''
밖에서 진행되는 경우
'''

def snail3(n):

    if n==1:
        return [[1]]

    current_x = current_y = 0
    current_dir_index = 0

    snail = [[0]* n for _ in range(n)]
    for i in range(n**2):
        snail[current_x][current_y] = i+1

        if current_dir_index ==0 :
            # y증가
            current_y +=1
            # 마지막 위치거나 임 돈 곳을 간 경우
            if current_y+1 == n or snail[current_x][current_y+1]!=0:
                current_dir_index = 1
        elif current_dir_index == 1:
            # x증가
            current_x +=1
            if current_x+1 == n or snail[current_x+1][current_y]!=0:
                current_dir_index = 2
        elif current_dir_index == 2:
            # y감소
            current_y -=1
            if current_y-1==-1 or snail[current_x][current_y-1]!=0:
                current_dir_index = 3
        else:
            current_x -=1
            if current_x - 1 == -1 or snail[current_x-1][current_y] != 0:
                current_dir_index = 0

    return snail


temp = snail3(n)
for t in temp:
    print(t)