## BOJ 자료구조 오답풀이

### Z [1074] *메모리초과*

idea) 2*2에서 가장 왼쪽 위의 숫자만 알면 모두 알 수 있게 됨.<br>
8은 8//2 = 4 -> 4//2 = 2 로 쪼개서 생각하고 (2,2)의 행렬로 분할되었다면 멈춤<br>
위의 과정에서 나눠진 나머지값만큼으로 (0,0)에서 step이 Z 모양의 단계대로 이동하면서 나머지값의 제곱배에 Z의 단계(1,2,3단계 존재)로 곱해지며 2차원 행렬을 채워나가기<br>

~~~

# idea) 2*2에서 가장 왼쪽 위의 숫자만 알면 모두 알 수 있게 됨.
# 8은 8//2 = 4 -> 4//2 = 2 로 쪼개서 생각하고 (2,2)의 행렬로 분할되었다면 멈춤
# 위의 과정에서 나눠진 나머지값만큼으로 (0,0)에서 step이 Z 모양의 단계대로 이동하면서 나머지값의 제곱배에 Z의 단계(1,2,3단계 존재)로 곱해지며 2차원 행렬을 채워나가기

n,r,c = map(int, input().split())

n = 2**n # n으로 3이 주어지면 8*8행렬임
N = n
steps = [(0,1),(+1, 0),(1,1)] #순서대로 오른쪽, 아래, 대각선
# graph
graph = [[0]*n for _ in range(n)]
graph[0][0] = 0
visited = [(0,0)]

while(n>2):
    temp_n = n//2 # 4
    step_size = temp_n # 4칸씩 Z로 이동
    step_plus = temp_n**2 # 4*4의 값만큼 커짐
    n = n//2
    #print(step_size, step_plus)
    
    visited_temp = []
    for i in visited:
        count = 1
        #print("visit",i)
        for step in steps:
            # i마다 step별로 이동
            if (i[0]+step[0]*step_size) <= N-1 and (i[1]+step[1]*step_size)<N-1:
                graph[i[0]+step[0]*step_size][i[1]+step[1]*step_size] = graph[i[0]][i[1]] + step_plus * count
                #print("step",i[0]+step[0]*step_size,i[1]+step[1]*step_size,graph[i[0]][i[1]] + step_plus * count)
                visited_temp.append((i[0]+step[0]*step_size,i[1]+step[1]*step_size))
                count+=1
    visited = visited + visited_temp
    
    
for t in visited:
    i,j = t[0], t[1]
    count = 1
    for step in steps:
        graph[i + step[0]][j + step[1]] = graph[i][j] + count
        count +=1
# print(graph)
print(graph[r][c])

~~~

다음과 같이 작성했을 때 test case의 경우를 모두 만족했다. 하지만 메모리초과가 나왔다.
분할정복으로 풀어야한다. 재귀를 사용해야하는데, 위의 코드의 아이디어처럼 맨 왼쪽 위를 기준으로 3가지 경우로 나누고 2로 나누며 작게 작게 들어가야하는 것을 유지한채로 작성해봐야겠다고 생각했다. <br>

[해결방법]<br>
- 재귀를 사용<br>
장점 1) (r,c)가 체크하는 영역안에 없을 경우 바로 return하여 **가지치기**를 통해 **시간단축**이 가능하다. <br>
장점 2) for문을 계속 돌면서 체크해야하는 2차원 배열의 값을 계속 업데이트하지 않아도 되기에 **메모리감소**가 가능하다.<br>

위의 코드에서 나눈 몫에 제곱배를 한 것 처럼 지금 돌아가고 있는 몫의 값에다가 제곱배를 해줘야한다.<br>
```
N, r, c = map(int,input().split())

def Z(x, y, N):
    global res
    if x == r and y == c:
        print(res)
        exit(0)
    elif N == 1:
        res += 1
        return
    if not (x <= r < x + N) and not (y <= c < y + N):
        res += N ** 2
        return
    Z(x, y, N // 2)
    Z(x, y + N // 2, N // 2)
    Z(x + N // 2, y, N // 2)
    Z(x + N // 2, y + N // 2, N // 2)


global res
res = 0
Z(0, 0, 2 ** N)

```
---
### 나는야 포켓몬 마스터 이다솜[1620] *시간초과* <br>

