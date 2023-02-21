# 단지번호 붙이기 1을 만날때마다 queue를 사용해서 1이 이어진 곳까지 이동하면서 count
# 7:57~

from collections import deque
n = int(input())
maps = []
for i in range(n):
    maps.append(input().rstrip())

visited = [[False]*(n) for _ in range(n)]

check_list = [(-1,0),(1,0),(0,1),(0,-1)]

def bfs(queue,count):

    while(queue):

        x,y = queue.popleft()
        count+=1

        for check in check_list:

            next_x = check[0] + x
            next_y = check[1] + y

            if next_x>=0 and next_x<=n-1 and next_y >=0 and next_y <=n-1:
                if visited[next_x][next_y]==False and maps[next_x][next_y] == '1':
                    queue.append((next_x, next_y))
                    visited[next_x][next_y] = True

    return count

result = 0 
results =[]
for i in range(n):
    for j in range(n):
        if maps[i][j]=='1' and visited[i][j]!=True:
            queue = deque([])
            queue.append((i,j))
            visited[i][j] = True
            results.append(bfs(queue,0))
            result +=1
            

print(result)
results.sort()
for r in results:
    print(r)
    