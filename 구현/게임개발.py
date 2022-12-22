#방문한 칸수를 출력.

n,m = map(int, input().split())

#1. 반시계 방향으로 이동
steps = [(0,-1), (-1,0),(0,1),(1,0),(0,-1),(0,1),(1,0)]

i,j,start = map(int, input().split())


#2. 캐릭터의 왼쪽이 가보지 않았다면 이동하고 아니면 회전만 수행하고 다시 그 위치부터 갈 곳이 있나 체크. //0일때 육지 이동.
#3. 만약 네 방향다 못 가는 경우, 바라보는 방향을 유지하고 한칸 뒤로 가고 1단계로 돌아감 => step에서 size를 2만큼 빼면 뒤로가는데 이때 뒤가 바다라면 움직임을 멈춘다.

visited = [[0]*(m+1) for _ in range(n+1)]
visited[i][j]=1

maps = []
for _ in range(n):
    maps.append(list(map(int,input().split())))

is_change = False
count = 1

while(1):
    is_change=False
    for t in range(4):# 회전 시키기
        next_i = steps[start+t][0] + i
        next_j = steps[start+t][1] + j
        if next_i < 0 or next_j <0 or next_i > n-1 or next_j > m-1:
            continue #다음방향으로 넘김
        if visited[next_i][next_j] ==0 and maps[next_i][next_j]==0:
            i = next_i
            j = next_j
            start = t
            visited[next_i][next_j] =1
            count +=1
            is_change = True
            break
    if is_change == False:
        back_i = steps[start-2][0] +i
        back_j = steps[start-2][1] + j
        if maps[back_i][back_j]==1:
            print(count)
            break
        else:
            i = back_i
            j = back_j


##
# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1
## 답 3
            



        
       