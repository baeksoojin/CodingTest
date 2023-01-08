# 11시 2분 시작. 11시 19분 완료.

# 3방향으로 이동하는데 모두 1씩 결과값이 커지는 것으로 visited되지 않은 곳을 방문한다. 
# 3방향으로 모두 이동하고 또 이동한 곳에서 3방향을 모두 이동하는 식으로 해야하기에 bfs를 사용해야한다.

from collections import deque

n,m= map(int, input().split())
# bfs를 위해서 queue를 사용해 앞의 것부터 차례대로 뽑아내며 탐색한다.
queue = deque([(n,0)])
# 현재 수빈이의 위치와 time을 저장한다.

visited = [False]*100001

while(queue):

    x , time = queue.popleft()

    if x==m:
        print(time)
        break

    if x-1>=0 and visited[x-1]==False:
        queue.append((x-1,time+1))
        visited[x-1] = True
    if x+1<100001 and visited[x+1]==False:
        queue.append((x+1, time+1))
        visited[x+1] = True
    if x*2 < 100001 and visited[x*2]==False:
        queue.append((x*2,time+1))
        visited[x*2] = True

# 빨리 풀기에 집중하다보니 visited를 통해서 append를 중복으로 하는 것을 방지했어야했는데 체크하지 않아서 메모리초과가 나는 코드가 됨.
# 이후 visited를 추가하니 메모리초과가 나지 않고 통과가 됨.
