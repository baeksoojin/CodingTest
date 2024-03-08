'''
bfs를 사용
메모리 초과 -> 갔던곳 또가게 되면 100,000 -> 1초 초과 => visied를 사용해야함
'''

from collections import deque

start,end = map(int, input().split())

queue = deque([])
cnt_queue = deque([])
visited = [0]*100001

queue.append(start)
cnt_queue.append(0)
visited[start] = 1


def find_short_path(path, cnt):
    while path:
        before = path.popleft()
        before_cnt = cnt.popleft()
        after_cnt = before_cnt+1

        if before == end:
            print(before_cnt)
            break
        
        if before-1 >= 0 and visited[before-1]!=1:
            path.append(before-1)
            cnt.append(after_cnt)
            visited[before-1]=1
        if before+1 <= 100000 and visited[before+1]!=1:
            path.append(before+1)
            cnt.append(after_cnt)
            visited[before+1]=1
        if before*2 >= 0 and before*2<=100000 and visited[before*2]!=1:
            path.append(before*2)
            cnt.append(after_cnt)
            visited[before*2]=1


find_short_path(queue, cnt_queue)
