'''

주사위 굴리기

주사위 굴리기를 진행
이동한 곳의 지도의 값이 0일때 => 주사위의 바닥면에 쓰여있는 수가 지도에 복사됨
이동한 곳의 지도의 값이 0이 아닌 경우 -> 칸에 쓰여있던 값이 주사위의 바닥면에 복사되고 지도의 값이 0으로 리셋

주사위를 이동시킬 때마다 상단에 쓰여있는 값(위)을 구하는 프로그램을 작성


-----

주사위의 상하좌우를 기록해놔야함

주사위의 각 면을 숫자로 구분하고 해당 숫자를 Key로 하고 그 면에 담긴 값을 value로 하는 dictionary를 이용해보자

주사위의 숫자를 가지고 방향을 변경 -> 숫자안의 값을 dictionary로 접근

<주사위의 숫자를 변경시키는 로직을 생각해야함>

위아래로 움직이는 경우는 각 경우를 고려해서 숫자를 위로 옮기거나 아래로 옮기면 됨
좌우로 움직이는 경우는 각 경우를 고려해서 역삼각형을 그리면서 4개를 바꿔줘야함.

'''

n,m,x,y,k_ = map(int, input().split())

# 맵을 입력받음
map_list = []
for i in range(n):
    map_list.append(list(map(int, input().split())))

# 주사위가 이동할 경우를 입력받음
k_list = list(map(int, input().split()))

# 주사위의 번호에 적힌 값을 초기화
box = {"1" : 0 ,
        "2" : 0 ,
        "3" : 0 ,
        "4" : 0 ,
        "5" : 0 ,
        "6" : 0 ,
        } #초기화 진행 

step = [-1,(0,1),(0,-1),(-1,0),(1,0)] # 차례대로 동서북남을 의미. -> k값으로 접근


# 주사위의 값을 저장
box_list = [4,1,3,2,5,6] #면

def change_dir(k):
    global box_list
    temp_box = [0]*6
    change_index = [0]*6
    if k==1: # 동쪽으로 이동시키는 경우
        # box_list의 index값을 가지고 다음 위치를 만들어줌
        change_index = [5, 0, 1, 3, 4, 2 ]# 예를들어서 기존에 3이있던 곳에 1을 넣어야하는데 1이 있는 index는 1이니까 1을 넣어줌.
    elif k==2: # 서쪽으로 이동하는 경우
        change_index = [1,2,5,3,4,0]
    elif k==3: # 북쪽으로 이동하는 경우
        change_index = [0,4,2,1,5,3]
    else: # 남쪽으로 이동하는 경우
        change_index = [0,3,2,5,1,4]

    # print(change_index)
    for i in range(len(change_index)):
            temp_box[i] = box_list[change_index[i]]
    # print(temp_box)
    
    box_list = temp_box
    # print("이동한 주사위 결과 :", box_list)
    

next_x,next_y = x,y

for k in k_list:
    
    # 주사위를 굴리기
    next_x += step[k][0]
    next_y += step[k][1]
    # print(next_x, next_y)

    #이동이 가능한 경우만 이동
    if next_x >=0 and next_x<n and next_y>=0 and next_y<m:

        # print("이동방향 k",k)
        # 굴리면서 변경된 면을 update해주는 로직작성
        change_dir(k)# 변경된 주사위의 전개도 리스트
        # print("box_list",box_list)
        # print(box_list)

        # 이동한 위치의 지도값이 0인지 판단
        if map_list[next_x][next_y]==0:#지도가 0이라면
            # 주사위의 바닥면에 쓰여있는 수가 지도에 복사됨
            map_list[next_x][next_y] = box[str(box_list[-1])]
            # print("update1")
        else: # 맵의 수가 주사위의 바닥면으로 업데이트
            # print("주사위바닥수",box_list[-1])
            box[str(box_list[-1])] = map_list[next_x][next_y]
            map_list[next_x][next_y] = 0 # 문제 조건 빼먹었었음 -> 문제 제대로 읽자....!!!!
            # print("update2")
        #상단에 적힌 값을 구하기
        print(box[str(box_list[1])])
    else:
        next_x -= step[k][0]
        next_y -= step[k][1]


    