해당 문제를 봐서 key, value로 이루어진 딕셔너리를 사용한다면 쉽게 풀 수 있을 것 같았다. 하나의 딕셔너리를 만들어서 key로 name을 보관하고 value로 index를 보관하려고했었다. 그러나 value를 가지고 key를 찾아야하는 경우에 value를 가지고 있는 key를 역으로 찾는 과정이 어렵기 때문에 items list를 받아서 for문을 돌면서 체크하려고 했다. <br>
따라서 딕셔너리를 사용해서 in 연산자를 사용하면 시간복잡도를 줄일 수 있기에, for문을 돌면서 다 비교해도 되지 않는다는 장점을 살려야하는데 그것을 살릴 수 없게끔 코드가 작성되었다. <br>
~~~
import sys
input = sys.stdin.readline
n ,m = map(int,input().split())
pocketmons = {}

for i in range(1,n+1):
    name = input().strip()
    pocketmons[name] = str(i)

for i in range(m):
    question = input().strip()

    for p in pocketmons.items():
        if question == p[0]:
            print(p[1])
            break
        if question == p[1]:
            print(p[0])
            break
~~~

[해결방법]<br>
그렇다면 name을 통해서 number를 찾고 number를 통해서도 key를 찾을 수 있도록 2개의 딕셔너리를 만들어야겠다고 생각했다. in 연산자를 사용한다면 for문을 돌리지 않아도 된다. 따라서 시간복잡도를 줄일 수 있게된다. <br>
~~~
import sys
input = sys.stdin.readline
n ,m = map(int,input().split())

key_name = {} # 이름을 입력했을 때 숫자가 나오도록
key_num = {} # 숫자를 입력했을 때 이름이 나오도록

for i in range(1,n+1):
    name = input().strip()
    key_name[name] = str(i)
    key_num[str(i)] = name

for _ in range(m):
    ques = input().strip()
    # 이름으로 입력받을 때
    if ques in key_name.keys():
        print(key_name[ques])
    else:
        print(key_num[ques])
~~~

dictionary를 사용할 땐 "검색"과 같은 알고리즘을 작성할 때 유리하지만 그 장점을 살리기 위해서는 in 연산자를 적극 사용해서 for문을 돌리지 않아야한다. 따라서 반드시 item을 기준으로 하나씩 돌리며 key와 value를 체크하는 경우가 필요한가? 에 대해서 코드를 작성할때 생각해보자!

------
### 듣보잡 *시간초과*<br>

두번에 걸쳐 입력받아진 string들 중에 공통된 string을 뽑아서 정렬하는 문제이다.<br>
이때 "in"을 사용했는데 시간초과가 난 이유는 list에 in 연산을 적용했기 때문이다.<br>

```
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

list1 =[]
list2 =[]


for i in range(n):
    list1.append(input().strip())
for i in range(m):
    temp = input().strip()
    if temp in list1:
        list2.append(temp)

list2.sort()
print(len(list2))
for i in list2:
    print(i)
```

[해결방법]
in 연산을 사용하게 되는데 그 시간복잡도는 평균 O(n)으로 list의 개수에 in 연산이 의존하고 있다. 하지만 dictionary로 계산할 경우 in 연산을 사용하면 list의 개수에 의존하지 않고(크기에 상관없이) 일정한 연산을 ㅅ행하며 시간복잡도는 O(1)이다. <br>
**in 연산을 사용할 때는 dictionary를 사용하자**<br>
```
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

list1 ={}
list2 =[]


for i in range(n):
    list1[input().strip()]=i
for i in range(m):
    temp = input().strip()
    if temp in list1.keys():
        list2.append(temp)

list2.sort()
print(len(list2))
for i in list2:
    print(i)
```
list1을 dictionary로만 바꿨는데 시간초과가 해결되었다.<br>

하지만 dictionary가 아니여도 풀 수 있다. 문제를 풀면서 두개의 교집합을 찾아내는 연산의 기능을 하는 method같은 것이 없나 찾아보았다. set을 사용해서 교집합을 얻을 수 있다.<br>
*intersection*<br>

- 만약 두개의 set set1, set2가 존재할때
*& 연산자와 intersection method*를 사용한다<br>
    ```
    set.intersection(set1, set2)
    ```
    혹은 
    ```
     set1 & set2
    ```
- 만약 set1에 set2와의 교집합을 구하고 바로 set1에 update하고 싶을때
    ~~~
    set1 = {1,2,3}
    set2 = {1,3}

    set1.intersection_update(set2)
    print(a)
    ~~~
    를 할경우 {1,2}로 교집합이 set1에 저장된다.

집합의 교집합 메서드 혹은 연산자를 사용한다면 쉽게 풀 수 있을 것이다.
```
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

set1 = set()
set2 = set()

for i in range(n):
    set1.add(input().strip())
for i in range(m):
    set2.add(input().strip())

result = sorted(list(set1 & set2))
print(len(result))
for i in result:
    print(i)
```
------
### 토마토[7576] 시간초과

