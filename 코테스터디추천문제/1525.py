'''
퍼즐문제

이동하는 경우를 구해야하는데 어떤 숫자가 이동하는지 하나의 level에서 여러개의 경우를 고려해야한다.
따라서 bfs를 사용해야하고 돌면서 최솟값을 체크해야하는 문제이다.

90%에서 틀렸습니다가 나옴...=>cnt 0일때를 체크안시켜줌.

'''

from collections import deque

check_list = [(-1,0),(1,0),(0,-1),(0,1)]

string_list = '123456780'
find_string = ""
visited = {}

def bfs(queue):

    while queue:
        
        string_temp , cnt = queue.popleft()

        if string_temp==string_list:
            # print(cnt)
            return cnt

        current_zero_index = string_temp.index('0')
        # print(current_zero_index)

        current_x = current_zero_index//3
        current_y = current_zero_index%3
        
        for check in check_list:
            next_x = current_x + check[0]
            next_y = current_y + check[1]
            # 바꿀 위치인(next_x, next_y)와 현재 위치인(current_x, current_y)를 바꿔줘야함.
            # 현재 위치에 바꿀 위치의 값을 넣고 바꿀 위치의 값을 0으로 변경
            # 
            if next_x>=0 and next_x<3 and next_y<3 and next_y>=0:
                
                list_temp = list(string_temp)
                next_zero_index = next_x*3 + next_y
                list_temp[next_zero_index],list_temp[current_zero_index] = list_temp[current_zero_index], list_temp[next_zero_index]
                next_string = ''.join(list_temp)
                if next_string not in visited.keys():
                    # print(next_string)
                    visited[next_string] = 1
                    queue.append((next_string, cnt+1))
          

for i in range(3):
    temp = input().rstrip()
    temp = temp.replace(" ","")
    find_string+= temp

# print("first",find_string)

queue =deque()
if find_string==string_list:
    print(0)
else:
    queue.append((find_string, 0)) # string과 cnt를 저장
    visited[find_string] = 1
    result = bfs(queue)
    if result:
        print(result)
    else:
        print("-1")



    
