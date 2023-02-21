# cnt를 변화시키면서 갈 수 있는 곳을 x-1, x+1, x*2로 넣고 만약에 동생의 위치가 나왔다면 그것이 최소 cnt값이 될 것임
# 갈 수 있는 경우마다 cnt값이 같아야하니까 너비우선탐색을 적용

from collections import deque

n,k = map(int,input().split())

visited = [False]*(100001)

queue = deque([])
cnt = deque([])
queue.append(n)
cnt.append(0)
visited[n] = True

while(queue):
    
    soobin = queue.popleft()
    count = cnt.popleft()

    if soobin == k:
        print(count)
        break


    if soobin-1>=0 and visited[soobin-1]==False:
        queue.append(soobin-1)
        visited[soobin-1]=True
        cnt.append(count+1)
    if soobin+1<100001 and visited[soobin+1]==False:
        queue.append(soobin+1)
        visited[soobin+1]=True
        cnt.append(count+1)
    if soobin*2<100001 and visited[soobin*2]==False:
        queue.append(soobin*2)
        visited[soobin*2]=True
        cnt.append(count+1)