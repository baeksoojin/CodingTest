## BOJ 자료구조 오답풀이

### Z [1074] *시간초과*

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
따라서 딕셔너리를 사용해서 for문을 돌면서 다 비교해도 되지 않는다는 장점을 살려야하는데 그것을 살릴 수 없게끔 코드가 작성되었다. <br>
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
그렇다면 name을 통해서 number를 찾고 number를 통해서도 key를 찾을 수 있도록 2개의 딕셔너리를 만들어야겠다고 생각했다. 그렇다면 for문을 돌리지 않아도 된다. <br>
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

dictionary를 사용할 땐 "검색"과 같은 알고리즘을 작성할 때 유리하지만 그 장점을 살리기 위해서는 for문을 돌리지 않아야한다. 따라서 반드시 item을 기준으로 하나씩 돌리며 key와 value를 체크하는 경우가 필요한가? 에 대해서 코드를 작성할때 생각해보자!