idea) bfs를 사용하는데 for문을 돌면서 입력값이 1일때 해당 위치에서 bfs를 실행하게끔 하였다. 만약 1이 두번일때는 첫번째 1을 만났을 때 bfs를 한번 실행하여 while문을 실행하여 tomato에 대한 상태값이 모두 업데이트된다. 하지만 두번째 1이 첫번째 1의 결과로 나온 tomato가 익은 날짜보다 더 빠르게 익었을 수도 있기때문에 첫번째 1이 나왔을때의 특정 자리에서 익은 토마토가 익기 위해서 걸리 날짜와 현재 그 자리의 토마토가 익기 위해서 걸린 날짜를 비교해서 더 작은 값을 update해주었다. <br>

~~~
import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())

tomato = []*(m)
for i in range(m):
    tomato.append(list(map(int, input().split())))

map_list = [(-1,0),(+1,0),(0,-1),(0,+1)] # 상하좌우 이동

def tomato_bfs(x,y,count_list):

    visited =[[False]*(n) for _ in range(m)]
        
    queue = deque([])
    queue.append((x,y))

    count = deque([])
    count.append(0)

    visited[x][y]=False
    count_list[x][y] = 0

    while(queue):
        
        x,y = queue.popleft()
        c = count.popleft()

        for map in map_list:
            a,b = map
            next_x = x +a
            next_y = y +b
            
            if next_x >m-1 or next_x<0 or next_y > n-1 or next_y<0:
                continue
            elif tomato[next_x][next_y] == -1:
                continue
            else: #갈 수 있을 경우 min값을 비교하는 조건고려
                if visited[next_x][next_y]==False and c+1 < count_list[next_x][next_y]:
                    #print(next_x,next_y)
                    visited[next_x][next_y]==True
                    count_list[next_x][next_y] = c+1
                    queue.append((next_x, next_y))
                    count.append(c+1)
    return count_list

INF = int(1e10)
count_list =[[INF]*(n) for _ in range(m)]
for i in range(m):
    for j in range(n):
        if tomato[i][j]==1:
            count_list = tomato_bfs(i,j,count_list)

# min값으로 비교하는 것을 추가해야함

# 다 익을 수 없는 경우
if 0 in tomato:
    print("-1")
else:
    result = []
    for i in range(m):
        result += count_list[i]
    result = list(set(result))
    result.remove(INF)
    print(max(result))
~~~
그러나 시간적인 측면에서 본다면 1이 나올때마다 bfs를 한번 호출하게 되어 비효율적이다.<br>
어떻게 시간초과를 해결할 수 있을까? 1이 나올때의 값을 deque에 넣고 bfs를 한번만 호출하게 하고 day를 담는 count_list를 없애고 counting값을 늘리면서 방문한 곳은 방문하지 않도록하여 자연스럽게 deque에 담긴 곳이 없을때의 counting값이 모두 익는데 걸리는 최솟값이 된다.<br>

[해결방법]<br>
count_list를 업데이트 하기보다는 입력받은 값이 1일때의 위치를 deque에 모두 저장하고 또 다른 deque를 만들어서 day counting값을 저장한다. 때문에 해당 bfs에서 counting값이 level과 같은 것으로 이해한다면 level이 같은 것으로 본다면 각 레벨은 *동시에 실행(즉, 동시에 상하좌우를 익힌다)*한다라고 이해하면 될 것이다.
~~~
import sys
from collections import deque
from tabnanny import check

input = sys.stdin.readline

n,m = map(int, input().split())

tomato = []*(m)
for i in range(m):
    tomato.append(list(map(int, input().split())))

map_list = [(-1,0),(+1,0),(0,-1),(0,+1)] # 상하좌우 이동

visited =[[False]*(n) for _ in range(m)]
queue = deque([])
counting = deque([])
def tomato_bfs(queue, counting):
    count = 0
    while(queue):
        
        x,y = queue.popleft()
        count = counting.popleft()

        for map in map_list:
            a,b = map
            next_x = x +a
            next_y = y +b
            
            if next_x >m-1 or next_x<0 or next_y > n-1 or next_y<0:
                continue
            else: 
                if visited[next_x][next_y]==False:
                    visited[next_x][next_y]=True
                    queue.append((next_x, next_y))
                    counting.append(count + 1)
    return count


INF = int(1e10)
for i in range(m):
    for j in range(n):
        if tomato[i][j]==1:
            queue.append((i,j))
            counting.append(0)
            visited[i][j]=True
        if tomato[i][j]==-1:
            visited[i][j] = True
