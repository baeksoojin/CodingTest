# BOJ 그리디 오답풀이

## 회의실 배정[1931]  *출력초과 및 틀렸습니다.*
처음에는 2^31을 못보고 2차원 배열을 만들어서 DP으로 풀기를 시도했다. 하지만 문제풀고 정답을 제출하려고 딱 보니 최대 숫자가 2^31이다. 따라서 최악의 경우 cache가 2^31+1개가 생성된다.<br>
DP로 풀면서 생각했던 아이디어와 비슷하게 가장 핵심은 끝나는 시간이 빨라야한다는 것이였다.<br>
~~~

import sys
input = sys.stdin.readline

n = int(input())

n_list = []
max_num =0
min_num = 0
for i in range(n):
    a,b = map(int, input().split())
    n_list.append((a,b))
    min_num = min(min_num, a)
    max_num = max(max_num, b)

# 2차원 리스트를 만들때 n+1행 max_num - min_num +1 개의 열을 만들어서 사용한다.

max_result = [[0]*(max_num+1) for _ in range(n+1)]

for i in range(1,n+1):
    a,b = n_list[i-1]
    for j in range(0,b):
        max_result[i][j]= max_result[i-1][j]
    for j in range(b,max_num+1):
        max_temp =0
        if a==0:
            max_temp = max_result[i-1][b]
        else:
            max_temp = max(max(max_result[i][:a])+1, max_result[i-1][b])
        max_result[i][j] = max_temp

# print(max_result)
print(max(max_result[n]))

# 시간초과와 메모리초과가 나올 것 같음 -> 2^31승일때...
# 실제로 메모리초과 나옴
~~~

[해결방법]<br>
해당 아이디어만 가지고 **그리디**를 통해서 문제를 풀어보자.
해당 아이디어를 가지고 입력값의 끝나는 시간을 가지고 정렬하였다.<br>
가장 빨리 끝나는 시간을 선택하고 그 타임 이후에는 또 다시 가장 빠르게 끝나는 시간을 선택한다. 이때 이전 타임의 끝나는 시간보다는 당연히 다음 시간대의 시작시간이 크거나 같아야한다는 것(조건)이다.<br>
따라서 나는 (a,b) 튜플로 입력받은 시작시간과 끝나는 시간이 담긴 list를 b를 Key로 하여 정렬한 뒤에 위의 조건문 걸고 for문을 돌리면 된다고 생각했다<br>

~~~
n = int(input())
cases =[]

for _ in range(n):
    a,b=map(int, input().split())
    cases.append((a,b))

cases = sorted(cases, key = lambda x : x[1])

count = 0
before_end_time =0

for case in cases:
    if case[0] >= before_end_time:
        count +=1
        before_end_time = case[1]
    else:
        continue

print(count)
~~~

그래서 다음과 같이 x[1](튜플의 두번째 값인 끝나는 시간)을 기준으로 정렬하고 for문을 돌리며 이전 끝나는 시간보다는 시작시간이 큰 것들중에서 가장 빠르게 끝나는 것을 선택하게 하였다<br>
하지만 이것역시, *틀렸습니다*가 나왔다.<br>

문제에서 빼먹은 조건이 있다<br>
시작시간과 끝나는 시간이 같아도 된다는 조건인데 이때도 회의실을 1번 사용한 것으로 카운팅 된다.<br>
위의 코드는 아래의 경우의 경우 정답이 2여야하지만 1을 반환한.<br>
```
2
5 5
1 5
```
1 5->5 5 가 되어야한다. 무조건 1 5가 먼저 5 5보다 선택되어야하는데 그러기 위해서는 *끝나는 시간이 같을 때 시작시간을 빠른 순서대로 정렬해야한다.* (for문으로 정렬된 list를 돌면서 우선으로 선택시킬 것이기 때문)<br>
위의 작성된 코드에서 한줄만 변경한다.<br>
~~~
cases = sorted(cases, key = lambda x : (x[1],x[0]))
~~~
x[0]을 두번째 key값으로 주어 x[1]을 정렬하고 x[1]의 값이 같다면 x[0]을 기준으로 정렬한다.<br>
가능한 경우가 2^31인 경우처럼 엄청나게 큰 수가 나오는 경우이다. 이 경우 입력받는 n의 수는 100,000이 최대이다. 이러한 변수를 봐서는 각 수가 갖는 것을 모두 구하면서 가장 큰 경우 혹은 가장 작은 경우를 찾는 DP가 아니라 *단계별로* 가장 큰 값을 선택하면서 넘어가는 그리디를 사용해야한다.<br>
그리디는 가장 큰 것을 선택하거나 가장 크게 변화하는 연산자를 선택하거나 가장 작은 것을 선택하는 등을 고려하는 문제의 유형인데 그렇기 때문에 **정렬**과 함께 사용되는 경우가 많다는 것을 항상 생각하면서문제를 풀어야한다.<br>