result = tomato_bfs(queue,counting)

def check_minus():
    for v in visited:
        if False in v:
            return 1
    return 0

if check_minus():
    print("-1")
else:
    print(result)
~~~

----
### 이중 우선순위 큐 *시간초과*

idea) heapq 두개 사용해서 최솟값이랑 최댓값을 뽑아내고 하나의 수가 삭제됐을 때 다른 heapq에서 해당 수를 제거해야한다고 생각하였다. 따라서 heapq를 list를 사용한 것이기에 list의 remove method를 사용하면 되겠다고 생각하였다.<br>

```
import sys
import heapq
input = sys.stdin.readline

n = int(input())

for _ in range(n):

    minh = []
    maxh =[]
    
    count = int(input())
    for _ in range(count):
        o, num = map(str,input().split())
        if o=="I":
            heapq.heappush(minh, int(num))
            heapq.heappush(maxh, -int(num))
        else:
            if len(minh)==0:
                continue
            if num == "-1": #최솟값을 삭제
                del_num = heapq.heappop(minh)
                maxh.remove(-del_num)
            else:#최댓값을 삭제
                del_num = -heapq.heappop(maxh)
                minh.remove(del_num)
    
    if not minh:
        print("EMPTY")
    else:
        max = -heapq.heappop(maxh)
        min = heapq.heappop(minh)
        print(max, min)

```

그러나 문제를 풀고 시간초과가 떠서 확인해보니 remove method를 사용해서는 안 됐다.<br>
remove의 시간복잡도는 O(N)이다. for문을 n번 돌면서 찾아내는 것을 의미하는데 따라서 시간초과가 난 것 같아서 remove가 아닌 다른 방법을 생각해냈어야 했다.<br>

[해결방법]<br>
따라서 값을 힙에 저장할때 값과 함께 그 값을 구분해줄 숫자를 함께 넣어서 해당 값이 빠졌는지 아직 있는지를 체크하도록 한다.<br>
```
if o=="I":
    heapq.heappush(minh, (int(num),key))
    heapq.heappush(maxh, (-int(num),key))
```
바로 위의 for문에서 index를 사용할 일이 없어서 _ 처리를 하였는데 이를 key로 바꾸고 위의 코드처럼 변경하도록하여 tuple을 각 heap에 저장한다.<br>
key값이 True일때 해당 값이 존재하는 것이고 만약 둘중 하나의 heap에서 값이 삭제됐다고 한다면 다른 하나의 heap에서도 삭제 되어야하기에 False로 만든다. 따라서 각 heap에서는 상대heap에 의해서 삭제된 원소인지 체크하고(False일때) 그 값이 가장 첫번째 원소에 있을 때 해당 값은 상대에 의해서 이미 제거된 값이기에 역시 해당 Heap에서도 제거해준다.<br>
```
while heap and not visited[heap[0][1]]:
    heapq.heappop(heap)
```
다음과 같은 코드를 최소힙, 최대힙에서 적용시켜야한다<br>
~~~

import sys
import heapq
input = sys.stdin.readline

n = int(input())


for _ in range(n):

    minh = []
    maxh =[]
    
    count = int(input())
    visited = [False]*count
    for key in range(count):
        o, num = map(str,input().split())
        if o=="I":
            heapq.heappush(minh, (int(num),key))
            heapq.heappush(maxh, (-int(num),key))
            visited[key] = True
        else:
            if num == "-1": #최솟값을 삭제
                while minh and not visited[minh[0][1]]:
                    heapq.heappop(minh)
                if minh:
                    visited[minh[0][1]] = False
                    heapq.heappop(minh)
                    
            else:#최댓값을 삭제
                while maxh and not visited[maxh[0][1]]:
                    heapq.heappop(maxh)
                if maxh:
                    visited[maxh[0][1]] = False
                    heapq.heappop(maxh) 
                    

    while minh and not visited[minh[0][1]]:
        heapq.heappop(minh)
    while maxh and not visited[maxh[0][1]]:
        heapq.heappop(maxh)
    
    if not minh:
        print("EMPTY")
    else:
        max,key1 = heapq.heappop(maxh)
        min,key2 = heapq.heappop(minh)
        print(-max, min)
~~~

list에서 pop(i), remove, insert, del, in 모두 시간복잡도는 O(N)으로 하나의 숫자를 찾거나 없애거나 넣을때 for문을 돌면서 하나씩 비교하며 업데이트 된다고 생각하면 된다. 따라서 method를 쓴다고해서 시간복잡도를 줄이는 것이 되지 않는다. <br>
해당 사항을 주의하면서 문제플 풀어야겠다.